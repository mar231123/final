class Property:
    def __init__(self,property_id,name,location,description,price_per_night,availability=True):
        self.property_id = property_id
        self.name = name
        self.location = location 
        self.price_per_night = price_per_night
        self.availability = availability
    def show_details(self):
        return f"Property:{self.name},Location:{self.location},Description:{self.description},Price per night:{self.price_per_night}"
    def availability_check(self,check_in_date,check_out_date):
        return self.availability
    def update_availability(self,availability):
        return self.availability
