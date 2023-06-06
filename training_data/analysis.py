import pandas as pd
import os
import numpy as np
from matplotlib import pyplot as plt
import itertools

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

def confusion_extract(N=215,fileName = "./habrok_data/run20/cross_guessesM"):
    data = []
    for i in range(N):
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
    
    F1Q = 1/((1/precisionQuestions+1/recallQuestions)/2)
    F1S = 1/((1/precisionStatements+1/recallStatements)/2)
    
    meanAcc = [sum(L)/len(L) for L in accuracy]
    meanRecallQ = [sum(L)/len(L) for L in precisionQuestions]
    meanRecallS = [sum(L)/len(L) for L in precisionStatements]
    meanPrecQ = [sum(L)/len(L) for L in recallQuestions]
    meanPrecS = [sum(L)/len(L) for L in recallStatements]
    # print(meanAcc)
    # print(meanRecallQ)
    # print(meanRecallS)
    # print(meanPrecQ)
    # print(meanPrecS)
    
    return

def cue_distribution(fileName):
    df = pd.read_csv(fileName)
    question = 0
    statement = 0
    noQ = 0
    noS = 0
    for idx in range(len(df)):
        if df["Outcomes"][idx]=="question":
            if df["Cues"][idx]=="bg":
                question +=1
            else:
                noQ += 1
        else:
            if df["Cues"][idx]=="bg":
                statement +=1
            else:
                noS += 1
    print(question,noQ)
    print(statement,noS)
    return

def ending(n):  
    return n[1]

def sort2(list_of_tuples):  
    return sorted(list_of_tuples, key = ending)  

def cue_distribution2(fileName):
    df = pd.read_csv(fileName)
    cueSetQ = {}
    cueSetS = {}

    x = list(itertools.chain.from_iterable([list(itertools.product('HL',repeat=i)) for i in range(1,5)]))
    y = ["".join(i) for i in x]
    z = [i+"#" for i in y] + ["#"+i for i in y]+["bg"]
    for i in z:
        cueSetQ[i] = 0
        cueSetS[i] = 0
    for idx in range(len(df)):
        cues = df["Cues"][idx].split("_")
        # print(cues)
        for idx2 in range(len(cues)):
            if df["Outcomes"][idx]=="question":
                cueSetQ[cues[idx2]] += 1
            else:
                cueSetS[cues[idx2]] += 1
    listS = sort2([(k, v) for k, v in cueSetS.items()])[::-1]
    listQ = sort2([(k, v) for k, v in cueSetQ.items()])[::-1]

    df2 = pd.DataFrame({"cue S":[i[0] for i in listS],"count S":[i[1] for i in listS],"cue Q":[i[0] for i in listQ],"count Q":[i[1] for i in listQ]})
    print(df2)
    
    fileName = "./cuesets/distribution_training_flat.csv"
    df2.to_csv(os.path.abspath(os.path.join(fileName)),index=False)


def middle(n):  
    return n[1]

def sort(list_of_tuples):  
    return sorted(list_of_tuples, key = middle)  

def cue_pattern_stats(fileName):
    df = pd.read_csv(fileName)
    df = df.rename(columns={"Unnamed: 0":"cue"})
    questionCues = []
    statementCues = []
    for idx in range(len(df)):
        if df["question"][idx] > 0:
            questionCues.append((df["cue"][idx],round(df["question"][idx],3)))
        else:
            statementCues.append((df["cue"][idx],round(df["statement"][idx],3)))
    questionCues = sort(questionCues)[::-1]
    statementCues = sort(statementCues)[::-1]
    
    #print(df["Unnamed: 0"])
    for idx in range(len(questionCues)):
        print(f"{questionCues[idx][0]}\t{questionCues[idx][1]}")
    print("\n")
    for idx in range(len(statementCues)):
        print(f"{statementCues[idx][0]}\t{statementCues[idx][1]}")
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