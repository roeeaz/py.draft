class Bookings:
        def __init__(self,customer_id,room_id,arrival_date,departure_date,total_price):
                self.customer_id=customer_id
                self.room_id=room_id
                self.arrival_date=arrival_date
                self.departure_date=departure_date
                self.total_price=total_price

        def _minimum_nights(type,arrival_date,departure_date):
                nights=(int(departure_date)-int(arrival_date))
                if type=="deluxe" and nights<2:
                        raise ValueError("deluxe room must be taken for at least two days")
                elif type=="suite" and nights<3:
                        raise ValueError("a suite must be taken for at least three days")
                else:
                        print("Your order meets the requirements")

        def _display_all_bookings():
                with open('bookings.file', 'r') as r:
                        all_bookings = r.read()
                print(all_bookings)

        def _display_specific_dates_booked_rooms(arrival,departure):
                with open('bookings.file','r') as d:
                        lines = []
                        for line in d:
                                if arrival in line and departure in line:
                                        lines.append(line)
                        for i in lines:
                                print(i)



        def _display_specific_dates_availables_rooms(arrival,departure):
                with open('bookings.file', 'r') as d:
                        l = []
                        for line in d:
                                if arrival not in line and departure not in line:
                                        l.append(line)
                        for i in l:
                                        return i


        def _check_availability(room_id):
                with open('bookings.file', 'r') as b:
                        for line in b:
                                if room_id in line[0]:
                                        raise ValueError('room not available')
                                else:
                                        return ' '




        def _book_a_room(room_id,customer_id,arrival_date,departure_date,night_price):
                with open('bookings.file', 'a') as b:
                        nights = (int(departure_date)) - (int(arrival_date))
                        b.write (f'{room_id},{customer_id},{arrival_date},{departure_date},{(int(nights))*(int(night_price))}$\n')
                print(f' The room has been successfully booked,the total price is {(int(nights))*(int(night_price))}$')

        def _cancel_booking(room_id):
                with open("bookings.file", "r") as r:
                        lines = r.readlines()
                with open('bookings.file', 'w') as r:
                        for line in lines:
                                if room_id not in line[0]:
                                        r.write(line)
                                        print('Your order has been cancelled')



        def __str__(self):
                return (f'\ncustomer id:{self.customer_id}/ room id:{self.room_id}/ arrival date:{self.arrival_date}/ departure date:{self.departure_date}/ total price:{self.total_price}')


#this is to the tests file
#book1=Bookings('31','1',22,25,200)
#book1._minimum_nights('deluxe',22,24)



















#def __str__(self):
#        return f'customer id: {self.customer_id} take room:{self.room} for {self.nights} nights'

#def __new_room(self,room):
#        self.rooms.append(room)


#def __new_booking(self,customer_id,room,nights):
#        __new_booking=Bookings(customer_id,room,nights)
#        bookings.append(__new_booking)

#def __price(self):
#       return self.price*self.nights
