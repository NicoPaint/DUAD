from User import User

class RegularUser(User):
    def __init__(self, name):
        super().__init__()
        self.role = "Regular"
        self.name = name
    
    def get_role(self):
        print(f"{self.name} es {self.role} user")
        return self.role
    
    def has_permission(self, permission):
        if permission.lower() != "read":
            return False
        return True

user1 = RegularUser("Miwi")
user1.get_role()
print(user1.has_permission("write"))
print(user1.has_permission("read"))