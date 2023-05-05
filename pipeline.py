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

def transform(B,trueFlat,lengths=(2,2),flatLength=0,flatChange=0):
    tfd.generate_cue_file(B,trueFlat,lengths=lengths,flatLength=flatLength,flatChange=flatChange)
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
    # species = [2,4,6,8,10,12]
    # attributes = [0.05,0.1,0.15,0.2,0.25,0.3]#run7
    # different = [1.6,1.9,2.2,2.5,2.8,3.1]
    # data = trd.confusion_extract()
    # trd.comparison_bar_3d(data,different,species,attributes)

    # species = [6,8,10,12,14,16] #run 9
    # attributes = [0,0.02,0.04,0.05,0.06,0.08]
    # different = [2,2.4,2.8,3.2,3.6,4]

    # data = trd.confusion_extract()
    # trd.comparison_bar_3d(data,different,species,attributes)
        
    # different = [2,2.4,2.8,3.2,3.6,4] #run 12
    # species = [1,2,3,4]
    # attributes = [0.26,0.28,0.3,0.32,0.34,0.36]

    # data = trd.confusion_extract()
    # trd.comparison_bar_3d(data,different,species,attributes)
    
    # species = [2,2.5,3,3.5,4,4.5,5,5.5]
    # attributes = [(4,4)]
    # data = trd.confusion_extract()
    # trd.comparison_bar_1d(data,attributes,species)
    
    different = [2.6,2.8,3,3.2]
    species = [1,2,3,4]
    attributes = [0.24,0.26,0.28,0.3,0.32,0.34,0.36,0.38]
    data = trd.confusion_extract()
    trd.comparison_bar_3d(data,different,species,attributes)
    
    # transform(2.4,True,(4,4),1,0.26)
    # training(2.4)
    # preprocessing()

    pass
