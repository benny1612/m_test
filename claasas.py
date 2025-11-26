class Soldier:
    def __init__(self,soldier_number,first_name,last_name,gender,city,distance,status):
        self.soldier_number=soldier_number
        self.first_name=first_name
        self.last_name=last_name
        self.gender=gender
        self.city=city
        self.distance=distance
        self.status=status
    
class Dorm:
    conter_dorm=0
    def __init__(self,dorm):
        self.dorm=dorm
        Dorm.conter_dorm+=1        

class Rooms(Dorm):
    conter_rooms=0
    def __init__(self, dorm,rooms):
        super().__init__(dorm)
        self.rooms=rooms
        Rooms.conter_rooms+=1

class Pepole_in_room(Rooms):
    conter_pepole_in_room=0
    def __init__(self, dorm, rooms,pepole_in_room):
        self.pepole_in_room=pepole_in_room
        super().__init__(dorm, rooms)
        Pepole_in_room.conter_pepole_in_room+=1
    