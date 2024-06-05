from user import User
from property import Property
class Host(User):
    def __init__(self, user_id, name, contact_num):
        super().__init__(user_id, name, contact_num)
        self.properties_listed = []

    def list_property(self, property_details):
        property = Property(**property_details)
        self.properties_listed.append(property)
        return property

    def update_property(self, property_id, new_details):
        for prop in self.properties_listed:
            if prop.property_id == property_id:
                for key, value in new_details.items():
                    setattr(prop, key, value)
                return True
        return False

    def remove_property(self, property_id):
        self.properties_listed = [prop for prop in self.properties_listed if prop.property_id != property_id]
