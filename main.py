import pandas as pd
import numpy as np
import re
from matplotlib import pyplot as plt
import seaborn as sns
import datetime

sns.set()


def media_parse(raw):
    if raw is not np.nan:
        raw = re.sub('[":«»]', '', raw)
        raw = raw.lower()
        temp = []
        for i in re.split(r'[,\;]+', raw):
            i = re.sub(r'\(.+\)', '', i)
            if i != ' ' and not bool(re.match(r'^\d+|^\s+', i.strip())):
                temp.append(i.strip())
            else:
                continue
        return temp

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
df.columns = ['uid', 'name', 'surname', 'sex', 'country', 'city', 'bday', 'music', 'movies', 'games', 'relation']
df['sex'] = df['sex'].astype(dtype='Int64')

### MUSIC - AGE stats
df2 = df[['sex', 'music', 'bday']].dropna()
df2['bday'] = 2020 - df['bday'].apply(lambda x: bdays(x, type='year')).astype(dtype='Int64')
df2['music'] = df2['music'].apply(lambda x: media_parse(x))
df2 = df2.explode('music', ignore_index=True)
print(df2.shape)
groups = ['дима билан']
df2 = df2[df2['music'].isin(groups)]
print(df2.shape)
plt.figure(figsize=(14, 6))
sns.histplot(x=df2['bday'],
    hue=df2['sex'].map({1: 'female', 2: 'male'}),
    # multiple='dodge'
    )
plt.xticks(ticks=range(df2['bday'].min(), df2['bday'].max() + 1, 2), rotation=90)
plt.tight_layout()
plt.show()
df2['count'] = 1
df2 = df2.groupby(['music', 'sex'], as_index=False).agg({'count': lambda x: sum(x) / len(df2) * 100, 'bday': 'mean'})
df2.rename(mapper={'count': 'percent', 'bday': 'mean_age'}, axis=1, inplace=True)
print(df2)


### GAMES - AGE stats
# df2 = df[['sex', 'games']].dropna()
# df2['games'] = df2['games'].apply(lambda x: media_parse(x))
# df2 = df2.explode('games', ignore_index=True)
# print(df2.shape)
# print(df2['games'].value_counts().head(20))
# games = ['gta']
# df2 = df2[df2['games'].isin(games)]
# print(df2.shape)
# df2['count'] = 1
# df2 = df2.groupby(['games', 'sex'], as_index=False).agg({'count': lambda x: sum(x) / len(df2) * 100})
# print(df2)

# print('Groups: {}\nNumber of records: {}\n'.format(groups, df2.shape[0]))

# groups = ['дима билан']
# df2 = df2[df2['music'].isin(groups)]
# df2['sex'] = df2['sex'].map({2: 'male', 1: 'female'})
# df2['music'] = df2['music'] / df2['music'].sum() * 100

# print(df2)

### TOP MOVIES
# df['movies'] = df['movies'].apply(lambda x: media_parse(x))
# df2 = df['movies'].dropna()
# df2 = df2.explode()
# df2 = df2.value_counts().sample(40)
# df2 = df2.value_counts()

# print('Number of records: {}\n'.format(df2.shape[0]))

# print(df2.head(40))


# top20cities = df['city'].value_counts()[:20].index.tolist()
# print(top20cities)
# print(df2.head())
# print(df2.info())

# top20cities = df['city'].value_counts()[:20].index.tolist()
# print(top20cities)

### parsing the dates
# df['day'] = df['bday'].apply(lambda x: bdays(x)).astype(dtype='Int64')
# df['month'] = df['bday'].apply(lambda x: bdays(x, type='month')).astype(dtype='Int64')
# df['year'] = df['bday'].apply(lambda x: bdays(x, type='year')).astype(dtype='Int64')
# year = df[['year', 'sex']].dropna()
# year = year[year['year'] > 1960]
# print(year.shape)
# year['sex'] = year['sex'].apply(lambda x: 'male' if x == 2 else 'female')


# plt.figure(figsize=(15, 5))
# plt.xticks(rotation=90)
# sns.countplot(data=year, x='year', hue='sex')
# plt.xlabel('Birth year')
# plt.ylabel('Count')
# plt.title('Birth year distribution')
# plt.tight_layout()
# plt.savefig('age_distrib.png')
# plt.show()
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
# df2 = df[['city', 'music']]
# df2 = df2[df2['city'].isin(top20cities)]
# df2['music'] = df2['music'].apply(lambda x: media_parse(x))
# df2 = df2.explode('music', ignore_index=True)
# top40music = df2['music'].value_counts()[1:41].index.tolist()
# print(top40music)
# df2 = df2[df2['music'].isin(top40music)]
# df2['count'] = 1
# df2 = pd.pivot_table(df2, values='count', index='city', columns='music', aggfunc='sum', fill_value=0)
# df2 = df2.reindex(df2.sum().sort_values(ascending=False).index, axis=1)
# print(df2.head(40))

# plt.figure(figsize=(14, 6))
# sns.heatmap(df2, linewidths=0.5, linecolor='black', cbar_kws={'label': 'Сила музыки'})
# plt.tight_layout()
# plt.show()
# df2 = df[['city', 'music']]
# df2 = df2[df2['city'].isin(top20cities)]
# df2['music'] = df2['music'].apply(lambda x: media_parse(x))
# df2 = df2.explode('music', ignore_index=True)
# top40music = df2['music'].value_counts()[1:41].index.tolist()
# print(top40music)
# df2 = df2[df2['music'].isin(top40music)]
# df2['count'] = 1
# df2 = pd.pivot_table(df2, values='count', index='city', columns='music', aggfunc='sum', fill_value=0)
# df2 = df2.reindex(df2.sum().sort_values(ascending=False).index, axis=1)
# print(df2.head(40))

# plt.figure(figsize=(14, 6))
# sns.heatmap(df2, linewidths=0.5, linecolor='black', cbar_kws={'label': 'Сила музыки'})
# plt.tight_layout()
# plt.show()

# movies = df['movies'].apply(lambda x: media_parse(x))
# print(movies.dropna().explode().value_counts().tail(60))

# print(df.head(40))
# print(df.shape)