import turtle
import pandas

data = pandas.read_csv('50_states.csv')
data.to_dict()
screen = turtle.Screen()
screen.title('US States Game')
image = "blank_states_img.gif"
screen.addshape(image)

map = turtle.Turtle()
map.shape(image)


def get_mouse_click_coord(x, y):
	print(x, y)


turtle.onscreenclick(get_mouse_click_coord)
states = data.state.tolist()
correct_guesses = []
guessed = 0
while len(correct_guesses) < 50:
	state_answer = turtle.textinput(f"{guessed}/50 guessed", "Type in the next state".title())

	if state_answer in states:
		guessed += 1
		correct_guesses.append(state_answer)
		turtle_answer = turtle.Turtle()
		turtle_answer.hideturtle()
		turtle_answer.penup()
		state_data = data
		answer_x = data[data.state == state_answer].x
		answer_y = data[data.state == state_answer].y
		turtle_answer.goto(int(answer_x), int(answer_y))
		turtle_answer.write(state_answer, align="Center")
	elif state_answer == 'exit':
		missing_states = []
		for s in states:
			if s not in correct_guesses:
				missing_states.append(s)
		print(missing_states)
		df = pandas.DataFrame(missing_states, columns=None)
		df.to_csv('list.csv',)
		break

screen.exitonclick()

# states to csv:
# for s in data.states:
# 	if s not in correct_guesses:
# 		data.s.to_csv()