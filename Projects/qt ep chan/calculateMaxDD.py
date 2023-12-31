import pandas as pd
import numpy as np


def calculateMaxDD(cumret):
    #calculation of max drawdown and max drawdown duration based on cumulutative COMPUNDED returns.
    #cumret must be a compunded cumulative return 
    #i is the index of the day with maxDD

    highwatermark = np.zeros(cumret.shape)
    drawdown = np.zeros(cumret.shape)
    drawdownduration = np.zeros(cumret.shape)
    
    for t in np.arange(1,cumret.shape[0]):
        highwatermark[t]=np.maximum(highwatermark[t-1],cumret[t])
        drawdown[t] = (1+cumret[t])/(1+highwatermark[t])-1
        if drawdown[t]==0:
            drawdownduration[t] = 0
        else:
            drawdownduration[t] = drawdownduration[t-1]+1
    
    maxDD, i = np.min(drawdown), np.argmin(drawdown) #drawdown < 0 always
    maxDDD = np.max(drawdownduration)
    return maxDD, maxDDD, i 