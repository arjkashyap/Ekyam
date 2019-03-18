from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
import numpy as np
import pandas as pd
import quandl
import math
import numpy as np
from sklearn import preprocessing , cross_validation , svm
from sklearn.linear_model import LinearRegression
import datetime

from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    return render(request, 'main/home.html')

@login_required
def incubators(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    incubators = Incubators.objects.all().exclude(verify = False)
    pos = Incubators.objects.values_list('latt', 'lonn')
    a = np.array(pos)
    lat1=[]
    long1=[]
    for i in range(len(a)):
        lat1.append(a[i][0])
        long1.append(a[i][1])
    return render(request, 'main/incubators.html', {"incubators": incubators ,'lat' : lat1 , 'lng':long1 })

@login_required
def about(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    return HttpResponse("About")

@login_required 
def result(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    # Shows the matched result
    query = request.GET.get('inc_search')
    check = Incubators.objects.filter(incubator_name__icontains= query).exclude(verify = False)
    return render(request, 'main/results.html', {'incubators': incubators,'check': check})

@login_required
def details(request, incubator_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    inc = get_object_or_404(Incubators, pk = incubator_id)
    details = Details.objects.get(pk = incubator_id)
    return render(request, 'main/details.html', {'inc': inc, 'details': details})

@login_required
def locate(request, incubator_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    pos = Incubators.objects.values_list('latt', 'lonn').filter(pk = incubator_id)
    return render(request, 'main/locate.html', {'pos': pos, 'incubator_id': incubator_id})


class AddIncubator(CreateView):
    model = Incubators
    fields = ['incubator_name', 'owner', 'city_location', 'description', 'logo', 'latt', 'lonn']


class AddDetails(CreateView):
    model = Details
    field = ['incubator', 'inc_name']

@login_required
def news(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    return render(request, 'main/news.html')

@login_required
def added(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    return render(request, 'main/added.html', context = None)

@login_required
def apply(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    return render(request, 'main/inc_apply.html')

@login_required
def done(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    return render(request, 'main/done.html')

@login_required
def location(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    incubators = Incubators.objects.all().exclude(verify = False)
    pos = Incubators.objects.values_list('latt', 'lonn')

    a = np.array(pos)
    lat1=[]
    long1=[]
    for i in range(len(a)):
        lat1.append(a[i][0])
        long1.append(a[i][1])
    return render(request, 'main/location.html', {"incubators": incubators ,'lat' : lat1 , 'lng':long1 })

@login_required
def prediction(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    auth_tok = 'MozuEJfqJDDqS-LqWgh1'
    df = quandl.get('WIKI/GOOGL',authtoken=auth_tok)
    df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
    df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
    df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
    df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]

    forecast_col = 'Adj. Close'
    df.fillna(-99999,inplace=True)

    forecast_out = int(math.ceil(0.01*len(df)))
    df['label'] = df[forecast_col].shift(-forecast_out)


    x = np.array(df.drop(['label'],1))
    x = preprocessing.scale(x)
    x = x[:-forecast_out]
    x_lately = x[-forecast_out:]
    df.dropna(inplace = True)
    y = np.array(df['label'])
    y = np.array(df['label'])
    X_train , X_test , y_train , y_test = cross_validation.train_test_split(x,y,test_size=0.2)
    clf = LinearRegression(n_jobs = -1)
    clf.fit(X_train , y_train)
    accuracy = clf.score(X_test,y_test)

    forecast_set = clf.predict(x_lately)


    df['Forecast'] = np.nan
    last_date = df.iloc[-1].name
    last_unix = last_date.timestamp()
    one_day = 86400
    next_unix = last_unix + one_day

    for i in forecast_set:
        next_date = datetime.datetime.fromtimestamp(next_unix)
        next_unix += one_day
        df.loc[next_date] = [np.nan for _ in range(len(df.columns) - 1)] +[i]

    x1 = [2005,2007,2009,2011,2013,2015]
    y1= []
    c1 = np.array(df['Forecast'])
    v1 = np.array(df['Adj. Close'])
    print("!!!!!!!@@@@@@@@@@########")
    for i in range(len(c1)):
        if(math.isnan(c1[i]) == True):
            c1[i] = 0
    for i in range(len(v1)):
        if(math.isnan(v1[i]) == True):
            v1[i] = 0
    c2 = []
    v2 = []
    for i in range(len(c1)):
        c2.append(c1[i])
    for i in range(len(v1)):
        v2.append(v1[i])
    
    return render(request, 'main/prediction.html', {'Forecast': c2 , 'AdjClose':v2})

def startups(request):
    return render(request, 'main/startups.html')