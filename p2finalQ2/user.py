class User:
    def __init__(self,user_id,name,contact_num):
        self.name = name 
        self.contact_num = contact_num
        self.user_id = user_id
    def show_profile(self):
        return f"ID:{self.user_id},Name:{self.name},Contact Number:{self.contact_num}"
        