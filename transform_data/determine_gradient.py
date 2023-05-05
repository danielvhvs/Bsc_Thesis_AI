import numpy as np

def determine_smooth_gradient_data(data,time,boundary):
    slope = np.gradient(data,time)
    smooth = [data[0]]
    for idx,dx in enumerate(slope[:len(slope)-1]):
        if np.abs(dx) >= boundary:
            smooth.append(data[idx+1])
            x=1
        else:
            smooth.append(smooth[idx])
    return smooth

def determine_flat_areas(data,time,boundary):
    slope = np.gradient(data,time)
    smooth = [data[0]]
    for idx,dx in enumerate(slope[:len(slope)-1]):
        if np.abs(dx) >= boundary:
            smooth.append(data[idx+1])
        else:
            smooth.append(smooth[idx])
    newSmooth = []
    for idx,x in enumerate(smooth[1:]):
        if (smooth[idx-1]==smooth[idx]):
            newSmooth.append(smooth[idx])
    return newSmooth

def determine_smooth_gradient_change(data,time,boundary):
    slope = np.gradient(data,time)
    smooth = [data[0]]
    for idx,dx in enumerate(slope[:len(slope)-1]):
        if np.abs(dx) >= boundary:
            smooth.append(smooth[idx]+0.01*dx)
        else:
            smooth.append(smooth[idx])
    return smooth

def find_gradient(data,time,boundary):
    slope = np.gradient(data,time)
    changes = np.zeros(len(data))
    abChange = np.zeros(len(data))
    
    for idx,dx in enumerate(slope):
        if dx >= boundary:
            changes[idx] += 1
            abChange[idx] += 1
        elif dx <= -1*boundary:
            changes[idx] -= 1
            abChange[idx] += 1
    return changes,abChange