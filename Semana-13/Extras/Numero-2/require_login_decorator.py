user_logged_in = False

def require_login(func):
    def wrapper(*args):
        if not user_logged_in:
            raise ValueError("Usuario no autenticado")
        
        return func(*args)
    
    return wrapper

@require_login
def view_profile():
    print("Mostrando perfil del usuario")

try:
    view_profile()
except ValueError as error:
    print(error)