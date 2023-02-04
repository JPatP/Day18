from turtle import Turtle as T, Screen as S
import random

#TODO#3 Change color each loop

screen = S()
screen.colormode(255)

leonardo = T()
leonardo.width(1)
leonardo.shape("classic")
leonardo.speed(0)


def set_random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color


heading = 0

#TODO#2 Loop the circle while changing its left degree until it completes 1 full rotation
for _ in range(72):

    # Draw a circle
    leonardo.circle(100)

    # Get the current heading and print to console
    current_heading = leonardo.heading()
    print("Before add heading is: ", current_heading)

    # After first circle is drawn, update the heading
    heading = heading + 5
    leonardo.setheading(heading)

    # Check if heading was updated
    print("After add Heading is: ", leonardo.heading())

    # Update the color
    leonardo.pencolor(set_random_color())


screen.exitonclick()