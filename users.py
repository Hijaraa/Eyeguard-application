from customtkinter import *
from tkinter import *
app=CTk()
class User:
    def __init__(self, name, user_id, role):
        self.name = name
        self.user_id = user_id
        self.role = role

    def __str__(self):
        return f"Name: {self.name}, ID: {self.user_id}, Role: {self.role}"

class Student(User):
    def __init__(self, name, user_id, major):
        super().__init__(name, user_id, "Student")
        self.major = major

    def __str__(self):
        return super().__str__() + f", Major: {self.major}"

class Visitor(User):
    def __init__(self, name, user_id, reason_for_visit):
        super().__init__(name, user_id, "Visitor")
        self.reason_for_visit = reason_for_visit

    def __str__(self):
        return super().__str__() + f", Reason for visit: {self.reason_for_visit}"

class Personnel(User):
    def __init__(self, name, user_id, department):
        super().__init__(name, user_id, "Personnel")
        self.department = department

    def __str__(self):
        return super().__str__() + f", Department: {self.department}"

app.mainloop()