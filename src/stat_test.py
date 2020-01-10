import pandas as pd
import numpy as np
from scipy import stats
import os
from variety_plot import get_variety, sort_variety

def compute_ttest(singles_path, doubles_path, months):
    singles = sort_variety(singles_path, months)
    doubles = sort_variety(doubles_path, months)
    return stats.ttest_ind(singles, doubles, equal_var=False)

month_list = ['2016-11', '2016-12', '2017-01', '2017-02', '2017-03', '2017-04',\
              '2017-05', '2017-06', '2017-07', '2017-08', '2017-09', '2017-10',\
              '2017-11', '2017-12', '2018-01', '2018-02', '2018-03', '2018-04',\
              '2018-05', '2018-06', '2018-07', '2018-08', '2018-09', '2018-10',\
              '2018-11', '2018-12', '2019-01', '2019-02', '2019-03', '2019-04',\
              '2019-05', '2019-06', '2019-07', '2019-08', '2019-09', '2019-10']

if __name__ == '__main__':
    print(compute_ttest('data/cleaned_data/singles', 'data/cleaned_data/doubles', month_list))