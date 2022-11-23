class User:
     __password = "password"

     def get_password(self):
          return self.__password


class Active_user(User):

     def get_password(self):
          return "********"

active_user = Active_user()
print(active_user.get_password())



