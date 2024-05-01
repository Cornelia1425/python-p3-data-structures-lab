spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names =[food["name"] for food in spicy_foods]
    return names

def get_spiciest_foods(spicy_foods):
    # spiciest_food=spicy_foods[0]
    # for food in spicy_foods:
    #     print(food["heat_level"])
    #     if food["heat_level"] > spiciest_food["heat_level"]:
    #         spiciest_food = food
    # elif:
    #     do nothing

    # spiciest_food=[]
    # for food in spicy_foods:
    #     if food["heat_level"]>5:
    #         spiciest_food.append(food)

    spiciest_food = [food for food in spicy_foods if food["heat_level"]>5]
    return spiciest_food

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print ( food["name"] + " (" + food["cuisine"] + ") | Heat Level: " + "🌶"* food["heat_level"])

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    # spicy_food_by_cuisine = ["cuisine: " + food["cuisine"] + "heat_level: " + food["heat_level"] + "name: " + food["name"] for food in spicy_foods if food["cuisine"] == cuisine]
    # return spicy_food_by_cuisine

    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food


    # for food in spicy_foods:
    #     print ("cuisine: " + food["cuisine"] + "heat_level: " + food["heat_level"] + "name: " + food["name"])


def print_spiciest_foods(spicy_foods):
       for food in spicy_foods:
            if food["heat_level"]>5:
                print ( food["name"] + " (" + food["cuisine"] + ") | Heat Level: " + "🌶"* food["heat_level"])

def get_average_heat_level(spicy_foods):
    heat_level_list = [food["heat_level"] for food in spicy_foods]
    get_average_heat_level = sum(heat_level_list)/len(heat_level_list)
    return get_average_heat_level

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

