# simple drawing app
# click and drag on the canvas to draw. Pick a color, or clear everthing

import tkinter as tk

current_color = "black"

def draw(event):
    x = event.x
    y = event.y
    size = 4
    canvas.create_oval(x - size, y - size, x + size, y + size, fill = current_color, outline = current_color)

def set_color(color):
    global current_color
    current_color = color

def clear_canvas():
    canvas.delete("all")

window = tk.Tk()
window.title("My Drawing App")
window.geometry("500x450")

canvas = tk.Canvas(window, width = 480, height = 250, bg = "white")
canvas.pack(pady = 10)
canvas.bind("<B1-Motion>", draw)

button_frame = tk.Frame(window)
button_frame.pack()

black_button = tk.Button(button_frame, text = "Black", command = lambda: set_color("black"))
black_button.grid(row = 0, column = 0, padx = 5)

red_button = tk.Button(button_frame, text = "Red", command = lambda: set_color("red"))
red_button.grid(row = 0, column = 1, padx = 5)

blue_button = tk.Button(button_frame, text = "Blue", command = lambda: set_color("blue"))
blue_button.grid(row = 0, column = 2, padx = 5)

green_button = tk.Button(button_frame, text = "Green", command = lambda: set_color("green"))
green_button.grid(row = 0, column = 3, padx = 5)

clear_button = tk.Button(button_frame, text = "clear", command = clear_canvas)
clear_button.grid(row = 0, column = 4, padx = 5)

window.mainloop()


