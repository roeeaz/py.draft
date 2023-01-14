import bookings_class
import customers_class
import rooms_class
from bookings_class import Bookings
from customers_class import Customers

b1=Bookings
c1=Customers
customers_class.Customers._new_customer(12,'roee','er','er','er',23)
with open("customers.file","r")as r:
    l=r.readlines()
    assert l[-1]=="12, roee, er, er, er, 23"































