import turtle
import csv
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
img = "states.gif"
screen.addshape(img)
turtle.shape(img)

answer_state = screen.textinput(title='Guess the State', prompt='What is another state name?')

df = pandas.read_csv('50_states.csv')
print(df)



screen.exitonclick()