import random
import mysql.connector as mysql

from schemas import Doctor, File, Medicine, Medicine_included, Patient, Pharmacist, Prescription, Station


def connection(debug=False):
    mydb_connection = mysql.connect(
        host="SG-shared-viper-3052-6227-mysql-master.servers.mongodirector.com",
        user="sgroot",
        password="contact for password",
        database="Mercy_Hospital")

    return mydb_connection


def insert_sql(table) -> str:
    schema = table.__dict__
    tbname = schema['tablename']
    schema.pop('tablename', None)
    schema.pop('id', None)
    vals = []

    for val in schema.values():
        vals.append(val)

    s = '%s,' * len(vals)
    return f"INSERT INTO {tbname} ({', '.join(vals)}) VALUES ({s[:-1]})"


def create_station(amount=3):
    cn = connection()
    cur = cn.cursor()

    val_list = []
    for i in range(0, amount):
        station = Station()
        val_list.append(station.insert(index=i))

    sql = insert_sql(Station())
    print(sql)

    try:
        cur.executemany(sql, val_list)
        cn.commit()
    except mysql.Error as e:
        print(e)

    cn.close()


def create_pharmacist(amount=30):
    cn = connection()
    cur = cn.cursor()

    val_list = []
    for i in range(0, amount):
        val_list.append(Pharmacist().insert())

    sql = insert_sql(Pharmacist())
    print(sql)

    try:
        cur.executemany(sql, val_list)
        cn.commit()
    except mysql.Error as e:
        print(e)

    cn.close()

    print('Created 30 pharmacists')


def create_patient(amount=100):
    cn = connection()
    cur = cn.cursor()

    val_list = []
    for i in range(0, amount):
        val_list.append(Patient().insert())

    sql = insert_sql(Patient())
    print(sql)

    try:
        cur.executemany(sql, val_list)
        cn.commit()
    except mysql.Error as e:
        print(e)

    cn.close()

    print('Created 100 patients')


def create_file():
    cn = connection()
    cur = cn.cursor()

    val_list = []
    count = 0
    i = 1
    while (i < 101):
        val_list.append(File().insert(i))

        if random.randint(1, 10) <= 2: i = i - 1
        else: i += 1
        count += 1

    sql = insert_sql(File())
    print(sql)

    try:
        cur.executemany(sql, val_list)
        cn.commit()
    except mysql.Error as e:
        print(e)

    cn.close()
    # Created 178 File
    print(f'Created {count} File')


def create_doctor(amount=35):
    cn = connection()
    cur = cn.cursor()

    val_list = []
    for i in range(0, amount):
        val_list.append(Doctor().insert())

    sql = insert_sql(Doctor())
    print(sql)

    try:
        cur.executemany(sql, val_list)
        cn.commit()
    except mysql.Error as e:
        print(e)

    cn.close()

    print('Created 35 Doctor')


def create_prescription():
    cn = connection()
    cur = cn.cursor()

    val_list = []
    count = 0
    i = 1
    while (i < 101):
        val_list.append(Prescription().insert(i))

        if random.randint(1, 10) <= 1: i = i - 1
        else: i += 1
        count += 1

    sql = insert_sql(Prescription())
    print(sql)

    try:
        cur.executemany(sql, val_list)
        cn.commit()
    except mysql.Error as e:
        print(e)

    cn.close()
    # Created 110 Prescription
    print(f'Created {count} Prescription')


def create_medicine():
    cn = connection()
    cur = cn.cursor()

    val_list = []
    for i in range(0, 67):
        val_list.append(Medicine().insert(i))

    sql = insert_sql(Medicine())
    print(sql)

    try:
        cur.executemany(sql, val_list)
        cn.commit()
    except mysql.Error as e:
        print(e)

    cn.close()

    print('Created 67 Medicines')


def create_medicine_include():
    cn = connection()
    cur = cn.cursor()

    val_list = []
    count = 0
    i = 1
    while (i < 111):
        val_list.append(Medicine_included().insert(i))

        if random.randint(1, 30) <= 1: i = i - 1
        else: i += 1
        count += 1

    sql = insert_sql(Medicine_included())
    print(sql)

    try:
        cur.executemany(sql, val_list)
        cn.commit()
    except mysql.Error as e:
        print(e)

    cn.close()

    print('Created 116 medicine_included')
