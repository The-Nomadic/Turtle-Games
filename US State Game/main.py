import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(answer_state)

# import turtle
# import pandas
#
# ALIGN = "center"
# FONT = ('Courier', 8, 'normal')
# i = 0
# score = 0
#
# screen = turtle.Screen()
# screen.title("U.S. States Game")
# img = "blank_states_img.gif"
# turtle.addshape(img)
# turtle.shape(img)
#
# data_file = pandas.read_csv("50_states.csv")
# states = data_file['state']
#
# while i < len(states): answer_state = screen.textinput(title=f"{score}/{len(states)} States Correct",
# prompt="What's another state's name? ")
#
#     i += 1
#     for state in states:
#         if answer_state.lower() == state.lower():
#             score += 1
#             loc = data_file[data_file.state == state]
#             x = int(loc['x'].iloc[0])
#             y = int(loc['y'].iloc[0])
#
#             name = turtle.Turtle()
#             name.penup()
#             name.hideturtle()
#             name.goto(x, y)
#             name.write(f"{state}", align=ALIGN, font=FONT)
#
# screen.exitonclick()
