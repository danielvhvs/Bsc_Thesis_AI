import numpy as np
from determine_gradient import *

from sklearn.preprocessing import OrdinalEncoder
from misc import *

def gradient_case(number):
    if number == 1:
        return "step up"
    if number == -1:
        return "step down"
    else:
        return "flat"
    
def abstract_gradient(change):
    abstract = [gradient_case(change[0])]
    for i in range(1,len(change)):
        if (change[i] != change[i-1]):
            abstract.append(gradient_case(change[i]))
    return abstract

def change1(abstract):
    for i in range(len(abstract)):
        if i>0 and i<len(abstract)-1:
            if abstract[i]=="flat":
                if abstract[i-1]=="step up" and abstract[i+1]== "step down":
                    abstract[i]= "hill"
                elif abstract[i-1]=="step down" and abstract[i+1]== "step up":
                    abstract[i]= "troph"
    return abstract

def change2(abstract):
    newAbstract = []
    for i in range(1,len(abstract)):
        if abstract[i]=="flat":
            if abstract[i-1] == "step up":
                newAbstract.append("Higher")
            if abstract[i-1] == "step down":
                newAbstract.append("Lower")
    return newAbstract

def change3(abstract):
    newAbstract = []
    if abstract[0]=="flat":
        newAbstract.append("mid")
    for i in range(len(abstract)):
        if i>0 and i<len(abstract)-1:
            if abstract[i]=="flat":
                if abstract[i-1]=="step up" and abstract[i+1]== "step down":
                    newAbstract.append("hill")
                elif abstract[i-1]=="step down" and abstract[i+1]== "step up":
                    newAbstract.append("troph")
                else:
                    newAbstract.append("mid")
            if abstract[i]!="flat" and abstract[i+1]!="flat":
                if abstract[i] == "step up" and abstract[i]!=abstract[i+1]:
                    newAbstract.append("hill")
                if abstract[i] == "step down" and abstract[i]!=abstract[i+1]:
                    newAbstract.append("troph")
        if i == len(abstract)-1 and abstract[i]=="flat":
            newAbstract.append("mid")
    return newAbstract

def change4(abstract):
    newAbstract = []
    for i in range(len(abstract)):
        if abstract[i]=="step down":
            newAbstract.append("Lower")
        if abstract[i]=="step up":
            newAbstract.append("Higher")
    return newAbstract

def change_abstract(abstract,change=0):
    if change==0:
        return abstract
    if change==1:
        return change1(abstract)
    if change==2:
        return change2(abstract)
    if change==3:
        return change3(abstract)
    if change==4:
        return change4(abstract)
    
def padding_abstract(left,right,padL=6,padR=6):
    abstract = []
    # left side
    if len(left)>=padL:
        abstract += left[:padL]
    else:
        abstract += left
        abstract += ["zero" for i in range(padL-len(left))]
        
    # right side
    if len(right)>=padR:
        abstract += right[len(right)-padR:]
    else:
        abstract += ["zero" for i in range(padR-len(right))]
        abstract += right
    return abstract
    
def print_abstract(data,boundary):
    halfway = int(len(data)/2)
    time = np.arange(len(data))/len(data)
    doChange = 4
    change1,abChange1 = find_gradient(data[:halfway],time[:halfway],boundary)
    change2,abChange2 = find_gradient(data[halfway:len(data)],time[halfway:len(data)],boundary)
    abstract1 = change_abstract(abstract_gradient(change1),doChange)
    abstract2 = change_abstract(abstract_gradient(change2),doChange)
    print(abstract1)
    print(abstract2)
    abstract = padding_abstract(abstract1,abstract2)
    print(abstract)
    
def abstract_output(allData,boundary):
    halfway = int(len(allData[0])/2)
    time = np.arange(len(allData[0]))/len(allData[0])
    doChange = 2
    allAbstract = []
    for idx,data in enumerate(allData):
        change1,abChange1 = find_gradient(data[:halfway],time[:halfway],boundary)
        change2,abChange2 = find_gradient(data[halfway:len(data)],time[halfway:len(data)],boundary)
        abstract1 = change_abstract(abstract_gradient(change1),doChange)
        abstract2 = change_abstract(abstract_gradient(change2),doChange)
        abstract = padding_abstract(abstract1,abstract2)
        allAbstract.append(abstract)
    return allAbstract

# def cat_to_number(data):
#     numbers = []
#     for row in range(len(data)):
#         new = []
#         for col in range(len(data[0])):
#             new.append(data[row][col])
            

def generate_output(data,boundary):
    abstract = np.array(abstract_output(data,boundary))
    # print(abstract[0])
    abstract = abstract.reshape(-1,1)
    enc = OrdinalEncoder()
    enc.fit(abstract)
    newAbs = enc.transform(abstract)
    newAbs = newAbs.reshape(len(data),len(abstract)//len(data))
    # print(newAbs[0])
    
    return
    

if __name__ == "__main__":
    fileName = "data/pitch_data_questions_processed_pitch.txt"
    pitch = read_file2(os.path.abspath(os.path.join(os.pardir, fileName)))
    B = 2.5
    generate_output(pitch,B)