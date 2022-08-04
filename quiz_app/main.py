class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username


user1 = User("001", "anees")

print(user1.id, user1.username)