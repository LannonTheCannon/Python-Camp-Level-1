# This would be a great program to show the students
# After the for loop practice section so they have a
# Good understanding of how to apply their own skills

import pgzrun
import pygame
import random

WIDTH = 950
HEIGHT = 645

main_box = pygame.Rect(0, 0, 700, 210)
timer_box = pygame.Rect(0, 0, 110, 210)
answer_box1 = pygame.Rect(0, 0, 365, 125)
answer_box2 = pygame.Rect(0, 0, 365, 125)
answer_box3 = pygame.Rect(0, 0, 365, 125)
answer_box4 = pygame.Rect(0, 0, 365, 125)

main_box.move_ip(50, 40)
timer_box.move_ip(810, 40)
answer_box1.move_ip(50, 308)
answer_box2.move_ip(555, 308)
answer_box3.move_ip(50, 500)
answer_box4.move_ip(555, 500)

answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]
score = 0
time_left = 10
lives = 10

q32 = ["In Python, what does the term concatenation refer to?",
       "forming sentences", "adding booleans", "adding two (or more) strings", "adding integers", 3]
q31 = ["What is the hardest substance in your body?",
       "tooth enamel", "knee bone", "elbow", "skull bone", 1]
q30 = ["Which Planet in the milky way is the biggest?",
       "Saturn", "Earth", "Venus", "Jupiter", 4]
q29 = ["A Portrait is a picture of what?",
       "a cat", "a particular moment in history", "a person", "an event", 3]
q28 = ["What type of error will be thrown when you try to add a string with an int:",
       "Type Error", "Syntax Error", "Semantic Error", "Logic Error", 1]
q27 = ["Aiden told a funny knock kncok joke about:",
       "An extinct sea creature", "Sea animals", "Tanks", "Birds", 3]
q26 = ["What sport does everyone like to play except for Mr.Lannon?",
       "Snowboarding", "Tennis", "Ping Pong", "Badminton", 4]
q25 = ["Why does Aiden like to do on his free time?",
       "Dancing", "Painting", "Soccer", "Play video games", 4]
q24 = ["Why does Dylan want to learn how to code?",
       "It is really fun", "So much you can do", "Mom still forces him to", "makes a whole lot of money", 3]
q23 = ["What game does Bailey like to play?",
       "My Little Pony", "Overwatch 2", "watch grass growing", "squid game", 2]
q22 = ["What did Mr.Lannon have for dinner seven nights ago?",
       "Bok Choy", "Steak", "Chow Fan", "Cup Ramen", 1]
q21 = ["What types of books does Madeline like to read?",
       "fictional", "nonfictional", "sci-fi", "horror", 1]
q20 = ["What can Python be used for?",
       "All Answer Choices", "Data Science", "Game Development", "Web Development", 1]
q19 = ["How many basic data types are there?",
       "4", "5", "3", "6", 1]
q18 = ["A string is always surrounded with:",
       "brackets", "asterisks", "quotation marks", "parentheses", 3]
q17 = ["What is the main distinction between a string and a boolean:",
       "strings are surrounded by quotation marks", "They turn different colors", "one has 4 or 5 letters", "spelling", 1]
q16 = ["When downloading Python IDLE, you have two windows.The Script editor and:",
       "Chevrons", "Calculator", "Shell", "User Interface", 3]
q15 = ["Variables are: ",
       "integers", "data types", "containers", "delicious", 3]
q14 = ["The python shell is used to test out: ",
       "One liners", "multiple lines of code", "back-end code", "APIs", 1]
q13 = ['The python shell can be regarded as the: ',
       'a protective exterior', 'something turtle snakes use', 'the input', 'the output', 4]
q12 = ['When we take a user input value we need to use which function: ',
       'print', 'input', 'len', 'index', 2]
q11 = ['When a text (or any character) is placed inside quotes we call this a',
       'boolean', 'float', 'String', 'integer', 3]
q10 = ['True and False are examples of',
       'Boolean', 'String', 'Float', 'Integers', 1]
q9 = ['A string will always turn to which color?',
      'white', 'purple', 'orange', 'green', 4]
q8 = ['When we create a variable we use the ___ symbol:',
      '+', '=', '*', '/', 2]
q7 = ['The operator that gives us the remainder: ',
      '+', '//', '%', '*', 3]
q6 = ['The operator that gives us the remainder: ',
      'floor division', 'modulo', 'exponent', 'square root', 2]
q5 = ['An example of a good variable name is: ',
      '0_FD', 'Fav-Drink', 'FaV_DrInK', 'fav_drink', 4]
q4 = ['The operator that divides a number but only returns an integer is',
      'subtraction', 'addition', 'division', 'floor division', 4]
q3 = ['The print statement and input statement turn to which color?',
      'white', 'purple', 'green', 'orange', 2]
q2 = ['When we ask the user to enter a value we use which function? ',
      'input', 'print', 'enter', 'define', 1]
q1 = ['When we want the user to enter an integer we use: ',
      'bool(input())', 'input()', 'int(input())', 'float(input())', 3]

questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11,
             q12, q13, q14, q15, q16, q17, q18, q19, q20,
             q21, q22, q23, q24, q25, q26, q27, q28, q29, q30, q31, q32]

random.shuffle(questions)

question = questions.pop(0)


def draw():
    screen.fill("dim grey")
    screen.draw.filled_rect(main_box, "sky blue")
    screen.draw.filled_rect(timer_box, "sky blue")

    for box in answer_boxes:
        screen.draw.filled_rect(box, "orange")
        screen.draw.textbox(str(time_left), timer_box, color=("black"))
        screen.draw.textbox(question[0], main_box, color=("black"))
        index = 1

    for box in answer_boxes:
        screen.draw.textbox(question[index], box, color=("black"))
        index = index + 1


def game_over():
    global question, time_left
    message = "Game over. You got %s questions correct" % str(score)
    question = [message, "-", "-", "-", "-", 5]
    time_left = 0


def correct_answer():
    global question, score, time_left
    score = score + 1
    if questions:
        question = questions.pop(0)
        time_left = 20
    else:
        print("End of questions")
        game_over()


def on_mouse_down(pos):
    global lives
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            print("Clicked on answer " + str(index))
            if index == question[5]:
                print("You got it correct!")
                correct_answer()
            else:
                print('Sorry, Incorrect.')
                lives = lives - 1
            if lives == 0:
                game_over()
        index = index + 1
    print(lives * '🧡')


def update_time_left():
    global time_left
    if time_left:
        time_left = time_left - 1
    else:
        game_over()


clock.schedule_interval(update_time_left, 1.5)
pgzrun.go()
