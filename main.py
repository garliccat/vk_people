import pandas as pd
import numpy as np
import re
from matplotlib import pyplot as plt
import seaborn as sns

sns.set()


def moviesmusic(raw):
    if raw is not np.nan:
        raw = raw.lower()
        raw = [i.strip(' "') for i in re.split(r'[,\;]+', raw)]
        return raw


def bdays(raw, type='day'):
    raw = str(raw)
    if raw == np.nan or raw == 'nan':
        return np.nan
    if type == 'day':
        return np.int64(raw.split('.')[0].strip())
    elif len(raw.split('.')) == 2 and type == 'month':
        return np.int64(raw.split('.')[1].strip())
    elif len(raw.split('.')) == 3 and type == 'month':
        return np.int64(raw.split('.')[1].strip())
    elif len(raw.split('.')) == 3 and type == 'year':
        return np.int64(raw.split('.')[2].strip())
    else:
        return np.nan

df = pd.read_csv('vk.csv', sep=';', header=None)
df.columns = ['uid', 'name', 'surname', 'sex', 'country', 'city', 'bday', 'music', 'movies']
df['sex'] = df['sex'].astype(dtype='Int64')

# df['music'] = df['music'].apply(lambda x: moviesmusic(x))
# df2 = df[['sex', 'music']].dropna()
# df2 = df2.explode('music', ignore_index=True)

# groups = ['дима билан']

# df2 = df2[df2['music'].isin(groups)]

# df2 = df2.groupby('sex', as_index=False).count()
# df2['sex'] = df2['sex'].map({2: 'male', 1: 'female'})
# df2['music'] = df2['music'] / df2['music'].sum() * 100

# print(df2.head())
# print(df2.info())

top20cities = df['city'].value_counts()[:20].index.tolist()
print(top20cities)

### parsing the dates
df['day'] = df['bday'].apply(lambda x: bdays(x)).astype(dtype='Int64')
df['month'] = df['bday'].apply(lambda x: bdays(x, type='month')).astype(dtype='Int64')
# df['year'] = df['bday'].apply(lambda x: bdays(x, type='year')).astype(dtype='Int64')

# print(df[(df['month'] == '4') & (df['day'] == '20')])
# print('Dates records: ', len(df['bday']) / len(df['bday'].dropna()))

### dates analysing (birthdays)
# df = df.dropna(subset=['day', 'month'])
# df = df[(df['day'] > 0) & (df['day'] < 32) & (df['month'] > 0) & (df['month'] < 13)]
# df = df[['uid', 'day', 'month']].groupby(['day', 'month'], as_index=False).count()
# df.sort_values(by=['month', 'day'], inplace=True)
# df['year'] = 2000
# df.index = pd.to_datetime(df[['year', 'month', 'day']], errors='coerce')
# plt.figure(figsize=(10, 5))
# sns.lineplot(x=df.index, y=df['uid'])
# plt.xticks(rotation=90)
# plt.tight_layout()
# plt.show()

### Top music in top cities
df2 = df[['city', 'music']]
df2 = df2[df2['city'].isin(top20cities)]
df2['music'] = df2['music'].apply(lambda x: moviesmusic(x))
df2 = df2.explode('music', ignore_index=True)
top40music = df2['music'].value_counts()[1:41].index.tolist()
print(top40music)
df2 = df2[df2['music'].isin(top40music)]
df2['count'] = 1
df2 = pd.pivot_table(df2, values='count', index='city', columns='music', aggfunc='sum', fill_value=0)
df2 = df2.reindex(df2.sum().sort_values(ascending=False).index, axis=1)
print(df2.head(40))

plt.figure(figsize=(14, 6))
sns.heatmap(df2, linewidths=0.5, linecolor='black', cbar_kws={'label': 'Сила музыки'})
plt.tight_layout()
plt.show()

# movies = df['movies'].apply(lambda x: moviesmusic(x))
# print(movies.dropna().explode().value_counts().tail(60))

# print(df.head(40))
# print(df.shape)