import turtle
import time

lines = turtle.clone()

lines.penup()

lines.hideturtle()

lines.goto(0,300)
lines.pendown()
lines.pencolor("white")
turtle.bgcolor('black')
lines.write("Save The T (Turtle)", align = 'center', font=("Arial", 30, "normal"))
lines.penup()
lines.goto(0,300)
lines.pendown()
lines.goto(400,300)
lines.goto(400,-300)
lines.goto(-400,-300)
lines.goto(-400,300)
lines.goto(0,300)
lines.penup()


UP_ARROW = "Up" #Make sure you pay attention to upper and lower 
LEFT_ARROW = "Left" #Pay attention to upper and lower case
RIGHT_ARROW = "Right" #Pay attention to upper and lower case
TIME_STEP = 100 #Update snake position after this many 
                #milliseconds
SPACEBAR = "space" # Careful, it's not supposed to be capitalized!



UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400


def left():
    global direction #snake direction is global (same everywhere)
    direction=LEFT #Change direction to up
     #Update the snake drawing <- remember me later
    print("You pressed the left key!")
    
turtle.onkeypress(left, LEFT_ARROW) # Create listener for up key


def right():
    global direction #snake direction is global (same everywhere)
    direction=RIGHT#Change direction to up
     #Update the snake drawing <- remember me later
    print("You pressed the right key!")


def move_turtle():
    my_pos = turtle.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]


    
    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    
    elif direction==UP:
        snake.goto(x_pos, y_pos + SQUARE_SIZE )
        print("You moved up!")

    


