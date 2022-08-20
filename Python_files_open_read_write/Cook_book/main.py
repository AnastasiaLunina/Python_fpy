from pprint import pprint

cook_book = {}


def get_cook_book():
    with open('cook_book.txt', encoding='UTF-8') as f:
        for line in f:
            name = line.strip()
            cook_book[name] = []
            f.readline()
            i = 0
            while i == 0:
                ingredients = f.readline()
                if len(ingredients) > 1:
                    ingredients = ingredients.strip()
                    ingredients = ingredients.split(' | ')
                    in_cook_book = \
                        {'ingredient_name': ingredients[0], 'quantity': ingredients[1], 'measure': ingredients[2]}
                    cook_book[name].append(in_cook_book)
                else:
                    i += 1
    pprint(cook_book)


def get_ingredients(dishes, person_count):
    dish_list = []
    ingredients = {}
    for name in dishes:
        for key, value in cook_book.items():
            if name == key:
                for i in value:
                    dish_list.append(i['ingredient_name'])
                    if len(set(dish_list)) == len(dish_list):
                        ingredients[i['ingredient_name']] = \
                            {'quantity': int(i['quantity']) * person_count, 'measure': i['measure']}
                    else:
                        difference = len(dish_list) - len(set(dish_list))
                        ingredients[i['ingredient_name']] = \
                            {'quantity': int(i['quantity']) * person_count * (difference + 1), 'measure': i['measure']}
    for key, value in ingredients.items():
        print(key, value)


get_cook_book()
print()
get_ingredients(['Запеченный картофель', 'Омлет'], 2)
