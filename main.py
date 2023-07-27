import turtle
import pandas
import csv
screen = turtle.Screen()
screen.title("P.H. States Game")
image = "ph-states-game/phil_states.gif"
screen.setup(1000, 1000)

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('ph-states-game/50_states_phil.csv')

writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

holder = True
correct_guess = []
title = "Guess the State"

while len(correct_guess) < 81:
    initial_holder = True

    while initial_holder == True:
        answer_state = screen.textinput(title=title, prompt="Name a state of our dear nation.")
        final_answer = data[data['state'] == answer_state.title()]
        if not final_answer.empty:
            initial_holder = False

    correct_guess.append(answer_state)
    final_answer_x = final_answer['x']
    final_answer_y = final_answer['y']
    writer.goto(int(final_answer_x), int(final_answer_y))
    writer.write(answer_state.title())
    title = f"{len(correct_guess)}/81 States Correct"


turtle.exitonclick()
