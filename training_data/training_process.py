import rpy2.robjects as robjects
import pandas as pd
import os
from sklearn.model_selection import train_test_split

def training_validation_mix():
    df = pd.read_csv("./data/input_cues.csv")
    x_train, x_test, y_train, y_test = train_test_split(df["Cues"], df["Outcomes"], test_size=0.2)
    df_train = pd.DataFrame({"Cues":x_train,"Outcomes":y_train})
    df_test = pd.DataFrame({"Cues":x_test,"Outcomes":y_test})
    
    fileName = "data/training_cues.csv"
    df_train.to_csv(os.path.abspath(os.path.join(fileName)),index=False)
    
    fileName = "data/validation_cues.csv"
    df_test.to_csv(os.path.abspath(os.path.join(fileName)),index=False)
    return

def set_hyper_parameters(eta,nruns,trainFile="../data/training_cues.csv",testFile="../data/validation_cues.csv",probabilityFile="../data/validation_guesses.csv"):
    df = pd.DataFrame({"eta":[eta],"nruns":[nruns],"train_data":[trainFile],"test_data":[testFile],"probability_data":[probabilityFile]})
    fileName = "data/hyper_parameters_R.csv"
    df.to_csv(os.path.abspath(os.path.join(fileName)),index=False)
    return

def training_in_r():
    robjects.r.source("./training_data/edlscript.R", encoding="utf-8")
    return

