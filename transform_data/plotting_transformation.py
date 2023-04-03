import numpy as np
from matplotlib import pyplot as plt
from .abstracting_gradient import *
from .determine_gradient import *

def test_single_plot(time,data,frame):
    halfway = int(len(data)/2)    
    fig,frame = plt.subplots(1,1)
    psize = 2
    # frame.scatter(time,data,s=psize)
    frame.plot(time[:halfway],data[:halfway])
    frame.plot(time[halfway:len(data)],data[halfway:len(data)])
    
    frame.set_xlabel("time (s)")
    frame.set_ylabel("normalized pitch (Hz)")
    
    plt.show()
    return

def plot_smooth(data,boundary):
    halfway = int(len(data)/2)
    time = np.arange(len(data))/len(data)
    
    smoothL = determine_smooth_gradient_change(data[:halfway],time[:halfway],boundary)
    smoothR = determine_smooth_gradient_change(data[halfway:len(data)],time[halfway:len(data)],boundary)
        
    fig,frame = plt.subplots(1,1)
    
    frame.plot(time[:halfway],smoothL)
    frame.plot(time[halfway:len(data)],smoothR)
        
    frame.set_xlabel("time (s)")
    frame.set_ylabel("normalized pitch (Hz)")
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