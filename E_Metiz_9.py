from random import randint
# 9-1
class Restaurant(object):
    def __init__(self, restaurant_name: str, cuisine_type: str):
        """Инициализирует атрибуты"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("Name: " + self.restaurant_name + " Type: " + self.cuisine_type)

    # 9-4
    def set_number_served(self, count):
        self.number_served += count

    def open_restaurant(self):
        print("Open!")


# 9-6
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name: str, cuisine_type: str):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["vanilla", "chocolate"]

    def describe_flavors(self):
        print(self.flavors)


# 9-3
class User(object):
    def __init__(self, first_name: str, last_name: str, password: str, online: bool):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.online = online
        self.login_attempts = 1

    def describe_user(self):
        print("Info: ")
        print(self.first_name, self.last_name, self.password, self.online)

    # 9-5
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def greet_user(self):
        print("Hi, User!")


# 9-7
class Admin(User):
    def __init__(self, first_name: str, last_name: str, password: str, online: bool):
        super().__init__(first_name, last_name, password, online)

        self.privileges = Privileges()

    def describe_privileges(self):
        print(self.privileges)


# 9-8
class Privileges(object):
    def __init__(self):
        self.privileges_l = ["«разрешено добавлять»", "«разрешено удалять»", "«разрешено банить»"]

    def show_privileges_l(self):
        print(self.privileges_l)


# 9-14
class Die(object):
    def __init__(self, sides: int = 6):
        self.sides = sides

    def roll_die(self) -> int:
        return randint(1, self.sides)



restaurant1 = Restaurant("KFC", "U-shaped kitchen")
print(restaurant1.restaurant_name, restaurant1.cuisine_type)
restaurant1.describe_restaurant()
# 9-2
restaurant2 = Restaurant("Rusiko", "U-shaped kitchen")
restaurant2.describe_restaurant()
restaurant3 = Restaurant("Doski", "linear kitchen")
restaurant3.describe_restaurant()
# 9-3
user1 = User("Nikita", "Boriakov", "1234", True)
user1.describe_user()
user1.greet_user()
user2 = User("Nikita", "Loriakov", "5678", True)
user2.describe_user()
user2.greet_user()
user3 = User("Boris", "Boriakov", "asdf", False)
user3.describe_user()
user3.greet_user()
# 9-4
print("number_served BEFORE: ", restaurant1.number_served)
restaurant1.number_served += 1
print("number_served AFTER: ", restaurant1.number_served)
restaurant1.set_number_served(12)
print("number_served AFTER METHOD: ", restaurant1.number_served)
# 9-5
user1.increment_login_attempts()
user1.increment_login_attempts()
print("increment_method works: ", user1.login_attempts)
user1.reset_login_attempts()
print("reset_method works: ", user1.login_attempts)
# 9-6
ice = IceCreamStand("BR", "linear kitchen")
ice.describe_flavors()
# 9-7
admin = Admin("OLga", "Boriakova", "asdf-AJdh-AKK8-La3i", True)
admin.describe_privileges()
# 9-8
admin_l = Admin("Sergei", "Boriakov", "asdf-AMdh-AKK8-La3i", True)
admin_l.privileges.show_privileges_l()
# 9-10
from my_restaurant import Myrestaurant

restaurant11 = Myrestaurant("Lunasole", "U-shaped kitchen")
restaurant11.describe_restaurant()
# 9-14
die1 = Die()
print(die1.roll_die())
die2 = Die(220)
print(die2.roll_die())