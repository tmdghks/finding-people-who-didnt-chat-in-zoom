import time
with open('chat.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    chatted_people_list = []
    i = 0
    for i in range(len(lines)):
        if i % 2 == 0:
            chatted_people_list.append(lines[i].split('님이')[0])
    print(chatted_people_list)
with open('people list.txt', 'r', encoding='utf-8') as file:
    people_list = file.readlines()[0].split("', '")
    people_list[0] = people_list[0][2:]
    people_list[-1] = people_list[-1][:-2]
    print(people_list)
for i in range(len(chatted_people_list)):
    try:
        people_list.remove(chatted_people_list[i])
    except:
        pass
print(people_list)
time.sleep(100)