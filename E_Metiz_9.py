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
print("increment_method works: ",user1.login_attempts)
user1.reset_login_attempts()
print("reset_method works: ",user1.login_attempts)