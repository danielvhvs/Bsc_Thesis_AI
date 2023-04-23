import pandas as pd

def stats(fileName):
    df = pd.read_csv(fileName)

    TQ, FQ, TS, FS = (0,0,0,0)
    for idx in range(len(df)):
        if df["Question"][idx] >= df["Statement"][idx]:
            if "question"==df["Outcomes"][idx]:
                TQ += 1
            else:
                FQ += 1  
        else:
            if "statement"==df["Outcomes"][idx]:
                TS += 1
            else:
                FS += 1
    return TQ, FQ, TS, FS
        