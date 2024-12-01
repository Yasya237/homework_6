#1. Дан словник виду {str: int} (ключи - строки, значення - цілі числа).

my_dict = {"pencil": 5,
           "pen": 3,
           "notebook": 8,
           "bag": 1}

# - Створити список ключів цього словнику

keys_list = []
for key in my_dict:
    keys_list.append(key)
print(keys_list)

# - Створити список значень цього словнику

values_list = []
for values in my_dict.values():
    values_list.append(values)
print(values_list)

# - Порахувати суму числових значень цього словнику

count = 0
for values in my_dict.values():
    count += values
print(count)
#####################################################

# 2. Дан словник виду {str: str} (ключи - строки, значення - строки)

my_dict = {"name": "Sara",
          "city": "New York",
          "job": "travel agent",
           "grandma": "Sara"}

# - Створити список з унікальних значень цього словнику

uniques = []
for unique_values in my_dict.values():
    if unique_values not in uniques:
        uniques.append(unique_values)
print(uniques)

# - Створити строку з унікальних значень цього словнику. У якості роздільника взяти символ ___

my_str = "___".join(uniques)
print(my_str)
#####################################################

# 3. Дано два списка строк однакової довжини. Створити словник з ключами
# із першого списка і значеннями із другого.

keys_list = ["name", "city","job"]
values_list = ["Sara", "New York","travel agent"]
my_dict = {}
for idx in range(len(keys_list)):
    my_dict[keys_list[idx]] = values_list[idx]
print(my_dict)
#####################################################

# 4. Дано два списка строк однакової довжини. Строки в першому списку строки можуть бути однакові.

keys_list = ["a", "b", "c", "a", "a", "c"]
values_list = [1, 2, 3, 4, 5, 6]

# Створити словник з ключами із першого списка і значеннями із другого.
# У разі повторення ключа - створити ключ з додатковим числовим суфіксом, що відповідає номеру ключа.
# Приклад:
# Дано: ["a", "b", "c", "a", "a", "c"] та [1, 2, 3, 4, 5, 6]
# Очікуванний результат: {"a": 1, "b": 2, "c": 3, "a2": 4, "a3": 5, "c2": 6}

my_dict = {}
key_count = {}
for idx in range(len(keys_list)):
    key = keys_list[idx]
    if key in key_count:
        key_count[key] += 1
        key = key + str(key_count[key])
    else:
        key_count[key] = 1
    my_dict[key] = values_list[idx]
print(my_dict)
