class Rooms:
    def __init__(self,id,size,capacity,number_of_beds,room_type,price):
        self.id=id
        self.size=size
        self.capacity = capacity
        self.number_of_beds=number_of_beds
        self.room_type =room_type
        self.price=price



    def _add_room( id, size, capacity, number_of_beds, room_type, price):
        with open('rooms.file',"a") as r:
            r.write(f'{id} {size} {capacity} {number_of_beds} {room_type} {price}$\n')
            print('room added successfully')


    def _remove_room(id):
        with open('rooms.file', "r") as r:
            lines=r.readlines()
        with open('rooms.file','w')as r:
            for line in lines:
                if id not in line[0]:
                    r.write(line)
                print("The room has been successfully removed")



    def _find_room_by_number(room_id):
        with open('rooms.file','r')as n:
            r=n.readlines()
            for line in r:
                if room_id in line:
                    print(line)


    def _find_room_by_type(room_type):
        with open('rooms.file','r')as n:
            r=n.readlines()
            for line in r:
                    if room_type in line:
                        print(line)

    def _display_all_rooms():
        with open('rooms.file','r') as r:
            all_rooms=r.read()
            print(all_rooms)




    def __str__(self):
        return (f'{self.id}/{self.size}/{self.capacity}/{self.number_of_beds}/{self.room_type}/{self.price}&')
#דוגמה לאיך לעבוד עם ריטרן במקום פרינט
#r=Rooms(319089959,20,2,3,'delux',50)
#print(r.__str__())
#r.find_room_by_number('319089959')
#print(r)
#print(r.minimum_nights('suite',25,28))

#בדיקה אם קיים חדר כזה בכלל על פי מספר חדר ואם כן רק אז לקוח יכול לבצע הזמנה
#    def existing_room(id):
#        with open('rooms.file', 'r') as b:
#            for line in b:
#                if id not in line:
#                    raise ValueError('room not available')
#                else:
#                    return ' '

