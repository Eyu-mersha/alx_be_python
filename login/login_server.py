import hashlib
users=[]
class Credentials:
    def __init__(self,username,password):
        self.username = username
        self.password = password 
    def __repr__(self):
        return print(f"Username: {self.username} Password: {self.password}")
    def createUser(username,password):
        credential = Credentials(username,password)
        users.append(credential)
    
     
def hash_password(password):
    sha256 = hashlib.sha256()
    sha256.update(password.encode('utf-8'))
    return sha256.hexdigest()

