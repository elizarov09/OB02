class User:
    def __init__(self, user_id, name, access_level='user'):
        self._user_id = user_id
        self._name = name
        self._access_level = access_level

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_access_level(self):
        return self._access_level


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, access_level='admin')
        self._users = []

    def add_user(self, user):
        if not any(u.get_user_id() == user.get_user_id() for u in self._users):
            self._users.append(user)
            print(f"User {user.get_name()} added.")
        else:
            print("User already exists.")

    def remove_user(self, user_id):
        for i, user in enumerate(self._users):
            if user.get_user_id() == user_id:
                del self._users[i]
                print(f"User {user_id} removed.")
                return
        print("User not found.")

    def list_users(self):
        for user in self._users:
            print(f"ID: {user.get_user_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}")

admin = Admin('001', 'Alice')

user1 = User('002', 'Bob')
user2 = User('003', 'Charlie')

admin.add_user(user1)
admin.add_user(user2)

admin.list_users()

admin.remove_user('002')

admin.list_users()
