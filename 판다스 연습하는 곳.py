import pandas as pd
import matplotlib.pyplot as plt
import os
os.chdir('C:\\Users\\way2g\\OneDrive\\문서\\Web_Python\\Term_Project')
plt.rc('font', family='NanumGothic')
df = pd.read_csv('학교알리미_초등학교_2019년도_학교기본정보.csv', encoding='utf-8')
print(df.columns)
print(df.info)
region_group = df.groupby("시도교육청")
schools_in_region = region_group['학교명'].count()
print(schools_in_region)
schools_in_region.sort_values().plot(kind='barh', grid='True',figsize=(10,10))
plt.show()