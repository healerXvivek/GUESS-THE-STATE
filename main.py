import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
state = turtle.Turtle()
state.hideturtle()

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()


def write_state(k, x, y):
    state.hideturtle()
    state.penup()
    state.goto(x - 15, y)
    state.write(f"{k}", font=("Calibri", 6, "bold"))


n = 0
game_is_on = True
guessed_states = []
while game_is_on:
    answer = screen.textinput(title=f" {n}/50  Guess The State", prompt="What's the other state ")
    answer = answer.title()
    if answer == "Exit":
        missing_states = [state for state in state_list if state not in guessed_states]
        break
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        game_is_on = False
    if answer in state_list:
        guessed_states.append(answer)
        n += 1
        st = data[data.state == answer]
        write_state(answer, int(st.x), int(st.y))
        if n == 50:
            game_is_on = False
