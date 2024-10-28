#1 Задача

with open('recipes.txt') as file:
    cook_book = {}
    for i in file:
        recipe_name = i.strip()
        ingredients_count = file.readline()
        ingredients = []
        for p in range(int(ingredients_count)):
            recipe = file.readline().strip().split(' | ')
            product, quantity, word = recipe
            ingredients.append({'ingredient name': product, 'quantity': quantity, 'measure': word})
        file.readline()
        cook_book[recipe_name] = ingredients
# print(cook_book)


#2 Задача

def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for consist in cook_book[dish]:
                if consist['ingredient name'] in result:
                    result[consist['ingredient name']]['quantity'] += consist['quantity'] * person_count
                else:
                    result[consist['ingredient name']] = {'measure': consist['measure'], 'quantity': (int(consist['quantity']) * person_count)}
        else:
            print('Такого блюда нет в книге')
    # print(result)


get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 3)

#3 Задача

count = 0
count_list = []
mlist = ('1.txt', '2.txt', '3.txt')
f_list = []
for t in mlist:
    with open(t) as f:
        for line in f:
            count += 1
    count_list.append(count)
    count = 0
print(count_list)
print(sorted(count_list))


with open('main.txt', 'w') as f:
    f.write('1.txt'.read())







# def rewriting(file_for_writing: str, base_path, location):
#     files = []
#     for i in list(os.listdir(os.path.join(base_path, location))):
#         files.append([acounting(os.path.join(base_path, location, i)), os.path.join(base_path, location, i), i])
#     for file_from_list in sorted(files):
#         opening_files = open(file_for_writing, 'a')
#         opening_files.write(f'{file_from_list[2]}\n')
#         opening_files.write(f'{file_from_list[0]}\n')
#         with open(file_from_list[1], 'r',encoding='utf-8') as file:
#             counting = 1
#             for line in file:
#                 opening_files.write(f'строка № {counting} в файле {file_from_list[2]} : {line}')
#                 counting += 1
#         opening_files.write(f'\n')
#         opening_files.close()
#
#
# file_for_writing = os.path.abspath('\\Users\\йролджэ\\Desktop\\Python\\1.txt')
# base_path = os.getcwd()
# location = os.path.abspath('\\Users\\йролджэ\\Desktop\\Python')
# rewriting(file_for_writing, base_path, location)