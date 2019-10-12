import glob
import os
import pandas as pd

stop = [word.split() for word in open("C:\\Users\\Ruben\\Documents\\Artikelen\\Joris\\stopwords-nl.txt", 'r', encoding = "utf-8").readlines()]

os.chdir("D:/Rampen")

list_csv = sorted(glob.glob('*bigrams.csv'))

for c in list_csv[0:1]:
    d= pd.read_csv(c)
    d = d[d['gram'].str.contains("_ramp")]
    d['gram'] = d['gram'].str.split('_').str[0]
    d = d.reset_index(drop=True)
    d = d.sort_values('count',ascending=False)

    print(d.head())
