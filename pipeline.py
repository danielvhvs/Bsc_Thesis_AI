import transform_data as tfd
import preprocess_praat_data as ppd
import training_data as trd
import organise

def organise_files():
    organise.rearange_all()
    print("organising files done")
    return

def preprocessing():
    ppd.run_all()
    ppd.preprocessing_data()
    print("preprocessing done")
    return

def transform():
    B = 2.4
    tfd.generate_cue_file(B)
    print("transforming done")
    return

def training():
    nruns = 10
    eta = 0.01
    trd.training_validation_mix()
    trd.set_hyper_parameters(eta,nruns)
    trd.training_in_r()
    print("training done")
    return

if __name__ == "__main__":
    preprocessing()
    transform()
    training()
    pass
