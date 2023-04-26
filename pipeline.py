import transform_data as tfd
import preprocess_praat_data as ppd
import training_data as trd
import organise
import os
import time
import pandas as pd

def organise_files():
    organise.rearange_all()
    print("organising files done")
    return

def preprocessing():
    # ppd.run_all_praat()
    ppd.preprocessing_data()
    print("preprocessing done")
    return

def transform(B,lengths=(2,2)):
    tfd.generate_cue_file(B,lengths=lengths)
    print("transforming done")
    return

def training(B):
    nruns = 100
    eta = 0.01
    randomSeed = trd.training_validation_mix()
    probabilityFile="save_progress_training/validation_guesses%s.csv"
    probabilityFile = tfd.next_path(os.path.abspath(os.path.join(probabilityFile)))
    training_weights="save_progress_training/training_weights%s.csv"
    training_weights = tfd.next_path(os.path.abspath(os.path.join(training_weights)))
    hyper_file="save_progress_training/hyper_parameters_R%s.csv"
    hyper_file = tfd.next_path(os.path.abspath(os.path.join(hyper_file)))
    trd.set_hyper_parameters(eta,nruns,B,randomSeed,hyper_file,probabilityFile=probabilityFile,training_weights=training_weights)
    trd.training_in_r()
    print("training done")
    return

def multiple_runs():
    boundary = [2,2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,3]
    length = [(1,1),(2,2),(3,3),(1,2),(2,1),(2,3),(3,2),(4,4),(1,3),(3,1)]
    for B in boundary:
        for L in length:
            transform(B,L)
            trd.cross_validation(B,L,1)
            
if __name__ == "__main__":
    B = 2.4
    lengths = (1,1)
    # preprocessing()
    # transform(B,lengths)
    # training(B)
    # cross_validation(B)
    # multiple_runs()
    # data = trd.confusion_extract()
    # B = [2.1]
    # length = [(1,1),(2,2),(3,3),(1,2),(2,1),(2,3),(3,2),(4,4),(1,3),(3,1)]
    # trd.comparison_bar(data,[str(x) for x in B],[str(x) for x in length])
    trd.stats("./save_progress_training/validation_guesses1.csv")
    # fileName = "data/pitch_data_questions_processed_pitch.txt"
    # pitch = tfd.read_file2(os.path.abspath(os.path.join(fileName)))
    # tfd.plot_smooth(pitch[1],2.4)
    pass
