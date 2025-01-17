class User:
    def __init__(
        self, first_name: str, last_name: str, username: str, email: str, password: str
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password
