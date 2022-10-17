import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
states_to_learn = data.state.tolist()
correct_guesses = []

while len(correct_guesses) < 50:
    answer_state = (screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="What state do you know?")).title()
    if answer_state == "Exit":
        x = pandas.Series(states_to_learn)
        x.to_csv("states_to_learn.csv")
        break
    for state in data.state:
        if state == answer_state:
            if answer_state in correct_guesses:
                pass
            else:
                correct_guesses.append(answer_state)
                states_to_learn.remove(answer_state)
                new_x = int(data[data.state == state]["x"])
                new_y = int(data[data.state == state]["y"])
                new_state = turtle.Turtle()
                new_state.penup()
                new_state.hideturtle()
                new_state.goto(new_x, new_y)
                new_state.write(state)
                print(states_to_learn)
