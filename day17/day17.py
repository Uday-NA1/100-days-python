class User:
    def __init__(self, id, username):
        print("New user is being created.")
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0
    
    def follow(self, user):
        self.following += 1
        user.followers += 1

    def stats(self):
        print(self.id, self.username, self.followers, self.following)

user_1 = User("001", "john_doe")
user_2 = User("002", "jane_smith")
user_1.follow(user_2)

user_1.stats()
user_2.stats()

