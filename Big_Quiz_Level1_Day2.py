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

q25 = ["Why does Aiden like to do on his free time?",
 "Dancing", "Painting", "Soccer", "Play video games", 4]
q24 = ["Why does Dylan want to learn how to code?",
 "Data Science", "Web Dev", "Mom forced him to", "Game dev", 3]
q23 = ["What game does Bailey like to play?",
 "My Little Pony", "Overwatch", "Animal Crossing", "Guitar Hero", 2]
q22 = ["What did Mr.Lannon have for dinner two nights ago?",
 "Bok Choy", "Steak", "Chow Fan", "Cup Ramen", 1]
q21 = ["When we want to display more than one item in a print statement we use the",
 "comma notation", "bracket notation", "spanish notation", "parantheses", 1]
q20 = ["What can Python be used for?",
 "All Answer Choices", "Data Science", "Game Development", "Web Development", 1]
q19 = ["How many basic data types are there?",
 "4", "5", "3", "6", 1]
q18 = ["A string is always surrounded with:",
 "brackets", "asterisks", "quotation marks", "parantheses", 3]
q17 = ["An example of an integer is:",
 "5", "5.0", "6.7", "-20.5", 1]
q16 = ["When downloading Python IDLE, you have two windows.The Script editor and:",
 "Chevrons", "Calculator", "Shell", "User Interface", 3]
q15 = ["Variables are: ",
 "integers", "data types", "containers", "delicious", 3]
q14 = ["The python shell is used to test out: ",
 "One liners", "multiple lines of code", "back-end code", "APIs", 1]
q13 = ['The python shell can be regarded as the: ',
'a protective exterior','middleware','back end','front end',4]
q12 = ['We use print when we want to ____ something to the user.',
'color','display','hide','cook',2]
q11 = ['When a text is placed inside quotes we call this a',
'boolean','float','String','integer',3]
q10 = ['True and False are examples of',
'Boolean','String','Float','Integers',1]
q9 = ['A string will always turn to which color?',
'white','purple','orange','green',4]
q8 = ['When we create a variable we use the ___ symbol:',
'+','=','*','/',2]
q7 = ['The operator that gives us the remainder: ',
'+','//','%','*',3]
q6 = ['The operator that gives us the remainder: ',
'floor division','modulo','exponent','square root',2]
q5 = ['An example of a good variable name is: ',
'0_FD','Fav-Drink','FaV_DrInK','fav_drink',4]
q4 = ['The operator that divides a number but only returns an integer is',
'subtraction','addition','division','floor division',4]
q3 = ['The print statement and input statement turn to which color?',
'white','purple','green','orange',2]
q2 = ['When we ask the user to enter a value we use which function? ',
'input','print','enter','define',1]
q1 = ['When we want the user to enter an integer we use: ',
'bool(input())','input()','int(input())','float(input())',3]

questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11,
             q12, q13, q14, q15, q16, q17, q18, q19, q20,
             q21, q22, q23, q24, q25]
             
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

def update_time_left():
    global time_left
    if time_left:
        time_left = time_left - 1
    else:
        game_over()

clock.schedule_interval(update_time_left, 1.5)
pgzrun.go()
