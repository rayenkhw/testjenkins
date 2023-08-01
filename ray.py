import turtle

def draw_circle(x, y, radius, color):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_rectangle(x, y, width, height, color):
    turtle.penup()
    turtle.goto(x - width/2, y - height/2)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

def draw_mouse():
    turtle.speed(1)
    
    # Draw the body of the mouse
    draw_circle(0, 0, 40, "gray")
    
    # Draw the ears
    draw_circle(-25, 80, 15, "gray")
    draw_circle(25, 80, 15, "gray")
    
    # Draw the eyes
    draw_circle(-15, 20, 7, "black")
    draw_circle(15, 20, 7, "black")
    
    # Draw the nose
    draw_circle(0, 0, 5, "pink")
    
    # Draw the tail
    turtle.penup()
    turtle.goto(50, -40)
    turtle.pendown()
    turtle.goto(100, -60)

    # Hide the turtle cursor
    turtle.hideturtle()

if __name__ == "__main__":
    turtle.setup(400, 400)  # Set the window size
    draw_mouse()
    turtle.done()

