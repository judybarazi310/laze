from django.db import models


"""
All of these are from our Model Class Diagram.
"""


class Administrator(User):
    def __init__(self, password, email, username, password_admin):
        super().__init__(password, username, email)
        self.password_admin = password_admin


class User(Guest):
    def __init__(self, password, username, email):
        super().__init__(email)
        self.password = password
        self.username = username


class Guest:
    def __init__(self, email):
        self.email = email


class Pin:
    def __init__(self, title, description, rating):
        self.title = title
        self.description = description
        self.rating = rating
