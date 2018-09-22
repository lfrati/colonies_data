import os
import json
import csv
import numpy as np
from pathlib import Path

path = Path('/Users/lapofrati/git/colonies_data/labels')

data = [json.load((path/label).open()) for label in os.listdir(path)]
data = [(el, np.array([size for x,y,size in el['colonies']])) for el in data]
data = [{'id': info['id'],
         'strain' : info['strain'], 
         'time' : info['time'], 
         'concentration' : info['concentration'],
         'count' : len(colonies), 
         'mean' : colonies.mean(), 
         'std' : colonies.std()}  
        for info, colonies in data]

with open('summary.csv', 'w') as csvFile:
    fields = ['id', 'strain', 'time', 'concentration','count','mean','std']
    writer = csv.DictWriter(csvFile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)
print("writing completed")
csvFile.close()