''' 
Today we will learn about:
- Review:
    - what's a string
    - input()
    - how to make commands
- Dictionaries and accessing a peice of the element
- adding variables to commands 
- looping with input
- += operator
'''

# What is a string?
#   Answer: characters that are inbetween "" or ''
#           A string can have any length 

students1 = {
    "Feranmi": 10,
    "Sam": 9,
    "Lorenzo": 4,
    "Dvimedh": 6
    }

students_points_class2 = {
    "Aria": 10,
    "Yuvan": 8,
    "Ryan": 7,
    "Isaac": -20
    }

# this will just find the student and add the points
def add_points(student, points):
    students_points_class2[student] += int(points)
    # students_points_class2[student] = students_points_class2[student] + points
    # we can also use students1[student] += int(points)

def subtract_points(student, points):
    students_points_class2[student] -= int(points)

def display_scores():
    print(students_points_class2)


display_scores()
while True:

    student_name = input("Enter the good student's name: ")
    student_points = input("Enter the points earned: ")
    add_points(student_name, student_points)
    display_scores()
