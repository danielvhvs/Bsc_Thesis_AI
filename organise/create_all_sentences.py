import os
import shutil

"""
move files to all sentences
"""
def move_files(fileName,dirName):
    source = "./"+dirName+"/"
    desination = "./all_sentences/"
    if not os.path.exists("./all_sentences"):
        os.makedirs("./all_sentences")

    sentences = []
    with open(fileName,"r") as file_read:
        for line in file_read:
            split = line.split("\t")
            sentences.append(split)
            
            src_path = source+split[0]+".wav"
            dst_path = desination+split[0]+".wav"
            shutil.copy(src_path,dst_path)
    file_read.close()
    
    print(len(sentences))
    with open("line_index_all_sentences.txt","a") as file_write:
        for q in sentences:
            file_write.write(q[0]+"\t"+q[1])
    file_write.close()