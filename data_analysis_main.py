import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()
gussed_state = []
while len(gussed_state) < 50:
    answer_state = screen.textinput(title=f"{len(gussed_state)}/50 correct Guess the state" ,prompt="What's another state's name").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_state:
            if state not in gussed_state:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_learn.csv")
        break
    if answer_state in all_state:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x) ,int(state_data.y))
        t.write(answer_state)
