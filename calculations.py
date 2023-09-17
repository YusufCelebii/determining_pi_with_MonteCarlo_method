import random
import turtle
import math

#Area of the circle is (2r)²= 4r²
#Area of the circle is  π r²

# Area of the circle / Area of the circle =  4/π
# So, The ratio of the number of all points to the points inside the circle should approximate 4/π




# You can determine faster without virtualization with using monteCarlo func.
def monteCarlo(n):
    dots_of_circle = 0
    dots_of_square = 0

    for i in range(n):
        x = random.uniform(-300, 300)
        y = random.uniform(-300, 300)

        distance = math.sqrt(x ** 2 + y ** 2)

        if distance <= 300:
            dots_of_circle += 1

        dots_of_square += 1

    return 4 * (dots_of_circle / dots_of_square)

# Firstly, Drawing circle and square with area func.
def area():
    turtle.tracer(0)
    # drawing circle
    tostos = turtle.Turtle()
    tostos.pensize(2)
    tostos.speed(0)
    tostos.penup()
    tostos.goto(0, -300)
    tostos.pendown()
    tostos.circle(300)
    tostos.penup()
    tostos.forward(-300)
    tostos.pendown()
    # drawing square
    for i in range(4):
        tostos.forward(600)
        tostos.left(90)
    turtle.update()

# Generate random dots and determine pi value approximately
def random_dots(number_of_dots,frequency):
    turtle.tracer(0)
    dotdot=turtle.Turtle()
    dotdot.speed(0)
    blue_counter=0
    red_counter=0
    iterate=0
    for i in  range(number_of_dots):
        x_coordinate=random.uniform(-300,300)
        y_coordinate=random.uniform(-300,300)
        dotdot.penup()
        dotdot.goto(x_coordinate,y_coordinate)
        dotdot.pendown()

        if dotdot.distance(0,0) <= 300:
            dotdot.pencolor("red")
            dotdot.dot(4)
            red_counter+=1
        else:
            dotdot.pencolor("blue")
            dotdot.dot(4)
            blue_counter+=1

        if red_counter!=0:
            pi = 4 / ((red_counter + blue_counter) / red_counter)
            if i%frequency==0:   # Call the print_result() func.
                print_result(pi,i/1000)
    iterate += 1



# Function to print the results
def print_result(pi, iterate):

    turtle.tracer(0)
    tostos = turtle.Turtle()
    tostos.hideturtle()
    tostos.speed(0)
    tostos.penup()
    tostos.goto(-440, +350)

    # Clear the previous result (This clears only the necessary area)
    tostos.color("white")
    tostos.begin_fill()
    for i in range(2):
        tostos.forward(900)
        tostos.left(90)
        tostos.forward(50)
        tostos.left(90)
    tostos.end_fill()
    tostos.color("black")

    # Print the currently calculated value in the cleared area
    tostos.pendown()
    tostos.write(f"π is approximately: {pi} ", font=("Arial", 20, "bold"))

    # Print the current iteration count in the upper right corner
    tosbik = turtle.Turtle()
    tosbik.hideturtle()
    tosbik.speed(0)
    tosbik.penup()
    tosbik.goto(460, +350)
    tosbik.pendown()
    tosbik.write(f"Iteration {iterate} K  ", font=("Arial", 20, "bold"), align="right")
    turtle.update()

