import random

def create_user():
    rand = random.randrange(1,999999)
    name = str(rand)
    username = 'user_' + name
    email = username + '@ermiry.com'
    
    return name, username, email

if __name__ == "__main__":
    create_user()