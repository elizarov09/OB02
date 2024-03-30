class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access_level = 'user'

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def set_name(self, name):
        self._name = name


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'
        self._user_list = []

    def add_user(self, user):
        if user not in self._user_list:
            self._user_list.append(user)
            print(f"User {user.get_name()} added.")

    def remove_user(self, user):
        if user in self._user_list:
            self._user_list.remove(user)
            print(f"User {user.get_name()} removed.")

    def get_user_list(self):
        return [user.get_name() for user in self._user_list]


# Пример использования
admin = Admin(1, "Admin User")
user1 = User(2, "John Doe")
user2 = User(3, "Jane Doe")

admin.add_user(user1)
admin.add_user(user2)

print("Users in the system:", admin.get_user_list())

admin.remove_user(user1)

print("Users after removal:", admin.get_user_list())
