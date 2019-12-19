import numpy as np
import pandas as pd
##import csv

def input(filename):

    df = pd.read_excel(filename,sheet_name=0)
    pid = df[0].tolist()

    #y = l[1:][1]
    #cls = l[1:][2]
    #name = l[1:][3]
    #sex = l[1:][4]
    #age = l[1:][5]
    #print(name[11] + age[11])
    print(pid[11])

input('train.csv')
