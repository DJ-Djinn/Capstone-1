import pandas as pd
import os

def cleaner(filepath):
    for file in os.listdir(filepath):
        df = pd.read_csv(os.path.join(filepath,file), header=3, sep='|')
        df = df.drop(index=[0, len(df)-1])
        df = df[df.columns[[1,2,3]]]
        df = df.rename(columns={df.columns[0]:'Rank', df.columns[1]:'Pokemon', df.columns[2]:'Weighted Usage %'})
        df['Pokemon'] = df['Pokemon'].apply(lambda x: x.strip())
        df['Rank'] = df['Rank'].astype(int)
        df['Weighted Usage %'] = df['Weighted Usage %'].apply(lambda x: x.replace('%', '')).astype(float)
        df = df[df['Weighted Usage %'] >= 1]
        df.to_csv(file.strip('.txt')+'.csv', index=False)

if __name__ == '__main__':
    # cleaner('../../raw_data/singles')
    cleaner('../../raw_data/doubles')