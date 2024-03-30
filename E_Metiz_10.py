# 10-1
# with open('text_files/имя_файла.txt') as file_object:
file_name_1 = '10_text_files/learning_python.txt'

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