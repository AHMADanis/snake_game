import turtle
import csv
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
img = "states.gif"
screen.addshape(img)
turtle.shape(img)

data = pd.read_csv('50_states.csv')
all_states = data.state.to_list()
print(all_states)

guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 States Correct', prompt='What is another state name?')
    answer_state = answer_state.title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("state_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)





