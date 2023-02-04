import random
from turtle import Turtle as T, Screen as S

color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

screen = S()
screen.colormode(255)

leonardo = T()
leonardo.shape("classic")
leonardo.speed(10)

leonardo.penup()

leonardo.setheading(225)
leonardo.forward(300)
leonardo.setheading(0)

for i in range(1,101):
    leonardo.dot(20, random.choice(color_list))
    leonardo.forward(50)

    if i % 10 == 0:
        leonardo.setheading(90)
        leonardo.forward(50)
        leonardo.setheading(180)
        leonardo.forward(500)
        leonardo.setheading(0)





screen.exitonclick()