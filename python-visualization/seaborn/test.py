import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pprint import pprint

df = pd.read_excel('./data_xlsx/data1.xlsx')

sns.set_style('darkgrid')
plt.rcParams['font.sans-serif'] = ['SimHei']

x = df['类别']
y = df['总金额']
plt.bar(x, y, color='slateblue', width=0.5)
plt.show()
# # pprint(df)
