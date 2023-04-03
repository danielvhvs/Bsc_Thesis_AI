import os
import shutil

def delete_dir_content(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

def write_file(fileIN,data):
    with open("./data/"+fileIN,"w") as file:
        for line in data:
            for wordIdx,word in enumerate(line):
                file.write(word)
                if wordIdx != len(line)-1:
                    file.write(" ")
            file.write("\n")
    file.close()
    return
        
def read_file_double(fileIN,fileOUT):
    data = []
    time = []
    with open("./data/"+fileIN,"r") as file:
        for line in file:
            split = line.split()
            sound = []
            soundTime = []
            for idx in range(len(split)//2):
                soundTime.append(split[idx*2])
                sound.append(split[idx*2+1])
            data.append(sound)
            time.append(soundTime)
    file.close()
    write_file(fileOUT+"_time.txt",time)
    write_file(fileOUT+"_pitch.txt",data)
    return

def read_file(fileIN):
    data = []
    with open("./data/"+fileIN,"r") as file:
        for line in file:
            split = line.split()
            data.append(split)
    file.close()
    return data