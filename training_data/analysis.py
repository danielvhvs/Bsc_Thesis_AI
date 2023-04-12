import pandas as pd

def stats(fileName):
    df = pd.read_csv(fileName)
    guessed = []
    questions = 0
    statements = 0
    guessed_question = 0
    guessed_statement = 0
    for idx in range(len(df)):
        if df["Question"][idx] >= df["Statement"][idx]:
            guessed.append(int("question"==df["Outcomes"][idx]))
            guessed_question += 1
        else:
            guessed.append(int("statement"==df["Outcomes"][idx]))
            guessed_statement += 1
            
        if "statement"==df["Outcomes"][idx]:
            statements += 1
        else:
            questions += 1
    print(sum(guessed),sum(guessed)/len(guessed))
    print(statements,questions)
    print(guessed_statement,guessed_question)
    return
        