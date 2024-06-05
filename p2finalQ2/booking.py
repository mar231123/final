class Booking():
    def __init__(self, booking_id, property, guest, check_in_date, check_out_date, booking_status="confirmed"):
        self.booking_id = booking_id
        self.property = property
        self.guest = guest 
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.booking_status = booking_status
    def confirm_booking(self):
        self.booking_status = "confirmed"
    def cancel_booking(self):
        self.booking_status = "canceled"
    def get_booking_details(self):
        return f"Booking ID: {self.booking_id}, Property: {self.property.name}, Guest: {self.guest.name}, Check-in: {self.check_in_date}, Check-out: {self.check_out_date}, Status: {self.booking_status}"
