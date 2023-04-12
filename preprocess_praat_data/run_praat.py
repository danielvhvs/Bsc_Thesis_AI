import subprocess
from .misc import *

def run_command(Dir,praatFile,outputFile,system="linux"):
    if system=="linux":
        subprocess.call(['/usr/bin/praat', '--run', praatFile, Dir, outputFile])
    elif system=="windows":
        subprocess.call(['C:\\Program Files\\Praat.exe', '--run', praatFile, Dir, outputFile])
    else:
        subprocess.call(['/Applications/Praat.app/Contents/MacOS/Praat', '--run', praatFile, Dir, outputFile])
    return

def delete_pitch_files():
    file_path = "./praat_files/pitch_data_statements.txt"
    if os.path.isfile(file_path) or os.path.islink(file_path):
        os.unlink(file_path)
    file_path = "./praat_files/pitch_data_questions.txt"
    if os.path.isfile(file_path) or os.path.islink(file_path):
        os.unlink(file_path)
    return

def run_all_praat(questionDir="../question_sentences_train/",statementDir="../statement_sentences_train/"):
    delete_pitch_files()
    run_command(statementDir,'./praat_files/extract_frequencies_script.praat',"pitch_data_statements.txt")
    run_command(questionDir,'./praat_files/extract_frequencies_script.praat',"pitch_data_questions.txt")
    return
