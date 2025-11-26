import csv 
from claasas import *
def loadCSV(file_path):
        data = []
        with open(file_path, mode ='r',encoding="utf8")as f:
            csvFile = csv.DictReader(f)
            for line in csvFile:
                data.append(dict(line))
                
                
        return(data)
    

file=loadCSV('Hayal_No_Status.csv')


sorted_file = sorted(file, key=lambda x: int(x['distance']))
