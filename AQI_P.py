import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
weather = 'data.xlsx'
data = pd.read_excel(weather,index_col=u'月份')

data['AQI'].plot()
plt.show()

data.corr()[3:].to_excel('result.xlsx')

shanghai = 'shanghai.xlsx'
data = pd.read_excel(shanghai,index_col=u'月份')


data.corr()[3:].to_excel('shanghai_res.xlsx')