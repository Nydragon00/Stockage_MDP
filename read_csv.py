import csv
import os
import math

dir_path = os.path.dirname(os.path.realpath(__file__))
dir = dir_path + '/password.csv'


def decrypt():
 with open(dir, mode='r') as csv_pwd_db:
  reader = csv.reader(csv_pwd_db)
  for x in reader:
   element = x[2].split(",")
   x = 0
   for data in element:
    element[x] = data.replace(" ", "").replace("[", "").replace("]", "")
    element[x] = (float(element[x]) * 111000) ** (1/3.141592653589793)
    x += 1
   print (element)

decrypt()
