from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def rigth():
    tim.right(10)

def left():
    tim.left(10)

screen.listen()
screen.onkey(key='w' , fun=move_forwards)
screen.onkey(key='a' , fun=rigth)
screen.onkey(key='d' , fun=left)
screen.exitonclick()