import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt


TickerA='ITSA4.SA'
TickerB='FLRY3.SA'
TickerC='LREN3.SA'
prices=pd.DataFrame()
tickers = [TickerA, TickerB, TickerC]

for t in tickers:
    prices[t]=wb.DataReader(t, data_source='yahoo', start='2010-1-1')['Adj Close']

#PRECOS DAS ACOES
(prices/prices.iloc[0]*100).plot(figsize=(15,5)) #onde prices.iloc[0] é o valor inicial do ativo

plt.ylabel('NORMALIZED PRICES')
plt.xlabel('DATE')
plt.show()

#RETORNOS DIÁRIOS
''' 
retorno = (preco_dia_1 - preco_dia_0)/preco_dia_0
'''
#prices.shift(1) toma o valor da linha acima da linha atual
log_returns=np.log(prices/prices.shift(1))

log_returns.plot(figsize=(15,5))
plt.ylabel('LOG DAILY RETURNS')
plt.xlabel('DATE')
plt.show()

#RETORNOS DIÁRIOS MÉDIO
print(log_returns.mean())

#RETORNOS ANUAIS MÉDIO
print(log_returns.mean()*250) #onde 250 é a média diária de dias úteis em um ano