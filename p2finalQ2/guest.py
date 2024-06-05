from user import User
from booking import Booking
class Guest(User):
    def __init__(self,user_id,name,contact_num):
        super().__init__(user_id,name,contact_num)
        self.bookings_made = []
    def book_property(self,property,check_in_date,check_out_date):
        if property.availability_check(check_in_date,check_out_date):
            booking_id = len(self.bookings_made) + 1 
            booking = Booking(booking_id, property, self, check_in_date, check_out_date)
            self.bookings_made.append(booking)
            property.update_availability(False)
            return booking
        else:
            return None
    def cancel_booking(self,booking_id):
        for booking in self.bookings_made:
            if booking.booking_id == booking_id:
                booking.cancel_booking()
                self.bookings_made.remove(booking)
                booking.property.update_availability(True)
                return True
        return False
