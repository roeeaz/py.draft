import customers_class
import rooms_class
import bookings_class

def welcome():
    print('*****Welcome to our hotel*****')
    print('What action would you like to do?')
    print('1.add a new room')
    print('2.add a new customer')
    print('3.book a room')
    print('4.cancel booking')
    print('5.display all rooms')
    print('6.display all customers')
    print('7.display all bookings')
    print('8.Display booked rooms for a specific date ')
    print('9.find room by type')
    print('10.find room by number')
    print('11.find customer by name')
    print('12.remove room')
    print('13.remove customer')
    print('14.get out from the menu')
    print('*before you tell us your choice we want you to see all the rooms type in our hotel')
    with open("rooms.json", "r") as f:
        print(f.read())
    c=input("enter your choice please: ")

    if c=='1':
            id=input('room id :')
            size= input('room size :')
            capacity= input('room capacity :')
            number_of_beds= input('number of beds :')
            room_type= input('room type :')
            price= input('price :')
            rooms_class.Rooms._add_room(id, size, capacity, number_of_beds, room_type, price)
            print("a.go back to the menu")
            print("b.exit")
            choice=input("enter your choice please")
            if choice=="a":
                welcome()
            else:
                print("goodbye")

    elif c=='2':
            cust_id=input('customer id :')
            name=input('customer name :')
            address = input('customer address :')
            city = input('customer city :')
            email = input('customer email :')
            age = input('customer age :')
            customers_class.Customers._new_customer(cust_id,name,address,city,email,age)
            print("a.go back to the menu")
            print("b.exit")
            choice=input("enter your choice please")
            if choice=="a":
                welcome()
            else:
                print("goodbye")


    elif c=='3':
        print('book a room')
        room_id= input('room id :')
        customer_id= input('customer id :')
        arrival_date= input('arrival date :')
        departure_date= input('departure date :')
        type = input('room type :')
        night_price= input('night price :')



        room_id=room_id
        room_id=room_id
        arrival_date=arrival_date
        departure_date=departure_date
        bookings_class.Bookings._minimum_nights(type,arrival_date,departure_date)
        bookings_class.Bookings._book_a_room(room_id,customer_id,arrival_date,departure_date,night_price)
        bookings_class.Bookings._check_availability(room_id)
        print("a.go back to the menu")
        print("b.exit")
        choice = input("enter your choice please")
        if choice == "a":
            welcome()
        else:
            print("goodbye")




    elif c=='4':
        print('cancel booking')
        room_id=input('enter room id please')
        bookings_class.Bookings._cancel_booking(room_id)
        print("a.go back to the menu")
        print("b.exit")
        choice = input("enter your choice please")
        if choice == "a":
            welcome()
        else:
            print("goodbye")



    elif c=='5':
        print('display all rooms')
        rooms_class.Rooms._display_all_rooms()
        print("a.go back to the menu")
        print("b.exit")
        choice = input("enter your choice please")
        if choice == "a":
            welcome()
        else:
            print("goodbye")


    elif c=='6':
        print('display all customers')
        customers_class.Customers._display_all_customers()
        print("a.go back to the menu")
        print("b.exit")
        choice = input("enter your choice please")
        if choice == "a":
            welcome()
        else:
            print("goodbye")




    elif c=='7':
        print('display all bookings')
        bookings_class.Bookings._display_all_bookings()
        print("a.go back to the menu")
        print("b.exit")
        choice = input("enter your choice please")
        if choice == "a":
            welcome()
        else:
            print("goodbye")


    elif c=='8':
        print('Display booked rooms for a specific date ')
        arrival=input('arrival date :')
        departure = input('departur date :')
        bookings_class.Bookings._display_specific_dates_booked_rooms(arrival,departure)
        print("a.go back to the menu")
        print("b.exit")
        choice = input("enter your choice please")
        if choice == "a":
            welcome()
        else:
            print("goodbye")




    elif c=='9':
        print("find room by type")
        room_type=input('enter room type please :')
        rooms_class.Rooms._find_room_by_type(room_type)
        print("a.go back to the menu")
        print("b.exit")
        choice = input("enter your choice please")
        if choice == "a":
            welcome()
        else:
            print("goodbye")

    elif c=='10':
        print("find room by number")
        room_id = input('enter room id please :')
        rooms_class.Rooms._find_room_by_number(room_id)
        print("a.go back to the menu")
        print("b.exit")
        choice = input("enter your choice please")
        if choice == "a":
            welcome()
        else:
            print("goodbye")


    elif c=='11':
        print("find customer by name")
        name=input('enter customer name please :')
        customers_class.Customers._find_customer_by_name(name)
        print("a.go back to the menu")
        print("b.exit")
        choice = input("enter your choice please")
        if choice == "a":
            welcome()
        else:
            print("goodbye")

    elif c=='12':
        print("remove room")
        id= input('enter room id please :')
        rooms_class.Rooms._remove_room(id)
        print("a.go back to the menu")
        print("b.exit")
        choice = input("enter your choice please")
        if choice == "a":
            welcome()
        else:
            print("goodbye")


    elif c=='13':
        print("remove customer")
        name = input('enter customer name please :')
        customers_class.Customers._remove_customer(name)
        print("a.go back to the menu")
        print("b.exit")
        choice = input("enter your choice please")
        if choice == "a":
            welcome()
        else:
            print("goodbye")

    elif c=='14':
        print('goodbye')
welcome()














