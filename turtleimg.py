import os
import turtle
from PIL import Image

class ImageNFT:
    def __init__(self, w, h, margin, bgcolor="blue", bdcolor="blue"):
        self.margin = margin
        self.num_rows = 0
        self.num_cols = 0
        self.cell_w = 0
        self.cell_h = 0
        self.window = turtle.Screen()
        self.window.bgcolor(bgcolor)
        self.window.setup(width=w, height=h)

        self.pen = turtle.Turtle()
        self.pen.speed(2)
        self.pen.penup()
        self.pen.color(bdcolor)
        self.pen.pensize(3)

        self.pen.goto(-w // 2 + margin, h // 2 - margin)
        self.pen.pendown()
        self.pen.goto(w // 2 - margin, h // 2 - margin)
        self.pen.goto(w // 2 - margin, -h // 2 + margin)
        self.pen.goto(-w // 2 + margin, -h // 2 + margin)
        self.pen.goto(-w // 2 + margin, h // 2 - margin)
        self.pen.penup()
        turtle.done()

    def add_image(self, path, pos):
        img_n = turtle.Turtle()
        img_n.speed(0)
        img_n.penup()
        img_n.shape(path)
        img_n.goto(pos)
        img_n.stamp()

    def add_text(self, text, xp, yp, color='black', fsize=16):
        text_pen = turtle.Turtle()
        text_pen.speed(0)
        text_pen.color(color)
        text_pen.penup()
        text_pen.goto(xp, yp)
        text_pen.write(text, align='left', font=('Arial', fsize, 'normal'))

    def draw_grid(self, lcolor="white"):
        width, height = self.window.window_width(), self.window.window_height()

        self.pen.color(lcolor)

        for c in range(self.num_cols + 1):
            self.pen.penup()
            self.pen.goto(-width // 2 + self.margin + c * self.cell_w, height // 2 - self.margin)
            self.pen.pendown()
            self.pen.goto(-width // 2 + self.margin + c * self.cell_w, -height // 2 + self.margin)

        for r in range(self.num_rows + 1):
            self.pen.penup()
            self.pen.goto(-width // 2 + self.margin, height // 2 - self.margin - r * self.cell_h)
            self.pen.pendown()
            self.pen.goto(width // 2 - self.margin, height // 2 - self.margin - r * self.cell_h)

    def paint_serie(self, serie, scolor):
        for num in serie:
            x = num % self.num_cols
            y = int(num / self.num_rows)
            self.paint_cell(x, y, scolor)

    def paint_cell(self, x, y, ccolor):
        width, height = self.window.window_width(), self.window.window_height()

        self.pen.color(ccolor)
        self.pen.penup()
        self.pen.goto(-width // 2 + self.margin + x * self.cell_w, height // 2 - self.margin - y * self.cell_h)
        self.pen.pendown()
        self.pen.begin_fill()
        for _ in range(4):
            self.pen.forward(self.cell_w)
            self.pen.right(90)
        self.pen.end_fill()

    def savejpg(self, name):
        # Get the screen size
        width, height = self.window.window_width(), self.window.window_height()

        # Create a new turtle to capture the screen
        capture_turtle = turtle.Turtle()
        capture_turtle.speed(0)
        capture_turtle.hideturtle()
        capture_turtle.penup()

        # Capture the screen and save it as a JPEG file
        capture_turtle.getscreen().getcanvas().postscript(file=f"{name}.eps")
        img = Image.open(f"{name}.eps")
        img.save(f"{name}.jpg", "JPEG")

        # Close the capture turtle and remove the temporary EPS file
        capture_turtle.clear()
        capture_turtle = None
        os.remove(f"{name}.eps")

    def set_grid(self, num_rows, num_cols):
        width, height = self.window.window_width(), self.window.window_height()
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_w = (width -2*self.margin) / num_rows
        self.cell_h = (height -2*self.margin) / num_cols

# h = 4096
# w = 4096
# cells = 100
# margin = 50

#wn = turtle.Screen()
# pen = turtle.Turtle()
# pen.speed(1)
# pen.penup()
# pen.color("black")
# pen.pensize(3)
# pen.goto(-w // 2 + margin, h // 2 - margin)
# pen.pendown()
# pen.goto(w // 2 - margin, h // 2 - margin)
# pen.goto(w // 2 - margin, -h // 2 + margin)
# pen.goto(-w // 2 + margin, -h // 2 + margin)
# pen.goto(-w // 2 + margin, h // 2 - margin)
# pen.penup()
# turtle.done()
