import numpy as np
from matplotlib import pyplot as plt
from .abstracting_gradient import *
from .determine_gradient import *
from .abstracting_flat_areas import *

def test_single_plot(data,data2,time2):
    halfway = int(len(data)/2) 
    print(len(data),len(data2))
    time = np.arange(len(data))/len(data)
    fig = plt.figure()
    frame2 = fig.add_subplot(2,1,1)
    frame = fig.add_subplot(2,1,2)
    psize = 2
    # frame.scatter(time,data,s=psize)
    # frame.scatter(time[:halfway],data[:halfway],s=psize)
    # frame.scatter(time[halfway:len(data)],data[halfway:len(data)],s=psize)
    
    frame.plot(time[:halfway],data[:halfway],label="first 0.5 (s)")
    frame.plot(time[halfway:len(data)],data[halfway:len(data)],label="last 0.5 (s)")
    # frame.plot(time2,data2)
    frame.set_xlabel("time (s)")
    frame.set_ylabel("pitch (Hz)")
    frame.set_title("pitch after interpolation")
    frame.set_title("(b)")
    frame.legend()
    frame2.plot(time2[:50],data2[:50],label="first 0.5 (s)")
    frame2.plot(time2[49:len(time2)-50],data2[49:len(time2)-50],c="red")
    frame2.plot(time2[len(time2)-51:],data2[len(time2)-51:],label="last 0.5 (s)",c="orange")
    frame2.legend()
    frame2.set_xlabel("time (s)")
    frame2.set_ylabel("pitch (Hz)")
    frame2.set_title("pitch from praat")
    frame2.set_title("(a)")
    
    fig.tight_layout()
    plt.show()
    return

def plot_smooth(data,boundary):
    data = data[5]
    halfway = int(len(data)/2)
    time = np.arange(len(data))/len(data)
    
    smoothL = determine_smooth_gradient_data(data[:halfway],time[:halfway],boundary)
    smoothR = determine_smooth_gradient_data(data[halfway:len(data)],time[halfway:len(data)],boundary)
    
    fig = plt.figure()
    frame = fig.add_subplot(2,1,2)
    frame2 = fig.add_subplot(2,1,1)
    
    frame.plot(time[:halfway],smoothL,label="first 0.5 (s)")
    frame.plot(time[halfway:len(data)],smoothR,label="last 0.5 (s)")
        
    frame.set_xlabel("time (s)")
    frame.set_ylabel("normalized pitch (Hz)")
    frame.set_title("(b)")
    frame.legend()

    frame2.plot(time[:halfway],data[:halfway],label="first 0.5 (s)")
    frame2.plot(time[halfway:len(data)],data[halfway:len(data)],label="last 0.5 (s)")
    
    frame2.set_xlabel("time (s)")
    frame2.set_ylabel("normalized pitch (Hz)")
    frame2.set_title("(a)")
    frame2.legend()
    fig.tight_layout()
    plt.show()
    return

def plot_flat(allData,boundary,N=6):
    data = allData[N]
    
    parameters = {'xtick.labelsize': 12,'ytick.labelsize': 12}
    plt.rcParams.update(parameters)
    
    fig = plt.figure()
    # frame = fig.add_subplot(2,1,1)
    frame2 = fig.add_subplot(1,1,1)
    halfway = int(len(data)/2)
    time = np.arange(len(data))/len(data)
    flatL = determine_flat_areas(data[:halfway],time[:halfway],boundary)
    flatR = determine_flat_areas(data[halfway:len(data)],time[halfway:len(data)],boundary)
    newFlatL = flat_areas2(flatL,2,0.05)
    newFlatR = flat_areas2(flatR,2,0.05)
    size = 3
    # frame.scatter(range(len(flatL)),flatL,s=size,label="starting pattern")
    # frame.scatter(range(len(flatL),len(flatL)+len(flatR)),flatR,s=size,label="ending pattern")
    frame2.scatter(range(len(newFlatL)),newFlatL,s=size,label="starting pattern")
    frame2.scatter(range(len(newFlatL),len(newFlatL)+len(newFlatR)),newFlatR,s=size,label="ending pattern")
    fsize= 12
    # frame.set_xlabel("time (ms)",fontsize=fsize)
    # frame.set_ylabel("frequency (log Hz)",fontsize=fsize)
    # frame.set_title("flat areas")
    # frame.set_title("(a)")
    frame2.set_xlabel("time (ms)",fontsize=fsize)
    frame2.set_ylabel("frequency (log Hz)",fontsize=fsize)
    frame2.set_title("filtered flat areas")
    # frame2.set_title("")

    # frame.legend()
    frame2.legend()
    fig.tight_layout()
    plt.show()
    return

def reduction_gradient(data,boundary):
    halfway = int(len(data)/2)
    time = np.arange(len(data))/len(data)
    
    change1,abChange1 = find_gradient(data[:halfway],time[:halfway],boundary)
    change2,abChange2 = find_gradient(data[halfway:len(data)],time[halfway:len(data)],boundary)
        
    fig = plt.figure(figsize=(13,4))
    frame1 = fig.add_subplot(1,2,1)
    frame2 = fig.add_subplot(1,2,2)
    
    psize = 6
    c1 = "#1f77b4" #"#ff7f0e"
    c2 = c1#"#ff7f0e"
    frame1.scatter(time[:halfway],change1,s=psize,c=c1)
    frame1.scatter(time[halfway:len(data)],change2,s=psize,c=c2)
        
    frame1.set_xlabel("time (s)")
    frame1.set_ylabel("normalized pitch (Hz)")
    
    frame2.scatter(time[:halfway],abChange1,s=psize,c=c1)
    frame2.scatter(time[halfway:len(data)],abChange2,s=psize,c=c2)
        
    frame2.set_xlabel("time (s)")
    frame2.set_ylabel("normalized pitch (Hz)")
    plt.show()
    return

def compare_plot(allData,allBoundary,N,tp):
    halfway = int(len(allData[0])/2)
    time = np.arange(len(allData[0]))/len(allData[0])
    allData = allData[N]
    fig,frames = plt.subplots(len(allData),len(allBoundary),figsize=(7*len(allBoundary),4*len(allData)))
    
    parameters = {'xtick.labelsize': 14,'ytick.labelsize': 14}
    plt.rcParams.update(parameters)
    for row,data in enumerate(allData):
        for col,boundary in enumerate(allBoundary):
            smoothL = determine_smooth_gradient_change(data[:halfway],time[:halfway],boundary)
            smoothR = determine_smooth_gradient_change(data[halfway:len(data)],time[halfway:len(data)],boundary)
            frames[row][col].plot(time[:halfway],smoothL)
            frames[row][col].plot(time[halfway:len(data)],smoothR)
                
            frames[row][col].plot(time[:halfway],data[:halfway])
            frames[row][col].plot(time[halfway:len(data)],data[halfway:len(data)])
            
            fsize=16
            frames[row][col].set_xlabel("time (s)",fontsize=fsize)
            frames[row][col].set_ylabel("log2 pitch (Hz) "+str(N[row]),fontsize=fsize)
            frames[row][col].set_title(str(boundary)+tp,fontsize=fsize+3)
            
    fig.tight_layout()

    fileName = "save_progress_plots/testing%s.jpg"
    plt.savefig(next_path(os.path.abspath(os.path.join(fileName))))

    plt.show()
    return