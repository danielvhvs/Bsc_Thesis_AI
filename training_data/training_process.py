import rpy2.robjects as robjects
import pandas as pd
import os
from sklearn.model_selection import train_test_split
import random
import numpy as np
from imblearn.over_sampling import RandomOverSampler, SMOTE

def training_validation_mix():
    df = pd.read_csv("./data/input_cues.csv")
    randomNumber = random.randint(1,10000)
    x_train, x_test, y_train, y_test = train_test_split(df["Cues"], df["Outcomes"], test_size=0.2,random_state=randomNumber)
    x_train = np.array(x_train).reshape(-1,1)
    # Randomly over sample the minority class
    ros = RandomOverSampler(random_state=42)
    x_train, y_train= ros.fit_resample(x_train, y_train)
    x_train = x_train.flatten()
    df_train = pd.DataFrame({"Cues":x_train,"Outcomes":y_train})
    df_test = pd.DataFrame({"Cues":x_test,"Outcomes":y_test})
    
    fileName = "save_progress_training/training_cues.csv"
    df_train.to_csv(os.path.abspath(os.path.join(fileName)),index=False)
    
    fileName = "save_progress_training/validation_cues.csv"
    df_test.to_csv(os.path.abspath(os.path.join(fileName)),index=False)
    return randomNumber

def set_hyper_parameters(eta,nruns,boundary_gradient,randomSeed,fileName,\
    trainFile="../save_progress_training/training_cues.csv",testFile="../save_progress_training/validation_cues.csv",\
    probabilityFile="../save_progress_training/validation_guesses.csv",training_weights="../save_progresss_training/training_weights.csv"):
    df = pd.DataFrame({"eta":[eta],"nruns":[nruns],"boundary_gradient":[boundary_gradient],"seed":[randomSeed],\
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