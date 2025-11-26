class Soldier:
    def __init__(self,soldier_number,first_name,last_name,gender,city,distance):
        self.soldier_number=soldier_number
        self.first_name=first_name
        self.last_name=last_name
        self.gender=gender
        self.city=city
        self.distance=distance
    def str(self):
        return f"soldier_number{self.soldier_number},first_name{self.first_name},last_name{self.last_name}gender{self.gender}city{self.city}distance{self.distance}"
    
class Dorm:
    conter_rooms=0
    conter_pepole_in_romm=0
    def __init__(self,rooms,pepole_in_room):
        self.rooms=rooms
        conter_rooms+=1
        self.pepole_in_room=pepole_in_room
        conter_pepole_in_romm+=1
