# 8-12
def create_sandwich(*info: str) -> None:
    if info:
        print("\nMaking a sandwich with the following toppings:")
        for count in info:
            print('-', count)
    else:
        print('\nError in the order')


create_sandwich("1", "2", "3")
create_sandwich("1", "2", "3", "4", "5")
create_sandwich()


# 8-13
def build_profile(first: str, last: str, **user_info) -> dict[str, str]:
    profile = {'first_name': first, 'last_name': last}
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
solution = build_profile('Nikita', 'Boria4kov', age='20', gender='male', height='1,85')
print(solution)


# 8-14
def create_auto(name: str, producer: str, **auto_info):
    profile = {'name': name, 'producer': producer}
    for key, value in auto_info.items():
        profile[key] = value
    return profile


crete_auto = create_auto('Opel', 'Opel Automobile GmbH', color='blue', weels=4, tow_package=True)
print(crete_auto)

# 8-15
# import имя_модуля
# from имя_модуля import имя_функции
# from имя_модуля import имя_функции as псевдоним
# import имя_модуля as псевдоним
# from имя_модуля import *
import printing_functions

printing_functions.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
