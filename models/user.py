from sql_alchemy import database

class UserModel(database.Model):
    user_id = database.Column(database.Integer, primary_key = True)
    username =  database.Column(database.String(40))
    hash = database.Column(database.String(200))

    def __init__(self, username, hash):
        self.username = username
        self.hash = hash
    
    def json(self):
        return {
            "user_id": self.user_id,
            "username": self.username
        }

    def save_user(self):
        database.session.add(self)
        database.session.commit()
    
    def delete_user(self):
        database.session.delete(self)
        database.session.commit()
    
    @classmethod
    def create_user(cls, username, password):
        user = cls(username, password)
        user.save_user()

        return user

    @classmethod
    def find_user(cls, user_id):
        user = cls.query.get(user_id)

        return user