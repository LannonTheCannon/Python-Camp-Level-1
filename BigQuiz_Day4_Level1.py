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
lives = 7


q19 = ['In the disney movie UP what is the dog\'s name?',
      'kevin', 'blue', 'spot', 'dug', 4]
q18 = ['Which animal lives almost entirely on bamboo?',
      'sabertooth tiger', 'grasshopper', 'panda', 'water snake', 3]
q17 = ['What is the largest bird? ',
      'DoDo', 'Ostrich', 'Bald Eagle', 'Emperor Penguin', 2]
q16 = ['Who lives at Number 4 Privet Drive?',
      'Hagrid', 'Ron Weasely', 'Hermione', 'Harry Potter', 4]
q15 = ['Dylan\'s favorite anime is: ?',
      'fuschia flowergarden', 'violet evergarden', 'purple fruitgarden', 'magenta backyard-garden', 2]
q14 = ["What does concatenation mean?",
       "Adding strings only", "Adding numbers only", "subtracting strings", "multiplying strings", 1]
q13 = ["What does an f-string literal use inside quotations?",
       "{}", "[]", "()", "||", 1]
q12 = ["Instead of using an f-string literal, you can also use:",
       "bracket notation", "asterisk notation", "comma notation", "parentheses notation", 3]
q11 = ["What is the main distinction between a string and a boolean:",
       "strings are surrounded by quotation marks", "They turn different colors", "one has 4 or 5 letters", "spelling", 1]
q10 = ["When downloading Python IDLE, you have two windows.The Script editor and:",
       "Chevrons", "Calculator", "Shell", "User Interface", 3]
q9 = ["Variables are: ",
       "integers", "data types", "containers", "delicious", 3]
q8 = ["The python shell is used to test out: ",
       "One liners", "multiple lines of code", "back-end code", "APIs", 1]
q7 = ['The python shell can be regarded as the: ',
       'a protective exterior', 'something turtle snakes use', 'the input', 'the output', 4]
q6 = ['True and False are examples of',
       'Boolean', 'String', 'Float', 'Integers', 1]
q5 = ['A string will always turn to which color?',
      'white', 'purple', 'orange', 'green', 4]
q4 = ['The operator that gives us the remainder: ',
      '+', '//', '%', '*', 3]
q3 = ['The operator that gives us the remainder: ',
      'floor division', 'modulo', 'exponent', 'square root', 2]
q2 = ['The operator that divides a number but only returns an integer is',
      'subtraction', 'addition', 'division', 'floor division', 4]
q1 = ['The print statement and input statement turn to which color?',
      'white', 'purple', 'green', 'orange', 2]

questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11,
             q12, q13, q14, q15, q16, q17, q18, q19]

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
