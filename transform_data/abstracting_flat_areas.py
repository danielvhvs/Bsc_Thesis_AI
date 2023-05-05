import numpy as np
import pandas as pd
import os
from .determine_gradient import *

from sklearn.preprocessing import OrdinalEncoder
from .misc import *

def flat_areas(flatList,flatLength,flatChange):
    newFlatList = []
    idx = 0
    while idx < len(flatList):
        i=idx
        count = 1
        value = flatList[idx]
        while i<len(flatList):
            if (flatList[i]==value):
                count+=1
                i+=1
            else:
                i+=1
                break
        newFlatList.append((value,count))
        idx = i
    abstract = []
    if (newFlatList == []):
        return abstract
    value = newFlatList[0][0]
    for idx,x in enumerate(newFlatList[1:]):
        if x[1]>=flatLength and np.abs(x[0]-value) >= flatChange:
            if x[0]-value >=0:
                abstract.append("Higher")
            else:
                abstract.append("Lower")
    return abstract
        
            