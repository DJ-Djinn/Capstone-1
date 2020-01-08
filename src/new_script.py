import pandas as pd
import os

def get_variety(filepath):
    number_viable_mons = []
    months = []
    for file in os.listdir(filepath):
        df = pd.read_csv(os.path.join(filepath, file))
        number_viable_mons.append(len(df))
        months.append(file)

if __name__ == '__main__':
    pass