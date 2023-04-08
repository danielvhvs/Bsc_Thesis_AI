import transform_data as tfd
import preprocess_praat_data as ppd
import training_data as trd
import organise

def organise_files():
    return

def preprocess():
    return

def transform():
    B = 2.4
    tfd.generate_cue_file(B)
    return

def training():
    trd.training_validation_mix()
    trd.set_hyper_parameters(0.01,10)
    trd.training_in_r()
    return

if __name__ == "__main__":
    organise_files()
    preprocess()
    transform()
    training()
