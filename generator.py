import logging
import random
import string
import time


def random_phone_number():
    return f'0{random.randint(10**(9 - 1), (10**9) - 1)}'


def random_date(start, end, time_format='%Y/%m/%d', prop=random.random()):

    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def get_disease(path='list_diseases.txt'):
    file = open(path, 'r', encoding='utf-8')
    diseases = []

    for disease in file.readlines():
        diseases.append(disease.strip('\n'))
    # print(diseases)
    file.close()
    return diseases[random.randint(0, len(diseases) - 1)]


def get_instruction(path='special_ins.txt'):
    file = open(path, 'r', encoding='utf-8')
    ins_ls = []

    for ins in file.readlines():
        ins_ls.append(ins.strip('\n'))

    file.close()
    return ins_ls[random.randint(0, len(ins_ls) - 1)]


def get_random_station():
    station_list = ['Lab Station', 'Shelving Station', 'Secure Sation']
    return station_list[random.randint(0, len(station_list) - 1)]


def get_med_list(path='med_list.txt'):
    file = open(path, 'r', encoding='utf-8')
    med_lst = []

    for med in file.readlines():
        med_lst.append(med.strip('\n'))

    file.close()
    return med_lst
