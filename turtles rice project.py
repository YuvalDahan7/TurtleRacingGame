from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title= "Turtles race", prompt= "Which turtle will win the rice? Enter a color: ")
colors = ["red", "blue", "green", "purple"]
y_position = [150, 50, -50, -150]
all_turtles = []

race_is_on = False

for turtle_index in range(0, 4):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-240, y=(y_position[turtle_index]))
    all_turtles.append(new_turtle)

if user_bet:
    race_is_on = True

while race_is_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                race_is_on = False
                print(f"you've won! the {winner_color} is the winner.")
            else:
                race_is_on = False
                print(f"you've lost! the {winner_color} is the winner.")

        turtle.forward(random.randint(0,10))


screen.exitonclick()