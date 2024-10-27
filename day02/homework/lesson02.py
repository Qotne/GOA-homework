import turtle

def draw_rectangle(color, width, height):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

def draw_tower(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    draw_rectangle("gray", 40, 80)

    # Draw the tower roof
    turtle.fillcolor("darkgray")
    turtle.begin_fill()
    turtle.goto(x - 20, y + 80)
    turtle.goto(x + 60, y + 80)
    turtle.goto(x + 40, y)
    turtle.end_fill()

def draw_castle():
    # Draw the main building
    turtle.penup()
    turtle.goto(-50, -100)
    turtle.pendown()
    draw_rectangle("lightgray", 100, 60)

    # Draw the roof of the main building
    turtle.fillcolor("darkgray")
    turtle.begin_fill()
    turtle.goto(-70, -40)
    turtle.goto(50, -40)
    turtle.goto(50, -100)
    turtle.goto(-50, -100)
    turtle.end_fill()

    # Draw towers
    draw_tower(-90, -100)
    draw_tower(50, -100)

def main():
    turtle.speed(2)
    draw_castle()
    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
