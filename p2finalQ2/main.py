from datetime import date
from property import Property
from guest import Guest
from host import Host
from booking import Booking
h1 =Host(1, "Maryam Rasheed", "3454652346")
g1 =Guest(101, "Ali Sethi", "2Q353465476")
g2 =Guest(103, "Hamza", "4567547686")

p1 = h1.list_property({"property_id": 1, "name": "Cozy Apartment", "location": "gulberg", "description": "A beautiful apartment in the heart of Lahore", "price_per_night": 15000})
p2 = h1.list_property({"property_id": 2, "name": "Beach House", "location": "karachi", "description": "A luxurious beach house with sea view", "price_per_night": 30000})

b1 = g1.book_property(p1, date(2024, 7, 1), date(2024, 7, 5))
if b1:
    print("Booking is successful!")
else:
    print("Property not available for the selected dates.")

b2 = g2.book_property(p1, date(2024, 7, 1), date(2024, 7, 5))
if b2:
    print("Booking is successful!")
else:
    print("Property not available for the selected dates.")

canceled = g1.cancel_booking(b1.booking_id)
if canceled:
    print("Booking canceled successfully!")
else:
    print("Booking not found or already canceled.")

h1.update_property(1, {"price_per_night": 180})
print(b1.get_booking_details())











