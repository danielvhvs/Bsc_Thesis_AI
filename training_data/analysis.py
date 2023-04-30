import pandas as pd
import os
import numpy as np
from matplotlib import pyplot as plt

def stats(fileName):
    df = pd.read_csv(fileName)

    TQ, FQ, TS, FS = (0,0,0,0)
    for idx in range(len(df)):
        if df["Question"][idx] >= df["Statement"][idx]:
            if "question"==df["Outcomes"][idx]:
                TQ += 1
            else:
                FQ += 1  
        else:
            if "statement"==df["Outcomes"][idx]:
                TS += 1
            else:
                FS += 1
    print(TQ/(TQ+FQ+TS+FS))
    print(FQ/(TQ+FQ+TS+FS))
    print(TS/(TQ+FQ+TS+FS))
    print(FS/(TQ+FQ+TS+FS))
    return TQ, FQ, TS, FS

def confusion_extract():
    fileName = "./habrok_data/run1/cross_guessesM"
    data = []
    for i in range(110):
        fileN = fileName + str(i) + ".csv"
        df = pd.read_csv(fileN)
        total = sum(df["TQ"])+sum(df["FQ"])+sum(df["TS"])+sum(df["FS"])
        TQ = sum(df["TQ"])/total
        FQ = sum(df["FQ"])/total
        TS = sum(df["TS"])/total
        FS = sum(df["FS"])/total
        data.append((TQ,FQ,TS,FS))
    return data

def more_stats(data,species,attributes):
    accuracy = np.array([(x[0]+x[2])/sum(x) for x in data]).reshape(len(species),len(attributes))
    precision = np.array([(x[0]+x[2])/sum(x) for x in data]).reshape(len(species),len(attributes))
    meanAcc = [sum(L)/len(L) for L in accuracy]
    print(meanAcc)
        


def comparison_bar(data,species1,attributes):
    species = np.array(species1)
    accuracy = np.array([(x[0]+x[2])/sum(x) for x in data]).reshape(len(species),len(attributes))

    y = np.arange(len(species))  # the label locations
    width = 0.07  # the width of the bars
    multiplier = 0

    Ngraphs = 3
    fig, ax = plt.subplots(Ngraphs,1,layout='constrained')
    oldBar = accuracy
    barData = []
    for i in range(len(oldBar[0])):
        barData.append(oldBar[::,i])
    for graph in range(Ngraphs):
        multiplier = 0
        x = np.arange(len(y[int(len(species)*(graph)/Ngraphs):int(len(species)*(graph+1)/Ngraphs)]))
        print(len(barData),len(attributes))
        for i in range(len(barData)):
            offset = width * multiplier
            print(int(len(barData[0])*(graph+1)/Ngraphs),(graph+1)/Ngraphs*len(barData[0]))
            print(barData[0])
            print(barData[i][int(len(barData[0])*(graph)/Ngraphs):int(len(barData[0])*(graph+1)/Ngraphs)])
            rects = ax[graph].bar(x + offset, \
                barData[i][int(len(barData[0])*(graph)/Ngraphs):int(len(barData[0])*(graph+1)/Ngraphs)], width, label=str(attributes[i]))
            ax[graph].bar_label(rects, padding=3)
            multiplier += 1

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax[graph].set_ylabel('Length (mm)')
        ax[graph].set_title('Penguin attributes by species')
        ax[graph].set_xticks(x + width, \
            species[int(len(species)*(graph)/Ngraphs):int(len(species)*(graph+1)/Ngraphs)])
        ax[graph].legend(loc='upper left', ncols=3)
        ax[graph].set_ylim(0, 1)

    plt.show()
    return

def next_path(path_pattern):
    """
    Finds the next free path in an sequentially named list of files

    e.g. path_pattern = 'file-%s.txt':
    file-1.txt
    file-2.txt

    Runs in log(n) time where n is the number of existing files in sequence
    
    credit: https://stackoverflow.com/questions/17984809/how-do-i-create-an-incrementing-filename-in-python
    James
    """
    i = 1

    # First do an exponential search
    while os.path.exists(path_pattern % i):
        i = i * 2

    # Result lies somewhere in the interval (i/2..i]
    # We call this interval (a..b] and narrow it down until a + 1 = b
    a, b = (i // 2, i)
    while a + 1 < b:
        c = (a + b) // 2 # interval midpoint
        a, b = (c, b) if os.path.exists(path_pattern % c) else (a, c)

    return path_pattern % b