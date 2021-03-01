#!/usr/local/bin/python3

import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup

def main():
    driver = webdriver.Chrome("/Users/Marcello395/python_projects_fun/libs/chromedriver")
    symbol = []
    rank = []

    driver.get("https://www.quiverquant.com/sources/wallstreetbets")
    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')

    i = 0
    nameRank = ''
    wsbRedditList = []
    for a in soup.findAll('td'):
        if i % 2 == 0:
            wsbRedditList.append(nameRank)
            nameRank = ''
            i = 0
        nameRank += str(a) + ' '
        i += 1

    dictList = []
    for element in wsbRedditList:
        features = (element.split('/td>'))
        try:
            name = features[0]
            rank = features[1]
        except IndexError:
            continue
        cleanName = (name.split('>')[2].split('<')[0])
        cleanRank = (rank.split('>')[1].split('<')[0])

        dictList.append({'symbol' : cleanName, '24_hour_mentions' : cleanRank})

    wsbDf = pd.DataFrame(dictList)

    print(wsbDf.head(10))

if __name__ == '__main__':
    main()
