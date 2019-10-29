import K1QWE as k
import pandas as pd
import getData as gd
import quandl
import math
import numpy as np
from sklearn import preprocessing , cross_validation , svm
from sklearn.linear_model import LinearRegression
import datetime
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

auth_tok = 'ozznMBmrYaK5QcBngxUq'
#df = quandl.get('WIKI/AAPL',authtoken=auth_tok)
df = gd._getData()
#df = quandl.get('WIKI/AAPL',authtoken=auth_tok)
df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume',]]
#here output csv file
MF = df
MF = np.array(df)
b1 = open('test.csv','w')
for item in MF:
  b1.write("%s\n" % item)
b1.close()
print(df)

df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]
forecast_col = 'Adj. Close'
df.fillna(-99999,inplace=True)

forecast_out = int(math.ceil(0.01*len(df)))
#print(forecast_out)

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

#print(forecast_set, accuracy , forecast_out)
k._REW012('0x0728')
df['Forecast'] = np.nan
last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns) - 1)] +[i]

print("####")

#print(df['Adj. Close'])
#print(df['Forecast'])
df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc = 4)
plt.xlabel('Date')
plt.show()
print("####")
#print(df['Forecast'])
print("####")
df= df.values
df.tolist()
print(df[0][1])

