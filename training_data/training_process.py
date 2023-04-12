import rpy2.robjects as robjects
import pandas as pd
import os
from sklearn.model_selection import train_test_split
import random

def training_validation_mix():
    df = pd.read_csv("./data/input_cues.csv")
    randomNumber = random.randint(1,10000)
    x_train, x_test, y_train, y_test = train_test_split(df["Cues"], df["Outcomes"], test_size=0.2,random_state=randomNumber)
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

def training_in_r():
    robjects.r.source("./training_data/edlscript.R", encoding="utf-8")
    return

