import numpy as np
from scipy.interpolate import interp1d
from .misc import *

def filter_start_end(fileIN):
    newLine = []
    soundTime = []
    with open("./praat_files/"+fileIN, 'r') as file:
        # Read in the entire file as a string
        for line in file:
            split = line.split()
            start = 0
            end = 0
            for idx in range(len(split)//2):
                if split[idx*2+1] != "--undefined--":
                    start = idx
                    break
            for idx in range((len(split)//2)-1,-1,-1):
                if split[idx*2+1] != "--undefined--":
                    end = idx
                    break
            soundTime.append((start,end))
            newLine.append(split[start*2:(((end+1)*2)+1)])
    file.close()
    # fileIN = "pitch_data_questions_modified2.txt"
    write_file(fileIN,newLine)
    return soundTime

def take_range(fileIN,fileOUT,beginLength,endLength,intervalTime = 0.01):
    data = read_file(fileIN+".txt")
    begin = int(beginLength/intervalTime)
    end = int(endLength/intervalTime)
    newData = []
    for idx in range(len(data)):
        endIdx = len(data[idx])-end
        newSentenceData = data[idx][:begin]+data[idx][endIdx:len(data[idx])]
        newData.append(newSentenceData)
    write_file(fileOUT+".txt",newData)
    return
    
def interpolate_silence(fileIN,fileOUT,intervalTime = 0.01):
    data = read_file(fileIN+"_pitch.txt")
    time = read_file(fileIN+"_time.txt")
    allStat = []
    for idx,sentence in enumerate(data):
        inter = []
        dataInter = []
        timeInter = []
        stat = []
        for idx2,freq in enumerate(sentence):
            if freq=="--undefined--":
                inter.append((float(time[idx][idx2]),idx2))
                stat.append(idx2)
            else:
                dataInter.append(float(freq))
                timeInter.append(float(time[idx][idx2]))
        cs = interp1d(timeInter,dataInter)
        if stat!=[]:
            allStat.append((min(stat),max(stat)))
        for idx2 in range(len(inter)):
            data[idx][inter[idx2][1]] = str(int(cs(inter[idx2][0])))        
    write_file(fileOUT+"_pitch.txt",data)
    return [float(x[0]) for x in allStat],[float(x[1]) for x in allStat]

def transformer(data,startPitch):
    return np.log2(data)-np.log2(startPitch)

def transformer2(f2,f1):
    return 12*np.log2(f2/f1)
    
def normalize_pitch(fileIN,fileOUT):
    data = read_file(fileIN+"_pitch.txt")
    
    for idx, sentence in enumerate(data):
        startPitch = float(sentence[0])
        for wordIdx in range(len(sentence)):
            data[idx][wordIdx] = str(transformer(float(data[idx][wordIdx]),startPitch))
    write_file(fileOUT+"_pitch.txt",data)
    return

def normalize_pitch2(fileIN,fileOUT):
    data = read_file(fileIN+"_pitch.txt")
    newData = []
    for idx, sentence in enumerate(data):
        startPitch = float(sentence[0])
        newSentence = []
        for wordIdx in range(1,len(sentence)):
            newSentence.append(str(transformer2(float(data[idx][wordIdx]),float(data[idx][wordIdx-1]))))
        newData.append(newSentence)
    write_file(fileOUT+"_semitones.txt",newData)
    return

def stats_time(soundTime):
    diff = [x[1]-x[0] for x in soundTime]
    print(min(diff),max(diff),np.mean(diff))
    return

def stats_time2(soundTime):
    print(min(soundTime),max(soundTime),np.mean(soundTime))
    return

def all_preprocessing_steps(fileIN):
    soundTime = filter_start_end(fileIN+".txt")
    
    stats_time(soundTime)
    
    read_file_double(fileIN+".txt",fileIN)
    minS,maxS = interpolate_silence(fileIN,fileIN+"_interp")
    
    stats_time2(minS)
    stats_time2(maxS)
    
    normalize_pitch(fileIN+"_interp",fileIN+"_normalized")
    normalize_pitch2(fileIN+"_interp",fileIN+"_normalized")
    take_range(fileIN+"_normalized_pitch",fileIN+"_processed_pitch",0.5,0.5,0.01)
    take_range(fileIN+"_normalized_semitones",fileIN+"_processed_semitones",0.5,0.5,0.01)
    take_range(fileIN+"_time",fileIN+"_processed_time",0.5,0.5,0.01)

def preprocessing_data():
    fileName = "data"
    delete_dir_content(os.path.abspath(os.path.join(fileName)))
    fileName = "pitch_data_statements"
    all_preprocessing_steps(fileName)
    print("statements done")
    fileName = "pitch_data_questions"
    all_preprocessing_steps(fileName)
