import pandas as pd
import os

def cleaner():
    for file in os.listdir('../Text_Data'):
        df = pd.read_csv(os.path.join('../Text_Data/',file), header=3, sep='|')
        df = df.drop(index=[0, len(df)-1])
        df.to_csv(file.strip('.txt')+'.csv')

if __name__ == '__main__':
    cleaner()
