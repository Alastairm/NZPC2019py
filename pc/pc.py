import sys
lines = []
for _line in sys.stdin:
    stripped = _line.strip()
    if not stripped: break
    lines.append(stripped)

recipe_name = lines.pop(0)
num_ingredients = int(lines.pop(0))

def process_ingredients(from_list:list, to_dict:list):
    ingredients = [a.strip() for a in from_list]
    for x in ingredients:
        x = x.split(',')
        x = [xi.strip() for xi in x]
        name, units, amount = x
        amount = float(amount)
        if units in ['kg', 'l']:
            to_dict[name] = amount * 1000
        elif units in ['g', 'ml', 'x']:
            to_dict[name] = amount
        else:
            raise ValueError("Unrecognised unit '{units}'.")

def check_ingredients(need, have):
    ingredients = list(need.keys())
    need_more = []
    for x in ingredients:
        if have[x] < need[x]:
            need_more.append(x)
    need_more.sort()
    return need_more

ingredients_need = {}
process_ingredients(lines[:num_ingredients], ingredients_need)

ingredients_have = {}
process_ingredients(lines[num_ingredients:], ingredients_have)

need_more = check_ingredients(ingredients_need, ingredients_have)

if len(need_more) == 0:
    print(f"You may make your {recipe_name}.")
else:
    print(f"You may NOT make your {recipe_name}.")
    print(f"You need {', '.join(need_more)}.")
