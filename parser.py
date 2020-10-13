import requests
import csv
from options import token
import os.path


def write_csv(data):
    with open('vk_friends.csv', 'a', newline='', encoding='utf-8') as f:
        #newline - to avoid blank rows after each record
        #encoding utf-16 - we are in russia, thats all
        writer = csv.writer(f, delimiter=';')
        writer.writerow(data)

def uid_info(uid):
    ret = requests.get(r'https://api.vk.com/method/users.get?user_id={}&access_token={}&fields=country,city,sex&v=5.124'.format(uid, token)).json()
    return ret

# def uid_frnds(uid):
#     '''
#     returns a list of names of friends of provided VK uid
#     '''
#     ret = requests.get(r'https://api.vk.com/method/friends.get?user_id={}&access_token={}&v=5.124'.format(uid, token)).json()
#     if ret['response']['count'] > 0:
#         return [uid_name(i) for i in ret['response']['items']]

# def uid_frndscnt(uid):
#     '''
#     returns friends count from UID
#     '''
#     ret = requests.get(r'https://api.vk.com/method/friends.get?user_id={}&access_token={}&v=5.124'.format(uid, token)).json()
#     return ret['response']['count']


if os.path.exists('vk_people.csv'):
    with open('vk_friends.csv', 'r', encoding='utf-8') as f:
        l = 1
        for i in f:
            l += 1
            pass
        last_uid = int(i.split(';')[0])
        print('UID in last line: %d' % last_uid)
        print('Number of lines: %d' % l)
else:
    l = 1
    last_uid = 440000000

stop = last_uid + 1000000

for uid in range(last_uid + 1, stop):
    
    rawdata = uid_info(uid)

    try:
        name = str(rawdata['response'][0]['first_name'])
    except:
        name = ''
        
    try:
        last_name = str(rawdata['response'][0]['last_name'])
    except:
        last_name = ''

    try:
        sex = rawdata['response'][0]['sex']

        
        l += 1
        print('Line number: ', l)
        print('UID: ', uid, ' of ', stop, ' ({:.1f} %)'.format((uid - last_uid) / (stop - last_uid) * 100))
        print('Name: ', name)
        print('Last Name: ', last_name)
        print('Sex: ', sex)
        print()

        # write_csv([uid, 
        #     name, 
        #     frnds_cnt, 
        #     '|'.join(frnds_lst)])

    except:
       pass