class Myrestaurant(object):
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