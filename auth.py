import json
import os

data = "users_data"

if not os.path.exists(data) :
    os.makedirs(data)

def user_file(username):
    return os.path.join(data, f"{username}.json")

def create_account():
    print("=== Création de compte ===")
    username = input("Choisissez un nom d'utilisateur :\n")
    
    if os.path.exists(user_file(username)):
        print("Ce nom d'utilisateur est déjà pris.\n")
        return None, None
    
    password = input("Choisissez un mot de passe :\n")
    
    user_data = {
        "password" : password,
        "tasks" : []
    }
    
    save_user_data(username, user_data)
    
    print("Compte créé avec succès !")
    
    return (username, user_data)

def login():
    print("=== Connexion ===")
    username = input("Nom d'utilisateur :")
    
    if not os.path.exists(user_file(username)):
        print("Aucun compte trouvé avec ce nom.")
        return None, None
    
    with open(user_file(username),"r") as f :
        user_data = json.load(f)     
    
    password = input("Mot de passe :")
    
    if password != user_data["password"]:
        print("Mot de passe incorrect.")
        return None, None
    
    print(f"Bienvenue {username} !")
        
    return (username, user_data)

def save_user_data(username, user_data):
    with open(user_file(username),"w") as f :
        json.dump(user_data, f, indent = 4)











