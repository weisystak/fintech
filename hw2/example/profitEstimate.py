import sys
import numpy as np
import pandas as pd
from myStrategy import myStrategy

df = pd.read_csv(sys.argv[1])
adjClose = df["Adj Close"].values
capital=1
capitalOrig=capital
dataCount=len(adjClose)
suggestedAction= np.zeros((dataCount,1))
stockHolding=np.zeros((dataCount,1))
total = np.zeros((dataCount,1))
realAction=np.zeros((dataCount,1))
total[0] = capital
for ic in range(dataCount):
    currPrice=adjClose[ic]
    suggestedAction[ic]=myStrategy(adjClose[0:ic], currPrice)
    if ic > 0:
        stockHolding[ic]=stockHolding[ic-1]
    if suggestedAction[ic] == 1:
        if stockHolding[ic]==0:            
            stockHolding[ic]=capital/currPrice
            capital=0
            realAction[ic]=1
    elif suggestedAction[ic] == -1:
        if stockHolding[ic]>0:
            capital=stockHolding[ic]*currPrice
            stockHolding[ic]=0
            realAction[ic]=-1
    elif suggestedAction[ic] == 0:
        realAction[ic]=0
    else:
        assert False
    total[ic]=capital+stockHolding[ic]*currPrice
returnRate=(total[-1]-capitalOrig)/capitalOrig     
