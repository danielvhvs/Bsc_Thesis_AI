import transform_data as tfd
import preprocess_praat_data as ppd
import training_data as trd
import organise
import os
import time
import pandas as pd

def organise_files():
    # organise.rearange_all()
    organise.rearange_files("line_index_test.txt","./test_sentences/","test")
    print("organising files done")
    return

def preprocessing():
    # ppd.run_all_praat()
    ppd.preprocessing_data(dataFolder="data")
    print("preprocessing done")
    return

def transform(B,trueFlat,lengths=(2,2),flatLength=0,flatChange=0,data="data"):
    tfd.generate_cue_file(B,trueFlat,lengths=lengths,flatLength=flatLength,flatChange=flatChange,data=data)
    print("transforming done")
    return

def training(B,length,flatLength=0,flatChange=0):
    nruns = 100
    eta = 0.01
    # randomSeed = trd.training_validation_mix(42,False)
    randomSeed = 42
    probabilityFile="save_progress_training/validation_guesses%s.csv"
    probabilityFile = tfd.next_path(os.path.abspath(os.path.join(probabilityFile)))
    training_weights="save_progress_training/training_weights%s.csv"
    training_weights = tfd.next_path(os.path.abspath(os.path.join(training_weights)))
    hyper_file="save_progress_training/hyper_parameters_R%s.csv"
    hyper_file = tfd.next_path(os.path.abspath(os.path.join(hyper_file)))
    
    trainFile = "../cuesets/training_cues_flat1.csv"
    testFile = "../cuesets/validation_cues_flat1.csv"
    trd.set_hyper_parameters(eta,nruns,B,randomSeed,hyper_file,length,flatLength,flatChange,probabilityFile=probabilityFile,\
        training_weights=training_weights,trainFile=trainFile,testFile=testFile)
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
    L = (1,1)
    fL = 1
    fC = 0.16
    B = 2.8
    # # preprocessing()
    # transform(B,True,L,fL,fC,"data")
    # transform(B,True,L,fL,fC,"data_train")
    
    # randomSeed = trd.training_validation_mix(42,False)
    
    # training(B,L,fL,fC)
    
    
    # trd.cue_distribution3("./cuesets/training_cues_flat1.csv","./cuesets/training_weights_flat1.csv")
    # trd.more_stats1("./cuesets/validation_guesses_flat.csv")
    # trd.cue_pattern_stats("./cuesets/training_weights_flat.csv")
    
    # fileName = "data/pitch_data_statements_processed_pitch.txt"
    # pitch = tfd.read_file2(os.path.abspath(os.path.join(fileName)))
    
    # tfd.plot_flat(pitch,2.8,N=0)
    
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
    
    # species = [2.4,2.8,3.2,3.6,4,4.4,4.8,5.2]
    # attributes = [(4,4),(0,4),(4,0)]
    # data = trd.confusion_extract()
    # trd.comparison_bar(data,species,attributes)
    
    # different = [2.6,2.8,3,3.2] #run 13 and 14 - 0.2 and 0.8 seconds # run15 0.8 seconds (5,5) length
    # species = [1,2,3,4]
    # attributes = [0.24,0.26,0.28,0.3,0.32,0.34,0.36,0.38]
    # data = trd.confusion_extract()
    # trd.comparison_bar_3d(data,different,species,attributes)
    
    # different = [2.6,2.8,3,3.2] #run 18
    # species = [1,2,3,4]
    # attributes = [(4,4),(0,4),(4,0),(3,3),(2,2),(1,1),(0,3),(0,2)]
    # data = trd.confusion_extract()
    # trd.comparison_bar_3d(data,different,species,attributes)
    
    #run 20 - normal run but with normalising
    # species = [2,2.4,2.8,3.2,3.6,4,4.4,4.8,5.2]
    # attributes = [(4,4),(4,0),(0,4),(5,5),(3,3),(2,2),(1,1)]
    # data = trd.confusion_extract(63,"./habrok_data/run20/cross_guessesM")
    # trd.comparison_bar(data,species,attributes)
    
    # run 21 - flat old run but with normalising # run22 flat new with normalising # run23 flat old without normalising #run 25 flat new not normalised
    # species = [2,4,6,8,10,12]
    # attributes = [0.05,0.1,0.15,0.2,0.25,0.3]
    # different = [1.6,1.9,2.2,2.5,2.8,3.1]
    # data = trd.confusion_extract(216,"./habrok_data/run22/cross_guessesM")
    # trd.comparison_bar_3d(data,different,species,attributes)
    
    # run 24 - old flat - specific
    # different = [2.5,2.7,2.9,3.1]
    # species = [1,2,3,4]
    # attributes = [0.02,0.04,0.06,0.08,0.1,0.12,0.14,0.16]
    # data = trd.confusion_extract(128,"./habrok_data/run24/cross_guessesM")
    # trd.comparison_bar_3d(data,different,species,attributes)   
    
    # run 27 - new flat - specific
    # different = [2.2,2.4,2.6,2.8,3,3.2]
    # species = [1,2,3]
    # attributes = [0.08,0.1,0.12,0.14,0.16,0.18,0.2,0.22]
    # data = trd.confusion_extract(144,"./habrok_data/run27/cross_guessesM")
    # trd.comparison_bar_3d(data,different,species,attributes)    

    # transform(2.8,True,(4,4),2,0.3)
    # training(2.8,(4,4),2,0.3)
    
    #run 26 normal specific
    # species = [2.4,2.6,2.8,3,3.2,3.4,3.6,3.8,4,4.2,4.4,4.6,4.8]
    # attributes = [(4,4),(4,0),(0,4),(3,3),(2,2),(1,1)]
    # data = trd.confusion_extract(78,"./habrok_data/run26/cross_guessesM")
    # trd.comparison_bar(data,species,attributes)

    # species = [2.6,2.8]
    # attributes = [(4,4),(4,0),(0,4),(3,3),(2,2),(1,1)]
    # y = 1
    # x = range(len(attributes)*y,len(attributes)*(y+1))
    # for i in x:
    #     print(i)
    # print(x)
    # trd.single_bar(attributes,x,"./habrok_data/run28/cross_guessesM")
    
    
    # preprocessing()
    fileName = "data"+"/pitch_data_questions_processed_pitch.txt"
    pitch = tfd.read_file2(os.path.abspath(os.path.join(fileName)),True)
    tfd.plot_flat(pitch,2.4,1)
    # tfd.plot_smooth(pitch,2.4)
    # trd.weight_bar()
    
    # fileName = "data"+"/pitch_data_questions_processed_pitch.txt"
    # fileName2 = "data"+"/pitch_data_questions_pitch.txt"
    # fileName3 = "data"+"/pitch_data_questions_time.txt"
    # N = 1
    # pitch = tfd.read_file2(os.path.abspath(os.path.join(fileName)),True)[N]
    # pitch2 = tfd.read_file2(os.path.abspath(os.path.join(fileName2)),True)[N]
    # time2 = tfd.read_file2(os.path.abspath(os.path.join(fileName3)),True)[N]
    # tfd.test_single_plot(pitch,pitch2,time2)
    pass
