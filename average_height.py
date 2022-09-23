heights = raw_input("Input a list of student heights, separated by spaces: ").split()
for height in range(0, len(heights)):
    heights[height] = int(heights[height])
print(heights)

total_height = 0
for height in heights:
    total_height += height

students = 0
for student in heights:
    students += 1

average = total_height/students
print("The average height is " + str(average))