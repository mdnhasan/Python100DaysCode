import turtle

# Creating turtle
t = turtle.Turtle()

turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)

while (True):
    for i in range(7):
        for colors in ["red", "blue", "magenta", "green", "yellow", "white","indigo"]:
            turtle.color(colors)
            turtle.circle(100)
            turtle.left(10)

turtle.hideturtle()
turtle.mainloop()


# import turtle
#
# # Creating turtle
# t = turtle.Turtle()
# s = turtle.Screen()
# s.bgcolor("black")
# t.pencolor("red")
#
# a = 0
# b = 0
# t.speed(0)
# t.penup()
# t.goto(0, 200)
# t.pendown()
# while (True):
#     t.forward(a)
#     t.right(b)
#     a += 3
#     b += 1
#     if b == 210:
#         break
#     t.hideturtle()
#
# turtle.done()



