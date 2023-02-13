import random
names_string = input("Give me everybody's name, seperated as a comma.\n: ")
names = names_string.split(", ")
print(names)
random_name = random.choice(names)
print(f"{random_name} is going to buy the meal today!")