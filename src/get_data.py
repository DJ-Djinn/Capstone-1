import requests

def make_url(month, rating, beginning):
    if month == (i for i in beginning):
        singles_url = 'https://www.smogon.com/stats/' + month + '/gen7pokebankou-' + str(rating) + '.txt'
        doubles_url = 'https://www.smogon.com/stats/' + month + '/gen7pokebankdoublesou-' + str(rating) + '.txt'
        return (singles_url, doubles_url)
    else:
        singles_url = 'https://www.smogon.com/stats/' + month + '/gen7ou-' + str(rating) + '.txt'
        doubles_url = 'https://www.smogon.com/stats/' + month + '/gen7doublesou-' + str(rating) + '.txt'
        return (singles_url, doubles_url)

def get_data(url):
    response = requests.get(url)
    return response.text

def save_data(lst, rating, beginning=None):
    for month in lst:
        urls = make_url(month, rating, beginning)
        with open('singles_' + month + '.txt', 'w+') as singles_file:
            singles_file.write(get_data(urls[0]))
        with open('doubles_' + month + '.txt', 'w+') as doubles_file:
            doubles_file.write(get_data(urls[1]))

month_list = ['2016-11', '2016-12', '2017-01', '2017-02', '2017-03', '2017-04',\
              '2017-05', '2017-06', '2017-07', '2017-08', '2017-09', '2017-10',\
              '2017-11', '2017-12', '2018-01', '2018-02', '2018-03', '2018-04',\
              '2018-05', '2018-06', '2018-07', '2018-08', '2018-09', '2018-10',\
              '2018-11', '2018-12', '2019-01', '2019-02', '2019-03', '2019-04',\
              '2019-05', '2019-06', '2019-07', '2019-08', '2019-09', '2019-10']

beginning = ['2016-11', '2016-12', '2017-01']

if __name__ == '__main__':
    save_data(month_list, 1825)
    save_data(month_list, 1695)