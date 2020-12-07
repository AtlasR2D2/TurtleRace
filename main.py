from turtle import Turtle, Screen
import random

SCREEN_HEIGHT = 400
SCREEN_WIDTH = 500
SCREEN_EDGE_BUFFER_WIDTH = 20
SCREEN_EDGE_BUFFER_HEIGHT = 30

STARTING_LINE = -SCREEN_WIDTH/2 + SCREEN_EDGE_BUFFER_WIDTH
FINISH_LINE = SCREEN_WIDTH/2 - SCREEN_EDGE_BUFFER_WIDTH
TOP_OF_SCREEN = SCREEN_HEIGHT/2 - SCREEN_EDGE_BUFFER_HEIGHT
BOTTOM_OF_SCREEN = -SCREEN_HEIGHT/2 + SCREEN_EDGE_BUFFER_HEIGHT
SCREEN_HEIGHT_NET = TOP_OF_SCREEN - BOTTOM_OF_SCREEN

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = [Turtle(shape="turtle") for color_x in colors]
for i in range(len(colors)):
    turtles[i].color(colors[i])

#Buffer between each turtle
TURTLE_BUFFER = SCREEN_HEIGHT_NET/(len(turtles)-1)

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

user_bet = screen.textinput(title="Make your bet",prompt=f"Which turtle will with the race? Enter a color {colors}: ")


def move_forwards(turtle_x):
    random.seed()
    forward_movement = random.randint(0, 10)
    if turtle_x.xcor()+forward_movement > FINISH_LINE:
        turtle_x.forward(FINISH_LINE - turtle_x.xcor())
    else:
        turtle_x.forward(forward_movement)


# Move the turtles to the starting position
for i in range(len(turtles)):
    turtles[i].penup()
    turtles[i].goto(x=STARTING_LINE, y=BOTTOM_OF_SCREEN + (i * TURTLE_BUFFER))


# Let the race begin!!!
if len(user_bet) != 0:
    Race_Over = False
else:
    Race_Over = True
while not Race_Over:
    random.seed()
    # Choose random turtle
    i = random.randint(0, len(turtles)-1)
    move_forwards(turtles[i])

    if turtles[i].xcor() == FINISH_LINE:
        Race_Over = True
        winning_color = turtles[i].pencolor()
        if winning_color == user_bet:
            print(f"Race is over! {colors[i]} won. You guessed correctly!! :)")
        else:
            print(f"Race is over! {colors[i]} won. You guessed incorrectly!! :)")

screen.exitonclick()
