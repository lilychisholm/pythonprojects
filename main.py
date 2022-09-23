print("Welcome to the Love Calculator!")
name1 = raw_input("What is your full name?: ")
name2 = raw_input("What is their full name?: ")
name1lower = name1.lower()
name2lower = name2.lower()

digit1 = name1lower.count("t") + name1lower.count("r") + name1lower.count("u") + name1lower.count("e") + name2lower.count("t") + name2lower.count("r") + name2lower.count("u") + name2lower.count("e")
digit2 = name1lower.count("l") + name1lower.count("o") + name1lower.count("v") + name1lower.count("e") + name2lower.count("l") + name2lower.count("o") + name2lower.count("v") + name2lower.count("e")
score = str(digit1) + str(digit2)

if int(score) < 10 or int(score) > 90:
    print("Your score is " + str(score) + ", you go together like coke and mentos.")
elif int(score) > 40 and int(score) < 50:
    print("Your score is " + str(score) + ". You are alright together.")
else:
    print("Your score is " + str(score) + ".")