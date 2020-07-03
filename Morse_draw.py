# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 10:28:15 2020

@author: jbris
"""

import turtle
word = input("Type what you want coded: ")
word = word.lower()

wn = turtle.Screen()
wn.title("Morse Code")
wn.bgcolor("blue")
wn.setup(width=800, height=600)

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
start = -300
pen.goto(start,250)
pen.pendown()
#pen.write("Richard : 0  Player 2: 0", align="center", font=("Courier", 24, "normal"))

def ddot():
    pen.penup()
    pen.goto(pen.xcor()+5, pen.ycor())
    pen.pendown()
    pen.goto(pen.xcor(), pen.ycor() + 10)
    pen.penup()
    pen.goto(pen.xcor(), pen.ycor() - 10)
def ddash():
    pen.penup()
    pen.goto(pen.xcor()+5, pen.ycor())
    pen.pendown()
    pen.goto(pen.xcor()+10, pen.ycor())
def dgap():
    global start
    pen.penup()
    if pen.ycor() < -250 and start == -300: 
        start = -200
        pen.sety(290)
    if pen.ycor() < -250 and start == -200:
        start = -100
        pen.sety(290)
    if pen.ycor() < -250 and start == -100:
        start = 0
        pen.sety(290)
    if pen.ycor() < -250 and start == 0:
        start = 100
        pen.sety(290)
    if pen.ycor() < -250 and start == 100:
        start = 200
        pen.sety(290)
    pen.goto(start, pen.ycor() - 40)
    pen.pendown()

a = [1, 2]
b = [2,1,1,1]
c = [2,1,2,1]
d = [2,1,1]
e = [1]
f = [1,1,2,1]
g = [2,2,1]
h = [1,1,1,1]
I = [1,1]
j = [1,2,2,2]
k = [2,1,2]
l = [1,2,1,1]
m = [2,2]
n = [2,1]
o = [2,2,2]
p = [1,2,2,1]
q = [2,2,1,2]
r = [1,2,1]
s = [1,1,1]
t = [2]
u = [1,1,2]
v = [1,1,1,2]
w = [1,2,2]
x = [2,1,1,2]
y = [2,1,2,2]
z = [2,2,1,1]


inp = []
output = []
for i in word:
    inp.append(i)

print("Input word is: ", inp)

for letter in inp:
    if letter == "a":
        output += a
        output += [3]
    if letter == "b":
        output += b
        output += [3]
    if letter == "c":
        output += c
        output += [3]
    if letter == "d":
        output += d
        output += [3]
    if letter == "e":
        output += e
        output += [3]
    # adding in spaces
    if letter == " ":
        output += [0]
    
    if letter == "f":
        output += f
        output += [3]
    if letter == "g":
        output += g
        output += [3]
    if letter == "h":
        output += h
        output += [3]
    if letter == "i":
        output += I
        output += [3]
    if letter == "j":
        output += j
        output += [3]
    if letter == "k":
        output += k
        output += [3]
    if letter == "l":
        output += l
        output += [3]
    if letter == "m":
        output += m
        output += [3]
    if letter == "n":
        output += n
        output += [3]
    if letter == "o":
        output += o
        output += [3]
    if letter == "p":
        output += p
        output += [3]
    if letter == "q":
        output += q
        output += [3]
    if letter == "r":
        output += r
        output += [3]
    if letter == "s":
        output += s
        output += [3]
    if letter == "t":
        output += t
        output += [3]
    if letter == "u":
        output += u
        output += [3]
    if letter == "v":
        output += v
        output += [3]
    if letter == "w":
        output += w
        output += [3]
    if letter == "x":
        output += x
        output += [3]
    if letter == "y":
        output += y
        output += [3]
    if letter == "z":
        output += z
        output += [3]

print("Output code in morse is: ", output)

for num in output:
    if num == 1:
        ddot()
    if num == 2:
        ddash()
    if num == 3:
        dgap()
        
while True:
    wn.update()
    