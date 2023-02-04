from turtle import Turtle as T, Screen as S

def create_shape(obj, sides):
    for _ in range(sides):
        obj.forward(100)
        obj.left(360/sides)
    obj.left()

def create_dash(obj):
    for _ in range (5):
        obj.forward(10)
        obj.color("white")
        obj.forward(10)
        obj.color("black")

leonardo = T()
leonardo.shape("classic")

create_dash(leonardo)

# num_sides = int(input("How many sides: "))

create_shape(leonardo, num_sides)



screen = S()
screen.exitonclick()