'''
collects user data from vk

sex: 1 — женский;
2 — мужской;
0 — пол не указан.

relation: 1 — не женат/не замужем;
2 — есть друг/есть подруга;
3 — помолвлен/помолвлена;
4 — женат/замужем;
5 — всё сложно;
6 — в активном поиске;
7 — влюблён/влюблена;
8 — в гражданском браке;
0 — не указано
'''
import requests
import csv
from options import token
import os.path


def write_csv(data):
    with open('vk_people.csv', 'a', newline='', encoding='utf-8') as f:
        #newline - to avoid blank rows after each record
        #encoding utf-16 - we are in russia, thats all
        writer = csv.writer(f, delimiter=';')
        writer.writerow(data)

def uid_info(uid):
    ret = requests.get(r'https://api.vk.com/method/users.get?user_ids={}&access_token={}&fields=country,city,sex,bdate,music,movies,relation,games&v=5.124'.format(uid, token)).json()
    return ret

if os.path.exists('vk_people.csv'):
    with open('vk_people.csv', 'r', encoding='utf-8') as f:
        l = 1
        for i in f:
            l += 1
            pass
        last_uid = int(i.split(';')[0])
        print('UID in last line: %d' % last_uid)
        print('Number of lines: %d' % l)
else:
    l = 1
    last_uid = 0

stop = 100000000
uids_batch = 200

rest = stop - last_uid
steps = rest // uids_batch
tail = rest % uids_batch

uids = [list(range(last_uid, last_uid + uids_batch))]

for i in range(steps):
    uids.append(list(range(uids[-1][-1], uids[-1][-1] + uids_batch)))

uids.append(list(range(uids[-1][-1], uids[-1][-1] + tail)))

for uid in uids:
    uid = str(uid).strip('[]').replace(' ', '')
    rawdata = uid_info(uid)

    for user_raw in rawdata['response']:
        try:
            if user_raw['deactivated']:
                continue
        except:
            pass

        try:
            name = str(user_raw['first_name'])
            if name == 'DELETED':
                continue
        except:
            name = ''
            
        try:
            last_name = str(user_raw['last_name'])
        except:
            last_name = ''

        try:
            sex = user_raw['sex']
        except:
            sex = ''
        
        try:
            country = user_raw['country']['title']
        except:
            country = ''
        
        try:
            city = user_raw['city']['title']
        except:
            city = ''

        try:
            bdate = user_raw['bdate']
        except:
            bdate = ''
        
        try:
            music = user_raw['music']
        except:
            music = ''
        
        try:
            movies = user_raw['movies']
        except:
            movies = ''
        try:
            relation = user_raw['relation']
        except:
            relation = ''

        try:
            user_id = int(user_raw['id'])
        except:
            user_id = ''

        try:
            games = user_raw['games']
        except:
            games = ''
        
        l += 1

        print('Line number: ', l)
        print('UID: {} of {} - ({:.2f} %)'.format(user_id, stop, user_id / stop * 100))
        print('Name: ', name)
        print('Last Name: ', last_name)
        print('Sex: ', sex)
        print('Country: ', country)
        print('City: ', city)
        print('Birth date: ', bdate)
        print('Music: ', music)
        print('Movies: ', movies)
        print('Games: ', games)
        print('Relation: ', relation)
        print()

        write_csv([user_id,
            name,
            last_name,
            sex,
            country,
            city,
            bdate,
            music,
            movies,
            games,
            relation])
