import csv
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

pwd_tag = input("Enter your password name: ")
pwd = input("Enter your password: ")

pwd_val = [pwd_tag, pwd]

dir = dir_path + '\\password.csv'
print (dir)

with open(dir, mode='a') as csv_pwd_db:
    writer = csv.writer(csv_pwd_db)
    writer.writerow(pwd_val)
