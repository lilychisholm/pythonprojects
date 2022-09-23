scores = raw_input("Please input student scores: ").split()
highest = 0
for score in scores:
    if highest < score:
        highest = score
print("The highest score is " + str(highest))