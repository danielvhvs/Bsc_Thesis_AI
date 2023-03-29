from determine_gradient import *
import numpy as np
from matplotlib import pyplot as plt

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