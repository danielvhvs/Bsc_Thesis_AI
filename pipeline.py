import transform_data as tfd
import preprocess_praat_data as ppd
import training_data as trd
import organise
import os

def organise_files():
    organise.rearange_all()
    print("organising files done")
    return

def preprocessing():
    # ppd.run_all_praat()
    ppd.preprocessing_data()
    print("preprocessing done")
    return

def transform(B):
    tfd.generate_cue_file(B)
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

if __name__ == "__main__":
    B = 2.4
    # preprocessing()
    # transform(B)
    # training(B)
    # trd.stats("./save_progress_training/validation_guesses2.csv")
    fileName = "data/pitch_data_questions_processed_pitch.txt"
    pitch = tfd.read_file2(os.path.abspath(os.path.join(fileName)))
    tfd.plot_smooth(pitch[1],2.4)
    
    pass
