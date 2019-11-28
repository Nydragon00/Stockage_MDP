import csv
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
dir = dir_path + '\\password.csv'


def encrypt(tag, user_name, pwd, CURL):
    string = ""
    with open(dir, mode='a') as csv_pwd_db:
        pwd = [ord(c) for c in pwd]
        for x in range(0, len(pwd)):
            test = (pwd[x] ** 3.141592653589793) / 111000
            test = str(test) + ","
            string += test

        pwd_val = [tag, user_name, string[:-1], CURL]
        writer = csv.writer(csv_pwd_db)
        writer.writerow(pwd_val)
