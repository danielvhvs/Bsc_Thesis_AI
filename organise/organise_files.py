import os
import shutil
from sklearn.model_selection import train_test_split

"""
rearange in question and statements for train data
"""
def rearange_files(fileName,dirName):
    if not os.path.exists("./statement_sentences_train"):
        os.makedirs("./statement_sentences_train")
    else:
        delete_dir_content("./statement_sentences_train")
    if not os.path.exists("./question_sentences_train"):
        os.makedirs("./question_sentences_train")
    else:
        delete_dir_content("./question_sentences_train")
    questions = []
    statements = []
    with open(fileName,"r") as file_read:
        for line in file_read:
            split = line.split("\t")
            if split[1][0]=="¿":
                questions.append(split)
                desination = "./question_sentences_train/"
            else:
                statements.append(split)
                desination = "./statement_sentences_train/"
            src_path = dirName+split[0]+".wav"
            dst_path = desination+split[0]+".wav"
            shutil.copy(src_path,dst_path)
    file_read.close()
    print(len(questions),len(statements))
    with open("line_index_questions_train.txt","w") as file_write_q:
        for q in questions:
            file_write_q.write(q[0]+"\t"+q[1])
    file_write_q.close()
    with open("line_index_statements_train.txt","w") as file_write_s:
        for s in statements:
            file_write_s.write(s[0]+"\t"+s[1])
    file_write_s.close()

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
    
def split_train_test():
    testDir = "./test_sentences/"
    trainDir = "./train_sentences/"
    source = "./all_sentences_filtered/"
    if not os.path.exists(testDir):
        os.makedirs(testDir)
    else:
        delete_dir_content(testDir)
    if not os.path.exists(trainDir):
        os.makedirs(trainDir)
    else:
        delete_dir_content(trainDir)
    
    codes = []
    sentences = []
    data = []
    with open("line_index_all_sentences_filtered.txt","r") as file_read:
        for line in file_read:
            split = line.split("\t")
            codes.append(split[0])
            sentences.append(split[1])
            data.append(line)
    file_read.close()
    x = range(len(data))
    x_train, x_test, y_train, y_test = train_test_split(x, data, test_size=0.2,random_state=42)

    with open("line_index_train.txt","w") as file_write:
        for line in y_train:
            file_write.write(line)
    file_write.close()
    
    with open("line_index_test.txt","w") as file_write:
        for line in y_test:
            file_write.write(line)
    file_write.close()

    with open("line_index_train.txt","r") as file_read:
        for line in file_read:
            split = line.split("\t")
            src_path = source+split[0]+".wav"
            dst_path = trainDir+split[0]+".wav"
            shutil.copy(src_path,dst_path)
    file_read.close()

    with open("line_index_test.txt","r") as file_read:
        for line in file_read:
            split = line.split("\t")
            src_path = source+split[0]+".wav"
            dst_path = testDir+split[0]+".wav"
            shutil.copy(src_path,dst_path)
    file_read.close()
    
def delete_bad_sentences(fileName,dirName):
    destination = "./all_sentences_filtered/"
    if not os.path.exists(destination):
        os.makedirs(destination)
    else:
        delete_dir_content(destination)
        
    sentences = []
    with open(fileName,"r") as file_read:
        for line in file_read:
            split = line.split("\t")
            if split[1][0]=="¿" or not ("?" in split[1]):
                sentences.append(split)
                src_path = dirName+split[0]+".wav"
                dst_path = destination+split[0]+".wav"
                shutil.copy(src_path,dst_path)
    file_read.close()

    with open("line_index_all_sentences_filtered.txt","w") as file_write:
        for s in sentences:
            file_write.write(s[0]+"\t"+s[1])
    file_write.close()

"""
making an smaller example folder for testing code
"""
def example_testing_folder(name,N=50):
    source = "./" + name + "_sentences_train/"
    destination = "./" + name + "_test/"
    fileName = "line_index_"+name+"s_train.txt"
    
    if not os.path.exists(destination):
        os.makedirs(destination)
    else:
        delete_dir_content(destination)
        
    sentences = []
    count = 0
    with open(fileName,"r") as file_read:
        for line in file_read:
            if count>=N:
                break
            else:
                count += 1
            split = line.split("\t")
            sentences.append(split)
            src_path = source+split[0]+".wav"
            dst_path = destination+split[0]+".wav"
            shutil.copy(src_path,dst_path)
    file_read.close()

    with open("line_index_"+name+"s_train_test.txt","w") as file_write:
        for s in sentences:
            file_write.write(s[0]+"\t"+s[1])
    file_write.close()

def rearange_all():
    delete_bad_sentences("line_index_all_sentences.txt","./all_sentences/")
    split_train_test()
    rearange_files("line_index_train.txt","./train_sentences/")
    return

def make_example_folder():
    example_testing_folder("question")
    example_testing_folder("statement")