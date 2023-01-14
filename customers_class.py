class Customers:
    def __init__(self,cust_id,name,address,city,email,age):
        self.cust_id=cust_id
        self.name=name
        self.address=address
        self.city=city
        self.email=email
        self.age=age

    def _new_customer(cust_id,name,address,city,email,age):
        with open('customers.file', 'a') as r:
            r.write(f'\n{cust_id}, {name}, {address}, {city}, {email}, {age}')
            print('Customer added successfully')

    def _find_customer_by_name(name):
        with open('customers.file','r') as n:
            r=n.readlines()
            for line in r:
                    if name in line:
                        print(line)

    def _display_all_customers():
        with open('customers.file','r') as r:
            all_customers=r.read()
            print(all_customers)

    def _remove_customer(name):
        with open('customers.file', "r") as r:
            lines = r.readlines()
        with open('customers.file', 'w') as r:
            for line in lines:
                if name not in line:
                    r.write(line)
            print("The customer has been successfully removed")






    def __str__(self):
            return f'customer id is: {self.cust_id}\ncustomer name is: {self.name}\ncustomer adress: {self.address}\n customer city: {self.city}\n customer email: {self.email}\n customer age: {self.age}'





