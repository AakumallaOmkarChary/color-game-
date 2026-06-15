import turtle as turtle_module
import random
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
turtle_module.colormode(255)
color_list = [(242, 239, 235), (244, 240, 242), (237, 242, 239), (234, 236, 240),
               (201, 162, 111), (144, 78, 51), (61, 102, 130), (166, 151, 43), (221, 202, 137),
               (134, 163, 181), (133, 33, 21), (71, 36, 28), (203, 91, 72), (54, 117, 85), (143, 179, 150),
               (232, 174, 162), (26, 53, 73), (108, 85, 96), (18, 94, 67), (54, 40, 45), (163, 145, 159),
               (90, 150, 117), (181, 204, 172), (91, 142, 153), (19, 87, 92), (18, 68, 47), (74, 68, 47), (38, 63, 94), (119, 34, 39), (97, 129, 161)]
tim.setheading(225)
tim.fd(300)

tim.setheading(0)
num_0f_dots = 100
for dot_count in range(1, num_0f_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.fd(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.fd(50)
        tim.setheading(180)
        tim.fd(500)
        tim.setheading(0)




screen = turtle_module.Screen()
screen.exitonclick()
