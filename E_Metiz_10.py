import json
# 10-1
# with open('text_files/имя_файла.txt') as file_object:
file_name_1 = '10_text_files/learning_python.txt'
file_name_2 = '10_text_files/guest.txt'
file_name_3 = '10_text_files/answer.txt'
file_name_4 = '10_text_files/dogs.txt'
file_name_5 = '10_text_files/cats.txt'
file_name_6 = '10_text_files/rats.txt'
file_name_7 = '10_text_files/username.json'

# with open(file_name_1) as file_object_1:
#     contents = file_object_1.read()
#     print(contents.rstrip())
#
# with open(file_name_1) as file_object_1:
#     for line in file_object_1:
#         print(line)
#
# string = ''
# with open(file_name_1) as file_object_1:
#     lines = file_object_1.readlines()
#     for line in lines:
#         string += line.strip()
#
# print(string)
# # 10-2
# change_string = 'C'
# with open(file_name_1) as file_object_2:
#     lines = file_object_2.readlines()
#     for line in lines:
#         if 'Python' in line:
#             print(line.replace('Python', change_string))
# 10-3
# string_name = input('Input your name: ') + "\n"
# with open(file_name_2, 'a') as file_object_3:
#     file_object_3.write(string_name)
# 10-4
# 10-5
# stop_flag = '1'
# while stop_flag != '0':
#     string_reason = input('Input your reason: ') + "\n"
#     with open(file_name_3, 'a') as file_object_3:
#         file_object_3.write(string_reason)
#     stop_flag = input('Input 0 for EXIT')
# 10-6
# try:
# except:
# else:
# try:
#     count_int_1 = int(input("Input new value"))
#     count_int_2 = int(input("Input other value"))
# except ValueError:
#     print('Enter integer values')
# else:
#     number_values = count_int_1 + count_int_2
#     print(number_values)
# 10-7
# stop_flag_7 = '1'
# while stop_flag_7 != '0':
#     try:
#         count_int_1 = int(input("Input new value"))
#         count_int_2 = int(input("Input other value"))
#     except ValueError:
#         pass
#         print('Enter integer values')
#     else:
#         number_values = count_int_1 + count_int_2
#         print(number_values)
#         stop_flag_7 = input("ENTER 0 for EXIT ")
# 10-8
# try:
#     with open(file_name_4) as file_object_7:
#         lines = file_object_7.read()
#         print(lines.rstrip())
#     with open(file_name_6) as file_object_8:
#         lines = file_object_8.read()
#         print(lines.rstrip())
# except FileNotFoundError:
#     print("File not found")
# print('program is working')
# # 10-9
# try:
#     with open(file_name_4) as file_object_7:
#         lines = file_object_7.read()
#         print(lines.rstrip())
#     with open(file_name_6) as file_object_8:
#         lines = file_object_8.read()
#         print(lines.rstrip())
# except FileNotFoundError:
#     pass
# print('program is working')
# 10-11; 10-12
try:
    with open(file_name_7) as file_object_12:
        user_value = json.load(file_object_12) #ERR
except FileNotFoundError:
    user_value = input("What is your favorite value? ")
    with open(file_name_7, 'w') as file_object_12:
        json.dump(user_value, file_object_12)
        print('Your favorite value is: ', user_value)
else:
    print('Your favorite value is: ', user_value)
