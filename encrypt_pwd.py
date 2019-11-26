import csv
import os
import math

dir_path = os.path.dirname(os.path.realpath(__file__))
dir = dir_path + '\\password.csv'

with open(dir, mode='wr') as csv_pwd_db:
    db_read = csv_pwd_db.read()
    pwd_tag = input("Enter your password name: ")
    pwd = input("Enter your password: ")
    for x in db_read:
        print(x)
    pwd = [ord(c) for c in pwd]

    for x in range(0, len(pwd)):
        # pwd[x] = pwd[x] ** 2 - pwd[x]
        pwd[x] = (pwd[x] ** 3.141592653589793) / 111000
        print (pwd[x])
        # pwd[x] = pwd[x] / 3.141592653589793
        # pwd[x] = round(pwd[x])

    pwd_val = [pwd_tag, pwd]
    writer = csv.writer(csv_pwd_db)
    writer.writerow(pwd_val)
