from User import User

class AdminUser(User):
    def __init__(self, name):
        super().__init__()
        self.role = "Admin"
        self.name = name
    
    def get_role(self):
        print(f"{self.name} es {self.role} user")
        return self.role
    
    def has_permission(self, permission):
        return True
    
user2 = AdminUser("Mocca")
user2.get_role()
print(user2.has_permission("write"))
print(user2.has_permission("read"))