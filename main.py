import pandas as pd
import numpy as np
import re
from matplotlib import pyplot as plt
import seaborn as sns
<<<<<<< HEAD
import datetime
=======
>>>>>>> 5681914cf8e6f2efd40c5430ce4fbbb6c46a3379

sns.set()


def moviesmusic(raw):
    if raw is not np.nan:
<<<<<<< HEAD
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
=======
        raw = raw.lower()
        raw = [i.strip(' "') for i in re.split(r'[,\;]+', raw)]
        return raw
>>>>>>> 5681914cf8e6f2efd40c5430ce4fbbb6c46a3379


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

<<<<<<< HEAD

=======
>>>>>>> 5681914cf8e6f2efd40c5430ce4fbbb6c46a3379
df = pd.read_csv('vk.csv', sep=';', header=None)
df.columns = ['uid', 'name', 'surname', 'sex', 'country', 'city', 'bday', 'music', 'movies']
df['sex'] = df['sex'].astype(dtype='Int64')

<<<<<<< HEAD
### MUSIC - AGE stats
=======
>>>>>>> 5681914cf8e6f2efd40c5430ce4fbbb6c46a3379
# df['music'] = df['music'].apply(lambda x: moviesmusic(x))
# df2 = df[['sex', 'music']].dropna()
# df2 = df2.explode('music', ignore_index=True)

<<<<<<< HEAD
# groups = ['pink floyd']

# df2 = df2[df2['music'].isin(groups)]
# print('Groups: {}\nNumber of records: {}\n'.format(groups, df2.shape[0]))
=======
# groups = ['дима билан']

# df2 = df2[df2['music'].isin(groups)]
>>>>>>> 5681914cf8e6f2efd40c5430ce4fbbb6c46a3379

# df2 = df2.groupby('sex', as_index=False).count()
# df2['sex'] = df2['sex'].map({2: 'male', 1: 'female'})
# df2['music'] = df2['music'] / df2['music'].sum() * 100

<<<<<<< HEAD
# print(df2)

### TOP MOVIES
df['movies'] = df['movies'].apply(lambda x: moviesmusic(x))
df2 = df['movies'].dropna()
df2 = df2.explode()
# df2 = df2.value_counts().sample(40)
df2 = df2.value_counts()

print('Number of records: {}\n'.format(df2.shape[0]))

print(df2.head(40))


# top20cities = df['city'].value_counts()[:20].index.tolist()
# print(top20cities)
=======
# print(df2.head())
# print(df2.info())

top20cities = df['city'].value_counts()[:20].index.tolist()
print(top20cities)
>>>>>>> 5681914cf8e6f2efd40c5430ce4fbbb6c46a3379

### parsing the dates
df['day'] = df['bday'].apply(lambda x: bdays(x)).astype(dtype='Int64')
df['month'] = df['bday'].apply(lambda x: bdays(x, type='month')).astype(dtype='Int64')
<<<<<<< HEAD
df['year'] = df['bday'].apply(lambda x: bdays(x, type='year')).astype(dtype='Int64')
year = df[['year', 'sex']].dropna()
year = year[year['year'] > 1960]
print(year.shape)
year['sex'] = year['sex'].apply(lambda x: 'male' if x == 2 else 'female')


plt.figure(figsize=(15, 5))
plt.xticks(rotation=90)
sns.countplot(data=year, x='year', hue='sex')
plt.xlabel('Birth year')
plt.ylabel('Count')
plt.title('Birth year distribution')
plt.tight_layout()
plt.savefig('age_distrib.png')
plt.show()
=======
# df['year'] = df['bday'].apply(lambda x: bdays(x, type='year')).astype(dtype='Int64')
>>>>>>> 5681914cf8e6f2efd40c5430ce4fbbb6c46a3379

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
<<<<<<< HEAD
# df2 = df[['city', 'music']]
# df2 = df2[df2['city'].isin(top20cities)]
# df2['music'] = df2['music'].apply(lambda x: moviesmusic(x))
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
=======
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
>>>>>>> 5681914cf8e6f2efd40c5430ce4fbbb6c46a3379

# movies = df['movies'].apply(lambda x: moviesmusic(x))
# print(movies.dropna().explode().value_counts().tail(60))

# print(df.head(40))
# print(df.shape)