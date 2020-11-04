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
    ret = requests.get(r'https://api.vk.com/method/users.get?user_id={}&access_token={}&fields=country,city,sex,bdate,music,movies&v=5.124'.format(uid, token)).json()
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

stop = 619000000

for uid in range(last_uid + 1, stop):
    
    rawdata = uid_info(uid)

    try:
        if rawdata['response'][0]['deactivated']:
            continue
    except:
        pass

    try:
        name = str(rawdata['response'][0]['first_name'])
        if name == 'DELETED':
            continue
    except:
        name = ''
        
    try:
        last_name = str(rawdata['response'][0]['last_name'])
    except:
        last_name = ''

    try:
        sex = rawdata['response'][0]['sex']
    except:
        sex = ''
    
    try:
        country = rawdata['response'][0]['country']['title']
    except:
        country = ''
    
    try:
        city = rawdata['response'][0]['city']['title']
    except:
        city = ''

    try:
        bdate = rawdata['response'][0]['bdate']
    except:
        bdate = ''
    
    try:
        music = rawdata['response'][0]['music']
    except:
        music = ''
    
    try:
        movies = rawdata['response'][0]['movies']
    except:
        movies = ''
    
    l += 1

    print('Line number: ', l)
    print('UID: ', uid, ' of ', stop, ' ({:.2f} %)'.format(uid / stop * 100))
    print('Name: ', name)
    print('Last Name: ', last_name)
    print('Sex: ', sex)
    print('Country: ', country)
    print('City: ', city)
    print('Birth date: ', bdate)
    print('Music: ', music)
    print('Movies: ', movies)
    print()

    write_csv([uid,
        name,
        last_name,
        sex,
        country,
        city,
        bdate,
        music,
        movies])