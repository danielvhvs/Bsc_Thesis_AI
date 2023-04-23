import numpy as np
import pandas as pd
import os
from .determine_gradient import *
from .abstracting_gradient import *
from .misc import *

def word_to_letter(abstract):
    newAbstract = []
    for idx,word in enumerate(abstract):
        if word[0] == "s":
            newAbstract.append(word[5])
        else:
          newAbstract.append(word[0])
    return newAbstract


def make_abstract(allData,boundary,doChange):
    halfway = int(len(allData[0])/2)
    time = np.arange(len(allData[0]))/len(allData[0])

    beginAbstract = []
    endAbstract = []
    for idx,data in enumerate(allData):
        change1,abChange1 = find_gradient(data[:halfway],time[:halfway],boundary)
        change2,abChange2 = find_gradient(data[halfway:len(data)],time[halfway:len(data)],boundary)
        abstract1 = word_to_letter(change_abstract(abstract_gradient(change1),doChange))
        abstract2 = word_to_letter(change_abstract(abstract_gradient(change2),doChange))
        beginAbstract.append(abstract1)
        endAbstract.append(abstract2)
    return beginAbstract,endAbstract

def make_cue_sets(allData,boundary,begLen,endLen,doChange):
    beginAb,endAb = make_abstract(allData,boundary,doChange)
    allCues = []
    for idx,data in enumerate(beginAb):
        i=1
        cueSet = []
        while i<=begLen and i<len(data):
            cue = "#"+"".join(data[:i])
            cueSet.append(cue)
            i+=1
        allCues.append(cueSet)
    bgCue = "bg"
    for idx,data in enumerate(endAb):
        i=0
        cueSet = []
        while i<endLen and i<len(data):
            cue = "".join(data[len(data)-i-1:len(data)])+"#"
            cueSet.append(cue)
            i+=1
        cueSet.append(bgCue)
        allCues[idx] += cueSet
             
    return allCues

def make_cue_frame(cueSets,question):
    newCues = []
    for idx,cues in enumerate(cueSets):
        cue = "_".join(cues)
        newCues.append(cue)
        
    df = pd.DataFrame({"Cues":newCues})
    df["Outcomes"] = [question for _ in range(len(cueSets))]
    return df

def generate_cue_file(B,lengths=2,doChange=2):
    if isinstance(lengths,int):
        endLen = lengths
        begLen = lengths
    else:
        endLen = lengths[1]
        begLen = lengths[0]
    fileName = "data/pitch_data_questions_processed_pitch.txt"
    pitch = read_file2(os.path.abspath(os.path.join(fileName)))
    dfq = make_cue_frame(make_cue_sets(pitch,B,begLen,endLen,doChange),"question")
    
    fileName = "data/pitch_data_statements_processed_pitch.txt"
    pitch = read_file2(os.path.abspath(os.path.join(fileName)))
    dfs = make_cue_frame(make_cue_sets(pitch,B,begLen,endLen,doChange),"statement")
    df = pd.concat([dfq,dfs])
    
    fileName = "data/input_cues.csv"
    df.to_csv(os.path.abspath(os.path.join(fileName)),index=False)
    return         