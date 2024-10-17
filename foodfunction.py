FILEPATH = 'meals.txt'

def get_meals(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        meals_local = file_local.readlines()
        return meals_local

def write_meals(meals_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(meals_arg)