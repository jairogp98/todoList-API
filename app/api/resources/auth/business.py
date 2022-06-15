from ....database.models.users import Users
import bcrypt

def authenticate(username, password):
    print ("___authenticate")
    pswd = password.encode('utf-8')

    user = Users.query.filter_by(email = username).first()

    if user:
        hash = user.password.encode('utf-8')
        if bcrypt.checkpw(pswd, hash):
            return user
        
    

def identity (payload):
    print ("identity")
    user_id = payload['identity']
    print(user_id)

    user = Users.query.filter_by(id = user_id).first()
    return user
