import random
names = raw_input("Give me everybody's names, separated by a comma. ")
names = names.split(", ")

length = len(names)

choice = random.randint(0, length - 1)
person = names[choice]
print(person + " is going to buy the meal today.")