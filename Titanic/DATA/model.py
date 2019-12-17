import numpy as np
import csv

pid = []
with open('train.csv','rt')as f:
    data = csv.reader(f)
    for row in data:
        print(row[1])
##        pid.append(row[0])
##print(pid[0])
