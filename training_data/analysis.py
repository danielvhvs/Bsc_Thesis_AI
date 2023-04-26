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
    fileName = "./save_progress_training/cross_guesses"
    data = []
    for i in range(1,10):
        fileN = fileName + str(i) + ".csv"
        df = pd.read_csv(fileN)
        total = sum(df["TQ"])+sum(df["FQ"])+sum(df["TS"])+sum(df["FS"])
        TQ = sum(df["TQ"])/total
        FQ = sum(df["FQ"])/total
        TS = sum(df["TS"])/total
        FS = sum(df["FS"])/total
        data.append((TQ,FQ,TS,FS))
    return data

def comparison_bar(data,species,attributes):
    accuracy = [(x[0]+x[2])/sum(x) for x in data]
    

    x = np.arange(len(species))  # the label locations
    width = 0.25  # the width of the bars
    multiplier = 0

    fig, ax = plt.subplots(layout='constrained')
    barData = accuracy
    for i in range(len(barData)):
        offset = width * multiplier
        rects = ax.bar(x + offset, barData[i], width, label=str(attributes[i]))
        ax.bar_label(rects, padding=3)
        multiplier += 1

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Length (mm)')
    ax.set_title('Penguin attributes by species')
    ax.set_xticks(x + width, species)
    ax.legend(loc='upper left', ncols=3)
    ax.set_ylim(0, 1)

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