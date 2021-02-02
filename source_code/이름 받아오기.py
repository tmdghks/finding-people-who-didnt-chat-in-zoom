import time
with open('chat.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    people_list = []
    i = 0
    for i in range(len(lines)):
        if i % 2 == 0:
            people_list.append(lines[i].split('님이')[0])
with open('people list.txt', 'w', encoding='utf-8') as file:
    file.write(str(people_list))
print(people_list)
time.sleep(100)