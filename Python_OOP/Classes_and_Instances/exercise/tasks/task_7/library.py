from user import User


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def add_user(self, user: User):
        if user not in self.user_records:
            self.user_records.append(user)
        return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user: User):
        if user in self.user_records:
            self.user_records.remove(user)
            del self.rented_books[user]
        else:
            return "We could not find such user to remove!"

    def change_username(self, user_id, new_username):
        filtered_users = [u for u in self.user_records if u.user_id == user_id]
        if filtered_users:
            user = filtered_users[0]
            if not user.username == new_username:
                old_username = user.username
                user.username = new_username
                if old_username in self.rented_books:
                    books_for_user = self.rented_books[old_username]
                    del self.rented_books[old_username]
                    self.rented_books[user.username] = books_for_user
            else:
                return "Please check again the provided username -" \
                       " it should be different than the username used so far!"
        else:
            return f"There is no user with id = {user_id}!"
