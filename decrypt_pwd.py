#importer bibliothèques
import csv
import os
import encrypt_pwd
from math import sqrt
	
#chemin
dir_path = os.path.dirname(os.path.realpath(__file__))
dir = dir_path + '\\password.csv'

#ouvrir en mode lecture
with open(dir, mode='r') as csv_pwd_db:
	db_read = csv_pwd_db.read()

# déchiffrer
	for x in range(0, len(pwd)):
		pwd[x] = (pwd[x] / math.sqrt(3.141592653589793)) * 111000 / (x + 1)
		print (pwd[x])
