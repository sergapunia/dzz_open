def cook_book(file=r'recipes.txt'):
    with open(file,'rt', encoding='utf-8') as f:
        recipe_book = {}
        for line in f:
            dish = line.strip()
            ingredients_count=int(f.readline().strip())
            ingredients = []
            for i in range(ingredients_count):
                ing = f.readline().strip()
                ingridient_name, quantity, measure =ing.split(' | ')
                ingredients.append({
                    'ingridient_name': ingridient_name,
                    'quantity': quantity,
                    'measure': measure
                })
            f.readline()
            recipe_book[dish]=ingredients
        return recipe_book

print(f'ДЗ-1 \n{cook_book()}\n-------------')
'''
В рецепт Утки по-пекински добавлены яйца,чтобы проверить работоспособность следующей функции
'''
def get_shop_list_by_dishes(dishes, person_count):
    ingredients={}
    for i in dishes:
        if i in cook_book():
            for g in cook_book()[i]:
                ingredient_name = g['ingridient_name']
                ingredient_quantity = int(g['quantity'])*person_count
                ingredient_measure = g['measure']
                for j in ingredients:
                    if j==ingredient_name:
                        ingredient_quantity += int(ingredients[j]['quantity'])
                quanti = {
                    'measure': ingredient_measure,
                    'quantity': ingredient_quantity
                }
                ingredients[ingredient_name]=quanti
    return ingredients

print(f"ДЗ-2 \n{get_shop_list_by_dishes(['Омлет','Утка по-пекински'],2)}\n----------")
def file_sorted(files):
    for file in files:
        with open(file,'r', encoding='utf-8') as f:
            list=[]
            for line in f:
                list.append(line.strip())
                quantity=len(list)
                name=file
        with open('sorted.txt','a',encoding='utf-8') as sort:
            sort.write(f'{name}\n')
            sort.write(f'{quantity}\n')
            for j in list:
                sort.write(f'{j}\n')

file_sorted(['1.txt','2.txt','3.txt'])
print('ДЗ - 3')
with open('sorted.txt','r',encoding='utf-8') as f:
    for line in f:
        print(line.strip())