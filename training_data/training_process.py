import rpy2.robjects as robjects
import pandas as pd
import os
from sklearn.model_selection import train_test_split
import random
import numpy as np
from imblearn.over_sampling import RandomOverSampler, SMOTE
from .analysis import *

def training_validation_mix(randomNumber,splitIt=True):
    df = pd.read_csv("./data/input_cues.csv")
    randomN = random.randint(1,10000)
    if splitIt:
        x_train, x_test, y_train, y_test = train_test_split(df["Cues"], df["Outcomes"], test_size=0.2,random_state=randomNumber)
    else:
        df2 = pd.read_csv("./data_train/input_cues.csv")
        x_train = df["Cues"]
        y_train = df["Outcomes"]
        x_test = df2["Cues"]
        y_test = df2["Outcomes"]
    # Randomly over sample the minority class
    ros = RandomOverSampler(random_state=42)
    
    x_train = np.array(x_train).reshape(-1,1)
    x_train, y_train= ros.fit_resample(x_train, y_train)
    x_train = x_train.flatten()
    
    ros = RandomOverSampler(random_state=0)
    
    x_test = np.array(x_test).reshape(-1,1)
    x_test, y_test= ros.fit_resample(x_test, y_test)
    x_test = x_test.flatten()
    
    
    df_train = pd.DataFrame({"Cues":x_train,"Outcomes":y_train})
    df_test = pd.DataFrame({"Cues":x_test,"Outcomes":y_test})
    
    fileName = "save_progress_training/training_cues.csv"
    df_train.to_csv(os.path.abspath(os.path.join(fileName)),index=False)
    
    fileName = "save_progress_training/validation_cues.csv"
    df_test.to_csv(os.path.abspath(os.path.join(fileName)),index=False)
    return randomNumber

def set_hyper_parameters(eta,nruns,boundary_gradient,randomSeed,fileName,length,flatLength,flatChange,\
    trainFile="../save_progress_training/training_cues.csv",testFile="../save_progress_training/validation_cues.csv",\
    probabilityFile="../save_progress_training/validation_guesses.csv",training_weights="../save_progresss_training/training_weights.csv"):
    df = pd.DataFrame({"eta":[eta],"nruns":[nruns],"boundary_gradient":[boundary_gradient],"start_length":[length[0]],"end_length":[length[1]],\
        "flat_length":[flatLength],"flat_change":[flatChange],"seed":[randomSeed],\
        "train_data":[trainFile],"test_data":[testFile],"probability_data":[probabilityFile],"training_weights":[training_weights]})

    df.to_csv(os.path.abspath(os.path.join(fileName)),index=False)
    fileName = "data/hyper_parameters_R.csv"
    df.to_csv(os.path.abspath(os.path.join(fileName)),index=False)
    return

def set_hyper_parameters_cross(eta,nruns,boundary_gradient,randomSeed,fileName,length=(0,0),\
    trainFile="../save_progress_training/training_cues.csv",testFile="../save_progress_training/validation_cues.csv",\
    probabilityFile="../save_progress_training/validation_guesses.csv"):
    
    df = pd.DataFrame({"eta":[eta],"nruns":[nruns],"boundary_gradient":[boundary_gradient],"seed":[randomSeed],"length_begin":length[0],"length_end":length[1],\
        "train_data":[trainFile],"test_data":[testFile],"probability_data":[probabilityFile]})

    df.to_csv(os.path.abspath(os.path.join(fileName)),index=False)
    return

def training_in_r(fileName="./training_data/edlscript.R"):
    robjects.r.source(fileName, encoding="utf-8")
    os.chdir("../")
    return

def testingStuff():
    df = pd.read_csv("./save_progress_training/training_cues.csv")
    print(len(df[df["Outcomes"]=="question"]))
    print(len(df[df["Outcomes"]=="statement"]))
    
def cross_validation(B,length,N_cross=20):
    nruns = 100
    eta = 0.01
    probabilityFile="save_progress_training/validation_guesses_cross.csv"
    probabilityFile = os.path.abspath(os.path.join(probabilityFile))

    hyper_file="data/hyper_parameters_R_cross.csv"
    hyper_file = os.path.abspath(os.path.join(hyper_file))
    randomSeedList = []
    accuracyList = []
    for idx in range(N_cross):
        randomSeed = training_validation_mix(idx)
        randomSeedList.append(randomSeed)
        set_hyper_parameters_cross(eta,nruns,B,randomSeed,hyper_file,probabilityFile=probabilityFile)
        training_in_r("./training_data/edlscript_cross_validation.R")
        TQ,FQ,TS,FS = stats("./save_progress_training/validation_guesses_cross.csv")
        accuracyList.append((TQ,FQ,TS,FS))
    hyper_file="save_progress_training/hyper_parameters_R_cross%s.csv"
    hyper_file = next_path(os.path.abspath(os.path.join(hyper_file)))
    set_hyper_parameters_cross(eta,nruns,B,"_".join([str(j) for j in randomSeedList]),hyper_file,length,probabilityFile=probabilityFile)

    df = pd.DataFrame({"TQ":[x[0] for x in accuracyList],"FQ":[x[1] for x in accuracyList],"TS":[x[2] for x in accuracyList],"FS":[x[3] for x in accuracyList]})
    fileName="save_progress_training/cross_guesses%s.csv"
    fileName = next_path(os.path.abspath(os.path.join(fileName)))
    df.to_csv(os.path.abspath(os.path.join(fileName)),index=False)
    print("training done")
    return