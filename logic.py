import csv 
from claasas import *
def loadCSV(file_path):
        data = []
        with open(file_path, mode ='r',encoding="utf8")as f:
            csvFile = csv.DictReader(f)
            for line in csvFile:
                data.append(dict(line))
                
                
        return(data)
file_r=loadCSV("Hayal_No_Status.csv")



sorted_file = sorted(file_r, key=lambda x: int(x['distance']),reverse=True)


def csv_to_obg(sorted_file):
    soldier_list=[]
    for s in sorted_file:
        soldier = Soldier(s["soder_nomber"], s["first_name"],s["last_name"],s["gender"],s["city"],s["distance"])
        soldier_list.append(soldier)
    return soldier_list
    

 

def shibutz(sorted_file):
    while Dorm.conter_dorm<=2:
        dorm1=Dorm(1)
        dorm2=Dorm(1)
    while Rooms.conter_rooms <=10:
        for i in range(10):
            i =Rooms(dorm1,10)
            while Pepole_in_room.conter_pepole_in_room <=8:
                for p in i:
                    p=Pepole_in_room(dorm1,i,8)
            
            
                for j in range(10):
                    j=Rooms(dorm2,10)
                    for p2 in j:
                        p2=Pepole_in_room(dorm2,j,8)
            