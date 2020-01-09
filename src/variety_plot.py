import pandas as pd
import matplotlib.pyplot as plt
import os

def get_variety(filepath):
    number_viable_mons = {}
    for file in os.listdir(filepath):
        df = pd.read_csv(os.path.join(filepath, file))
        number_viable_mons[file.strip('.csv')] = len(df)
    return number_viable_mons

def sort_variety(filepath, months):
    variety_dict = get_variety(filepath)
    variety_val = []
    for month in months:
        variety_val.append(variety_dict[month])
    return variety_val

def make_plot(singles_path, doubles_path, save_path, months):
    singles = sort_variety(singles_path, months)
    doubles = sort_variety(doubles_path, months)
    fig, (ax1, ax2) =  plt.subplots(ncols=2, sharey=True, figsize=(16,4))
    fig.suptitle('Number of Viable Pokémon Between Singles and Doubles', fontsize=16)
    ax1.scatter(months, singles)
    ax1.set_title('Singles')
    ax2.scatter(months, doubles)
    ax2.set_title('Doubles')
    for ax in fig.axes:
        ax.set_xlabel('Year-Month')
        ax.set_ylabel('# of Mons')
        plt.sca(ax)
        plt.xticks(rotation=70)
    fig.savefig(save_path, dpi=125)
    plt.close('all')

month_list = ['2016-11', '2016-12', '2017-01', '2017-02', '2017-03', '2017-04',\
              '2017-05', '2017-06', '2017-07', '2017-08', '2017-09', '2017-10',\
              '2017-11', '2017-12', '2018-01', '2018-02', '2018-03', '2018-04',\
              '2018-05', '2018-06', '2018-07', '2018-08', '2018-09', '2018-10',\
              '2018-11', '2018-12', '2019-01', '2019-02', '2019-03', '2019-04',\
              '2019-05', '2019-06', '2019-07', '2019-08', '2019-09', '2019-10']

if __name__ == '__main__':
    make_plot('data/cleaned_data/singles', 'data/cleaned_data/doubles', 'img/singles_v_doubles.png', month_list)