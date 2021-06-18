import turtle
import pandas

FONT = ("Courier", 8, "normal")
# Configuring screen to display image and title
screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("U.S. States Games")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

# Creating turtle for writing states name
turtle = turtle.Turtle()
turtle.penup()
turtle.hideturtle()

# Reading from CSV file using pandas
data = pandas.read_csv("50_states.csv")
states = data["state"].tolist()

score = 0
playing = True
prompt = "What's another states name?"
answered_states = []
while playing:
    answer_states = screen.textinput(title="Guess the states", prompt=prompt).title()
    for state in states:
        if answer_states == state:
            turtle.goto(int(data[data.state == state]["x"]), int(data[data.state == state]["y"]))
            turtle.write(state, align="center", font=FONT)
            score += 1
            prompt = f"{score}/50 States correct"
            answered_states.append(answer_states)
        elif answer_states == "Exit":
            playing = False
            missing_states = []
            for ind_state in states:
                if ind_state not in answer_states:
                    missing_states.append(ind_state)
            missing_dict = {"states": missing_states}
            missing_data = pandas.DataFrame(missing_dict)
            missing_data.to_csv("./savefiles/missing_states")
        else:
            continue
    if score == 50:
        playing = False

# Code for getting co-ordinates on clicking on screen
# def get_mouse_click_coor(x, y):
#     print(x, y)
#  turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop() It is similar to exitonclick() to exit the screen but it dosen't exit even on clicking and loops
# printing the screen
