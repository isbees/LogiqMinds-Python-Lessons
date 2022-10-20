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
    "Feranmi": 5,
    "Sam": 1,
    "Lorrenzo": 1,
    "Dvimedh": 2
    }

students2 = {
    "Arya": 8,
    "Yuvan": 6,
    "Ryan": 5
    }

# this will just find the student and add the points
def add_points(student, points):
    students1[student] += int(points)
    # we can also use students1[student] += int(points)

def display_scores():
    print(students1)

while True:
    display_scores()

    student_name = input("Enter the good student's name: ")
    student_points = input("Enter the points earned: ")
    add_points(student_name, student_points)
