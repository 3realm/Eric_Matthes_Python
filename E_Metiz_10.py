# 10-1
# with open('text_files/имя_файла.txt') as file_object:
file_name_1 = '10_text_files/learning_python.txt'
file_name_2 = '10_text_files/guest.txt'
file_name_3 = '10_text_files/answer.txt'

with open(file_name_1) as file_object_1:
    contents = file_object_1.read()
    print(contents.rstrip())

with open(file_name_1) as file_object_1:
    for line in file_object_1:
        print(line)

string = ''
with open(file_name_1) as file_object_1:
    lines = file_object_1.readlines()
    for line in lines:
        string += line.strip()

print(string)
# 10-2
change_string = 'C'
with open(file_name_1) as file_object_2:
    lines = file_object_2.readlines()
    for line in lines:
        if 'Python' in line:
            print(line.replace('Python', change_string))
# 10-3
# string_name = input('Input your name: ') + "\n"
# with open(file_name_2, 'a') as file_object_3:
#     file_object_3.write(string_name)
# 10-4
# 10-5
stop_flag = '1'
while stop_flag != '0':
    string_reason = input('Input your reason: ') + "\n"
    with open(file_name_3, 'a') as file_object_3:
        file_object_3.write(string_reason)
    stop_flag = input('Input 0 for EXIT')