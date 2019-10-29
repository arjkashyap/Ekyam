import K1QWE as k
import pandas as pd
import quandl
import math
import numpy as np
from sklearn import preprocessing , cross_validation , svm
from sklearn.linear_model import LinearRegression
import datetime
import matplotlib.pyplot as plt
from matplotlib import style

auth_tok = 'ozznMBmrYaK5QcBngxUq'

def _dsa():
    style.use('ggplot')

    auth_tok = 'ozznMBmrYaK5QcBngxUq'
    _Q12 = quandl.get('WIKI/GOOGL',authtoken=auth_tok)
    _Q12 = _Q12[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume',]]
    _Q12['HL_PCT'] = (_Q12['Adj. High'] - _Q12['Adj. Close']) / _Q12['Adj. Close'] * 100.0
    df['PCT_change'] = (_Q12['Adj. Close'] - _Q12['Adj. Open']) / _Q12['Adj. Open'] * 100.0
    _Q12 = _Q12[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]
    forecast_col = 'Adj. Close'
    df.fillna(-99999,inplace=True)

    forecast_out = int(math.ceil(0.01*len(df)))
    ##### Future market condition predicition #####
    _Q12['label'] = _Q12[forecast_col].shift(-forecast_out)


    x = np.array(_Q12.drop(['label'],1))
    x = preprocessing.scale(x)
    x = x[:-forecast_out]
    x_lately = x[-forecast_out:]
    _Q12.dropna(inplace = True)
    y = np.array(_Q12['label'])
    y = np.array(_Q12['label'])
    X_train , X_test , y_train , y_test = cross_validation.train_test_split(x,y,test_size=0.2)
    clf = LinearRegression(n_jobs = -1)
    clf.fit(X_train , y_train)
    accuracy = clf.score(X_test,y_test)

    forecast_set = clf.predict(x_lately)


    _Q12['Forecast'] = np.nan
    last_date = _Q12.iloc[-1].name
    last_unix = last_date.timestamp()
    one_day = 86400
    next_unix = last_unix + one_day

    for i in forecast_set:
        next_date = datetime.datetime.fromtimestamp(next_unix)
        next_unix += one_day
        _Q12.loc[next_date] = [np.nan for _ in range(len(_Q12.columns) - 1)] +[i]
    print("####")
    _Q12['Adj. Close'].plot()
    _Q12['Forecast'].plot()
    plt.legend(loc = 4)
    plt.xlabel('Date')
    plt.ylabel('price')
    plt.show()
    print("####")
    print("####")
    _Q12= _Q12.values
    _Q12.tolist()
    auth_tok = 'ozznMBmrYaK5QcBngxUq'
    _Q12 = quandl.get('WIKI/GOOGL',authtoken=auth_tok)
    _Q12 = _Q12[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume',]]
    _Q12['HL_PCT'] = (_Q12['Adj. High'] - _Q12['Adj. Close']) / _Q12['Adj. Close'] * 100.0
    df['PCT_change'] = (_Q12['Adj. Close'] - _Q12['Adj. Open']) / _Q12['Adj. Open'] * 100.0
    _Q12 = _Q12[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]
    forecast_col = 'Adj. Close'
    df.fillna(-99999,inplace=True)

    forecast_out = int(math.ceil(0.01*len(df)))
    _Q12['label'] = _Q12[forecast_col].shift(-forecast_out)


    x = np.array(_Q12.drop(['label'],1))
    x = preprocessing.scale(x)
    x = x[:-forecast_out]
    x_lately = x[-forecast_out:]
    _Q12.dropna(inplace = True)
    y = np.array(_Q12['label'])
    y = np.array(_Q12['label'])
    X_train , X_test , y_train , y_test = cross_validation.train_test_split(x,y,test_size=0.2)
    clf = LinearRegression(n_jobs = -1)
    clf.fit(X_train , y_train)
    accuracy = clf.score(X_test,y_test)

    forecast_set = clf.predict(x_lately)


    _Q12['Forecast'] = np.nan
    last_date = _Q12.iloc[-1].name
    last_unix = last_date.timestamp()
    one_day = 86400
    next_unix = last_unix + one_day

    for i in forecast_set:
        next_date = datetime.datetime.fromtimestamp(next_unix)
        next_unix += one_day
        _Q12.loc[next_date] = [np.nan for _ in range(len(_Q12.columns) - 1)] +[i]
    print("####")
    _Q12['Adj. Close'].plot()
    _Q12['Forecast'].plot()
    plt.legend(loc = 4)
    plt.xlabel('Date')
    plt.ylabel('price')
    plt.show()
    print("####")
    print("####")
    _Q12= _Q12.values
    _Q12.tolist()
def _getData():
    return quandl.get('WIKI/GOOGL',authtoken=auth_tok)
