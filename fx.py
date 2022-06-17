import fxcmpy
from pylab import plt
import pandas as pd

TOKEN = "input your fxcm token here"
con = fxcmpy.fxcmpy(access_token=TOKEN, log_level='error')
con.get_instruments()

df = con.get_candles('USD/JPY', period='m1', number=250)
df.head()

plt.style.use('seaborn')
%matplotlib inline
df['askclose'].plot(figsize=(10, 6));

plots = df[['bidclose', 'tickqty']].plot(subplots=True, figsize=(10, 10))
plt.show()

df['ma50'] = pd.rolling_mean(df['bidclose'], 50)
df['ma200'] = pd.rolling_mean(df['bidclose'], 200)
plots = df[['bidclose', 'ma50', 'ma200']].plot(subplots=False, figsize=(10, 4))
plt.show()

df['ma50'] = pd.rolling_mean(df['bidclose'], 50)
df['ma200'] = pd.rolling_mean(df['bidclose'], 200)
plots = df[['bidclose', 'ma50', 'ma200']].plot(subplots=False, figsize=(10, 4))
plt.show()
