import csv 

def loadCSV(file_path, skip_header=True):
        data = []
        new_data=[]
        with open(file_path, mode ='r',encoding="utf8")as f:
            csvFile = csv.reader(f)
            if skip_header:
               columns = next(csvFile)  # Skip header
           
            for line in csvFile:
                data.append(dict(zip(columns, line)))
                
        print(data)
    
# file=loadCSV('Hayal_No_Status.csv')
