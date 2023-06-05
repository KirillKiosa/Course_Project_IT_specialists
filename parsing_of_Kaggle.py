#pip install pandas openpyxl xlsxwriter xlrd
import pandas as pd
import openpyxl
import numpy as np
df = open("data1.csv")
allCities = list()
line = df.readline()
gender = []
city = []
country = []
position = []
seniority = []
wage_euro = []
wage_dollar = []
a = 0

for line in df:
    commas_indexes = list()
    i = 0
    while len(commas_indexes) < 8:
        if line[i] == ',':
            commas_indexes.append(i)
        i += 1

    locallist = list()
    locallist.append(line[commas_indexes[1]+1:commas_indexes[2]])
    locallist.append(line[commas_indexes[2]+1:commas_indexes[3]])
    locallist.append(line[commas_indexes[3]+1:commas_indexes[4]])
    locallist.append(line[commas_indexes[6]+1:commas_indexes[7]])

    #getting salary
    commas_indexes1 = list()
    i = len(line) - 1
    number = 0
    while len(commas_indexes1) <= 1:
        if line[i] == ',':
            number += 1
            if number == 12 or number == 13:
                commas_indexes1.append(i)
        i -= 1

    sal = line[commas_indexes1[1]+1:commas_indexes1[0]]
    if locallist[0] != '' and locallist[1] != '' and locallist[2] != '' and locallist[3] != '' and sal != '':
        gender.append(locallist[0])
        city.append(locallist[1])
        country.append('Germany')
        position.append(locallist[2])
        seniority.append(locallist[3])
        wage_euro.append(sal)
        wage_dollar.append(sal)

    '''
    if localList[0] != '' and localList[1] != '' and localList[2] != '' and localList[3] != '':
        for i in localList:
            print(i, end = ' ')
        print('\n')'''

dict = {"Gender": gender, "City": city, "Country": country, "Position": position, "Seniority": seniority, "Wage(EU)": wage_euro, "Wage(USD)": wage_dollar}
Bigtable = pd.DataFrame(dict)
Bigtable.to_excel('data.xlsx')
print(Bigtable)
df.close()