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
    fileName = "./habrok_data/run2/cross_guessesM"
    data = []
    for i in range(176):
        fileN = fileName + str(i) + ".csv"
        df = pd.read_csv(fileN)
        total = sum(df["TQ"])+sum(df["FQ"])+sum(df["TS"])+sum(df["FS"])
        TQ = sum(df["TQ"])/total
        FQ = sum(df["FQ"])/total
        TS = sum(df["TS"])/total
        FS = sum(df["FS"])/total
        data.append((TQ,FQ,TS,FS))
    return data

def confusion_extract2():
    fileName = "./save_progress_training/cross_guesses1.csv"
    data = []
    df = pd.read_csv(fileName)
    print(len(df["TQ"]))
    for i in range(len(df["TQ"])):
        TQ = df["TQ"][i]
        FQ = df["FQ"][i]
        TS = df["TS"][i]
        FS = df["FS"][i]
        data.append((TQ,FQ,TS,FS))
    return data

def more_stats(data,species,attributes):
    accuracy = np.array([(x[0]+x[2])/sum(x) for x in data]).reshape(len(species),len(attributes))
    
    precisionQuestions = np.array([(x[0])/(x[0]+x[1]) for x in data]).reshape(len(species),len(attributes))
    precisionStatements = np.array([(x[2])/(x[2]+x[3]) for x in data]).reshape(len(species),len(attributes))
    
    recallQuestions = np.array([(x[0])/(x[0]+x[3]) for x in data]).reshape(len(species),len(attributes))
    recallStatements = np.array([(x[2])/(x[1]+x[2]) for x in data]).reshape(len(species),len(attributes))
    
    meanAcc = [sum(L)/len(L) for L in accuracy]
    meanRecallQ = [sum(L)/len(L) for L in precisionQuestions]
    meanRecallS = [sum(L)/len(L) for L in precisionStatements]
    meanPrecQ = [sum(L)/len(L) for L in recallQuestions]
    meanPrecS = [sum(L)/len(L) for L in recallStatements]
    print(meanAcc)
    print(meanRecallQ)
    print(meanRecallS)
    print(meanPrecQ)
    print(meanPrecS)
    return
        


def comparison_bar(data,species1,attributes):
    species = np.array(species1)
    accuracy = np.round(np.array([(x[0]+x[2])/sum(x) for x in data]),2)
    meanA = np.mean(accuracy)
    accuracy = accuracy.reshape(len(species),len(attributes))
    accuracy = accuracy[:-1]
    species = species[:-1]

    y = np.arange(len(species))  # the label locations
    width = 0.06  # the width of the bars
    multiplier = 0

    Ngraphs = 5
    newNgraphs = 5
    fig, ax = plt.subplots(newNgraphs,1)
    oldBar = accuracy
    barData = []
    graphName = ["(a)","(b)","(c)","(d)","(e)"]
    for i in range(len(oldBar[0])):
        barData.append(oldBar[::,i])
    for graph in range(newNgraphs):
        multiplier = 0
        x = np.arange(len(y[int(len(species)*(graph)/Ngraphs):int(len(species)*(graph+1)/Ngraphs)]))
        for i in range(len(barData)):
            offset = width * multiplier

            rects = ax[graph].bar(x + offset, \
                barData[i][int(len(barData[0])*(graph)/Ngraphs):int(len(barData[0])*(graph+1)/Ngraphs)], width, label=str(attributes[i]))
            ax[graph].bar_label(rects, padding=3)
            multiplier += 1

        # Add some text for labels, title and custom x-axis tick labels, etc.
        # ax[graph].axhline(meanA)
        ax[graph].set_ylabel('accuracy')
        ax[graph].set_title(graphName[graph])
        ax[graph].set_xticks(x + width, \
            species[int(len(species)*(graph)/Ngraphs):int(len(species)*(graph+1)/Ngraphs)])
        ax[graph].set_ylim(0, 1)
    ax[0].set_ylim(0,2.2)
    ax[0].legend(loc="upper left",ncol=8)
    #fig.tight_layout()
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