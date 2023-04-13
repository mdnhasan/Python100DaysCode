import turtle


is_run=True
while is_run:
    my_screen = turtle.Screen()
    my_screen.bgcolor('black')
    tname =turtle.Turtle()
    tname.shape('turtle')
    tname.color('red','white')
    tname.circle(30)
    tname.forward(200)
    tname.left (90)
    tname.circle(30)
    tname.forward(200)
    tname.left (90)
    tname.circle(30)
    tname.forward(200)
    tname.left (90)
    tname.circle(30)
    tname.forward(200)
    tname.left (90)
    tname.shapesize(2)

#tname.color('yellow')
    print(tname)


    my_screen=turtle.Screen()
    my_screen.bgcolor('coral')
    #print(my_screen.canvheight)
    my_screen.exitonclick()