import pandas as pd
import os
import numpy as np
from matplotlib import pyplot as plt


def comparison_bar_3d(data,different_graphs,species,attributes):
    precisionQuestions = np.array([(x[0])/(x[0]+x[1]) for x in data])
    precisionStatements = np.array([(x[2])/(x[2]+x[3]) for x in data])
    
    recallQuestions = np.array([(x[0])/(x[0]+x[3]) for x in data])
    recallStatements = np.array([(x[2])/(x[1]+x[2]) for x in data])
    
    F1Q = 1/((1/precisionQuestions+1/recallQuestions)/2)
    F1S = 1/((1/precisionStatements+1/recallStatements)/2)

    precisionQuestions = np.round(precisionQuestions,2)
    precisionStatements = np.round(precisionStatements,2)
    
    recallQuestions = np.round(recallQuestions,2)
    recallStatements = np.round(recallStatements,2)
    
    F1Q = np.round(F1Q,2)
    F1S = np.round(F1S,2)

    accuracy = np.round(np.array([(x[0]+x[2])/sum(x) for x in data]),2)

    thing = accuracy
    allData = thing.reshape(len(different_graphs),len(species),len(attributes))

    fig, ax = plt.subplots(len(allData),1,figsize=(20,20))

    for totalGraph in range(len(allData)):
        newThing = allData[totalGraph]

        width = 0.1  # the width of the bars
        multiplier = 0

        oldBar = newThing
        barData = []
        graphName = ["(a)","(b)","(c)","(d)","(e)","(f)","(g)","(h)"]
        graphName = [str(x) for x in different_graphs]
        for i in range(len(oldBar[0])):
            barData.append(oldBar[::,i])

        multiplier = 0
        x = np.arange(len(species))
        for i in range(len(barData)):
            offset = width * multiplier

            rects = ax[totalGraph].bar(x + offset, barData[i], width, label=str(attributes[i]))
            ax[totalGraph].bar_label(rects, padding=3)
            multiplier += 1

        # Add some text for labels, title and custom x-axis tick labels, etc.
        # ax[graph].axhline(meanA)
        ax[totalGraph].set_ylabel('accuracy')
        ax[totalGraph].set_title(graphName[totalGraph])
        ax[totalGraph].set_xticks(x + width,species)
        ax[totalGraph].set_ylim(0, 1)
    ax[0].set_ylim(0,1.1)
    ax[0].legend(loc="upper left",ncol=8)
    fig.tight_layout()
    plt.show()
    return

def comparison_bar(data,species1,attributes):
    species = np.array(species1)
    accuracy = np.round(np.array([(x[0]+x[2])/sum(x) for x in data]),2)

    precisionQuestions = np.array([(x[0])/(x[0]+x[1]) for x in data])
    precisionStatements = np.array([(x[2])/(x[2]+x[3]) for x in data])
    
    recallQuestions = np.array([(x[0])/(x[0]+x[3]) for x in data])
    recallStatements = np.array([(x[2])/(x[1]+x[2]) for x in data])
    
    F1Q = 1/((1/precisionQuestions+1/recallQuestions)/2)
    F1S = 1/((1/precisionStatements+1/recallStatements)/2)

    precisionQuestions = np.round(precisionQuestions,2)
    precisionStatements = np.round(precisionStatements,2)
    
    recallQuestions = np.round(recallQuestions,2)
    recallStatements = np.round(recallStatements,2)
    
    F1Q = np.round(F1Q,2)
    F1S = np.round(F1S,2)
    
    thing = accuracy
    thing = thing.reshape(len(species),len(attributes))

    y = np.arange(len(species))  # the label locations
    width = 0.08  # the width of the bars
    multiplier = 0

    Ngraphs = 3
    newNgraphs = Ngraphs
    fig, ax = plt.subplots(newNgraphs,1)
    oldBar = thing
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
    ax[0].set_ylim(0,1.1)
    ax[0].legend(loc="upper left",ncol=5)
    fig.tight_layout()
    plt.show()
    return

def comparison_bar_2d(data,different_graphs,species,attributes):
    precisionQuestions = np.array([(x[0])/(x[0]+x[1]) for x in data])
    precisionStatements = np.array([(x[2])/(x[2]+x[3]) for x in data])
    
    recallQuestions = np.array([(x[0])/(x[0]+x[3]) for x in data])
    recallStatements = np.array([(x[2])/(x[1]+x[2]) for x in data])
    
    F1Q = 1/((1/precisionQuestions+1/recallQuestions)/2)
    F1S = 1/((1/precisionStatements+1/recallStatements)/2)

    precisionQuestions = np.round(precisionQuestions,2)
    precisionStatements = np.round(precisionStatements,2)
    
    recallQuestions = np.round(recallQuestions,2)
    recallStatements = np.round(recallStatements,2)
    
    F1Q = np.round(F1Q,2)
    F1S = np.round(F1S,2)

    accuracy = np.round(np.array([(x[0]+x[2])/sum(x) for x in data]),2)

    thing = accuracy
    allData = thing.reshape(len(different_graphs),len(species),len(attributes))

    thing = allData[5]
    thing = thing.reshape(len(species),len(attributes))

    y = np.arange(len(species))  # the label locations
    width = 0.08  # the width of the bars
    multiplier = 0

    Ngraphs = 3
    newNgraphs = Ngraphs
    fig, ax = plt.subplots(newNgraphs,1)
    oldBar = thing
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
    ax[0].set_ylim(0,1.1)
    ax[0].legend(loc="upper left",ncol=6)
    fig.tight_layout()
    plt.show()
    return

def single_bar(species,N=range(10),fileName="./habrok_data/run26/cross_guessesM"):
    data = []
    for i in N:
        fileN = fileName + str(i) + ".csv"
        df = pd.read_csv(fileN)
        total = sum(df["TQ"])+sum(df["FQ"])+sum(df["TS"])+sum(df["FS"])
        TQ = sum(df["TQ"])/total
        FQ = sum(df["FQ"])/total
        TS = sum(df["TS"])/total
        FS = sum(df["FS"])/total
        data.append((TQ,FQ,TS,FS))

    accuracy = np.round(np.array([(x[0]+x[2])/sum(x) for x in data]),2)
    fig = plt.figure()
    frame = fig.add_subplot(1,1,1)
    width = 0.8
    thing  = accuracy
    x = range(len(thing))
    rects = frame.bar(x,thing,width)
    frame.bar_label(rects,padding=3)
    frame.set_xticks(x,species)
    frame.set_ylim(0,1)
    
    frame.set_ylabel("accuracy")
    frame.set_xlabel("start and end length")
    plt.show()
    return

def middle(n):  
    return n[0]

def sort(list_of_tuples):  
    return sorted(list_of_tuples, key = middle)  

def weight_bar(fileName="./cuesets/training_weights_flat1.csv"):
    df = pd.read_csv(fileName)
    statements = [(df["statement"][idx],df.iloc[:,0][idx]) for idx in range(len(df))]
    questions = [(df["question"][idx],df.iloc[:,0][idx]) for idx in range(len(df))]
    statements = sort(statements)[:-1]
    questions = sort(questions)[:-1]
    print(statements)
    print(questions)
    fig = plt.figure()
    frame = fig.add_subplot(1,1,1)
    frame.bar([x[1] for x in statements], [x[0] for x in statements],width = 0.4,label="statement")
    frame.bar([x[1] for x in questions], [x[0] for x in questions],width = 0.4,label="question")
    
    frame.axhline(0,linewidth=0.6, color='black')
    frame.legend()
    plt.show()
    return

def comparison_bar_1d(data,species,attributes):
    accuracy = np.round(np.array([(x[0]+x[2])/sum(x) for x in data]),2)

    precisionQuestions = np.array([(x[0])/(x[0]+x[1]) for x in data])
    precisionStatements = np.array([(x[2])/(x[2]+x[3]) for x in data])
    
    recallQuestions = np.array([(x[0])/(x[0]+x[3]) for x in data])
    recallStatements = np.array([(x[2])/(x[1]+x[2]) for x in data])
    
    F1Q = 1/((1/precisionQuestions+1/recallQuestions)/2)
    F1S = 1/((1/precisionStatements+1/recallStatements)/2)

    precisionQuestions = np.round(precisionQuestions,2)
    precisionStatements = np.round(precisionStatements,2)
    
    recallQuestions = np.round(recallQuestions,2)
    recallStatements = np.round(recallStatements,2)
    
    F1Q = np.round(F1Q,2)
    F1S = np.round(F1S,2)
    
    thing = accuracy
    thing = thing.reshape(len(species),len(attributes))

    y = np.arange(len(species))  # the label locations
    width = 0.08  # the width of the bars
    multiplier = 0


    fig, ax = plt.subplots(1,1)
    oldBar = thing
    barData = []
    graphName = ["(a)","(b)","(c)","(d)","(e)"]
    for i in range(len(oldBar[0])):
        barData.append(oldBar[::,i])
    
    for i in range(len(barData)):
        offset = width * multiplier

        rects = ax.bar(0 + offset,barData[i], width, label=str(attributes[i]))
        ax.bar_label(rects, padding=3)
        multiplier += 1

    # Add some text for labels, title and custom x-axis tick labels, etc.
    # ax[graph].axhline(meanA)
    ax.set_ylabel('accuracy')
    ax.set_title(graphName[0])
    ax.set_ylim(0,1.1)
    ax.legend(loc="upper left",ncol=8)
    fig.tight_layout()
    plt.show()
    return