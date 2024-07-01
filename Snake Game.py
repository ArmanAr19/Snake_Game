from tkinter import *
from random import randint
import os
import sys
class Snake:
    def __init__(self):
        self.body_size = BODY_SIZE
        self.coordinates = []
        self.squares = []
        
        for i in range(0, BODY_SIZE):
            self.coordinates.append([0, 0])
        for x, y in self.coordinates:
            square = canvas.create_oval(x, y, x+SPACE_SIZE, y+SPACE_SIZE,
                                              fill=SNAKE_COLOR, tag='snake')
            self.squares.append(square)
class Food:
    def __init__(self):
        x = randint(0, (GAME_WIDTH // SPACE_SIZE)-1) * SPACE_SIZE
        y = randint(0, (GAME_HEIGHT // SPACE_SIZE)-1) * SPACE_SIZE
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x+SPACE_SIZE, y+SPACE_SIZE,
                                              fill=FOOD_COLOR, tag='food')
def moving(snake, food):
    x, y = snake.coordinates[0]
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    snake.coordinates.insert(0, [x, y])
    square = canvas.create_oval(x, y, x+SPACE_SIZE, y+SPACE_SIZE,
                                      fill= SNAKE_COLOR)
    snake.squares.insert(0, square)
    while x < 0 or y < 0 or x > (GAME_WIDTH - SPACE_SIZE) or y > (GAME_HEIGHT - SPACE_SIZE):
        
        if x < 0 :
            snake.coordinates.insert(0, [GAME_WIDTH, y])
            square = canvas.create_oval(GAME_WIDTH, y, GAME_WIDTH+SPACE_SIZE, y+SPACE_SIZE,
                                      fill= SNAKE_COLOR)
            snake.squares.insert(0, square)
            del snake.coordinates[-1]
            canvas.delete(snake.squares[-1])
            del snake.squares[-1]
            break
        if x > (GAME_WIDTH-SPACE_SIZE):
            snake.coordinates.insert(0, [0, y])
            square = canvas.create_oval(0, y, 0+SPACE_SIZE, y+SPACE_SIZE,
                                      fill= SNAKE_COLOR)
            snake.squares.insert(0, square)
            del snake.coordinates[-1]
            canvas.delete(snake.squares[-1])
            del snake.squares[-1]
            break
        if y < 0:
            snake.coordinates.insert(0, [x, GAME_HEIGHT])
            square = canvas.create_oval(x, GAME_HEIGHT, x+SPACE_SIZE, GAME_HEIGHT+SPACE_SIZE,
                                      fill= SNAKE_COLOR)
            snake.squares.insert(0, square)
            del snake.coordinates[-1]
            canvas.delete(snake.squares[-1])
            del snake.squares[-1]
            break    
        if y > (GAME_HEIGHT-SPACE_SIZE):
            snake.coordinates.insert(0, [x, 0])
            square = canvas.create_oval(x, 0, x+SPACE_SIZE, 0+SPACE_SIZE,
                                      fill= SNAKE_COLOR)
            snake.squares.insert(0, square)
            del snake.coordinates[-1]
            canvas.delete(snake.squares[-1])
            del snake.squares[-1]
            break
    if x == food.coordinates[0] and y == food.coordinates[1]:
        if food.coordinates in snake.coordinates:
            global score
            score += 1
            label.config(text= f'score: {score}')
            canvas.delete('food')
            food = Food()
            while food.coordinates in snake.coordinates:
                canvas.delete('food')
                food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    
    if check_game_over():
        game_over()
    else:
        window.after(SLOWNESS, moving, snake, food)
        
    


def change_direction(new_dir):
    global direction
    if new_dir == 'left':
        if direction != 'right':
            direction = new_dir
    if new_dir == 'right':
        if direction != 'left':
            direction = new_dir
    if new_dir == 'up':
        if direction != 'down':
            direction = new_dir
    if new_dir == 'down':
        if direction != 'up':
            direction = new_dir        
def check_game_over():
    x , y = snake.coordinates[0]
    for head in snake.coordinates[1:]:
        if x == head[0] and y == head[1]:
            return True
    return False
def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2,canvas.winfo_height()/ 2,font=("Roboto Condensed", 50),
                        text= "GAME OVER!", fill='red', tag= 'gameover')
def restart_program():
    path = sys.executable
    os.execl(path, path, *sys.argv)

GAME_WIDTH = 550
GAME_HEIGHT = 550
SPACE_SIZE = 25
BODY_SIZE = 2
SLOWNESS = 170
TIMER = 10
BACKGROUND_COLOR = 'black'
SNAKE_COLOR = '#5DFF00'
FOOD_COLOR = 'red'
direction = 'down'
score = 0

window = Tk()
window.title('Snake game')
window.resizable(False, False)
label = Label(window, text=f"score: {score}",font=('Roboto Condensed', 30))
label.pack()
canvas = Canvas(window, bg=BACKGROUND_COLOR,width=GAME_WIDTH, height=GAME_HEIGHT)
canvas.pack()
restart = Button(window, text='RESTART', fg= 'red',command=restart_program)
restart.pack()
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width / 2)-(window_width / 2))
y = int((screen_height / 2)-(window_height / 2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.bind("<Left>", lambda event: change_direction('left'))
window.bind("<Right>", lambda event: change_direction('right'))
window.bind("<Up>", lambda event: change_direction('up'))
window.bind("<Down>", lambda event: change_direction('down'))
snake = Snake()
food = Food()
moving(snake, food)
window.mainloop() 