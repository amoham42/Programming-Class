import turtle
import random

# Set up the screen
wn = turtle.Screen()
wn.title("Turtle Cube Avoidance Game")
wn.bgcolor("white")
wn.setup(width=600, height=600)

# Define a list of colors for the turtle to change to
colors = ["blue", "purple", "orange", "pink", "yellow", "brown", "cyan"]

# Create the player turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.pensize(4)  # Set the size of the pen
player.penup()
player.speed(0)
player.goto(random.randint(-280, 280), random.randint(-280, 280))
player.setheading(random.choice([45, 135, 225, 315]))  # Set initial diagonal direction
player.pendown()  # Start drawing

# Create red cubes
num_red_cubes = 10
red_cubes = []

for _ in range(num_red_cubes):
    cube = turtle.Turtle()
    cube.shape("square")
    cube.color("red")
    cube.penup()
    cube.speed(0)
    x = random.randint(-280, 280)
    y = random.randint(-280, 280)
    cube.goto(x, y)
    red_cubes.append(cube)

# Create green cubes
num_green_cubes = 5
green_cubes = []

for _ in range(num_green_cubes):
    cube = turtle.Turtle()
    cube.shapesize(1.5, 1.5)
    cube.shape("square")
    cube.color("green")
    cube.penup()
    cube.speed(0)
    x = random.randint(-280, 280)
    y = random.randint(-280, 280)
    cube.goto(x, y)
    green_cubes.append(cube)

# Collision avoidance counter
collision_avoidance = 0

# Function to adjust heading after border collision
def adjust_heading():
    new_heading = (player.heading() + 180) % 360
    player.setheading(new_heading - 10)
    player.color(random.choice(colors))

# Function to move the turtle
def move_turtle():
    global collision_avoidance

    player.forward(15)
    x, y = player.position()

    if collision_avoidance > 0:
        # Skip collision check
        collision_avoidance -= 1
    else:
        # Check for collision with window border and change direction
        if x > 280 or x < -280 or y > 280 or y < -280:
            adjust_heading()
            collision_avoidance = 4

        # Check for near collision with red cubes and change direction
        for cube in red_cubes:
            if player.distance(cube) < 30:
                new_heading = random.choice([45, 135, 225, 315])
                player.setheading(new_heading)
                collision_avoidance = 4
                player.color(random.choice(colors))  # Change to a random color

        # Check for collision with green cubes and "eat" them
        for cube in green_cubes:
            if player.distance(cube) < 20:
                cube.hideturtle()
                green_cubes.remove(cube)
                player.color("green")  # Change back to green after eating a green cube

# Main game loop
def game_loop():
    move_turtle()
    wn.ontimer(game_loop, 1)

# Start the game loop
game_loop()

wn.mainloop()
