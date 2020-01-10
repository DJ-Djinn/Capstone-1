import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

def create_freq_dict(filepaths):
    freq_dict = {}
    loc = 0
    for path in filepaths:
        for file in os.listdir(path):
            df = pd.read_csv(os.path.join(path, file)).head(15)
            for pokemon in df['Pokemon']:
                if pokemon in freq_dict.keys():
                    freq_dict[pokemon][loc] += 1
                else:
                    freq_dict[pokemon] = [0, 0]
                    freq_dict[pokemon][loc] += 1
        loc += 1
    return freq_dict

def seperate_keys_values(filepaths):
    freq_dict = create_freq_dict(filepaths)
    keys = list(freq_dict.keys())
    singles = []
    doubles = []
    for value in list(freq_dict.values()):
        singles.append(value[0])
        doubles.append(value[1])
    return [keys, singles, doubles]

def make_bar(singles_path, doubles_path, save_path):
    keys, singles, doubles = seperate_keys_values([singles_path, doubles_path])
    N = len(keys)
    ind = np.arange(N)
    width = 0.4

    fig, ax = plt.subplots(figsize=(28,14))
    fig.suptitle('Frequency of Pokémon in Top 15 of Singles and Doubles', fontsize=16)
    ax.bar(ind-width, singles, width, color='darkviolet', label='Singles')
    ax.bar(ind, doubles, width, color='darkorange', label='Doubles')
    ax.set_xticks(ticks=range(N))
    ax.set_xticklabels(keys)
    ax.legend(loc='best')
    plt.xticks(rotation=90)
    fig.savefig(save_path, dpi=125)
    plt.close('all')

if __name__ == '__main__':
    make_bar('data/cleaned_data/singles', 'data/cleaned_data/doubles', 'img/frequency_top_15')