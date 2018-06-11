# -*- coding: utf-8 -*-
time = []
api = []
pm2 = []
pm10 = []
SO2 = []
CO = []
NO2 = []
O3 = []

for line in open("data.txt",encoding='utf-8',errors='ignore'):
        row = line.split()
        print(row)
        time.append(str(row[0]))
        api.append(float(row[1]))
        pm2.append(float(row[4]))
        pm10.append(float(row[5]))
        SO2.append(float(row[6]))
        CO.append(float(row[7]))
        NO2.append(float(row[8]))
        O3.append(float(row[9]))


from numpy import array, cov, corrcoef

data = array([api,pm2])
print(corrcoef(data))
