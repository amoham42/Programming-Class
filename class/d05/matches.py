from typing import Match

colors_list = ["blue", "          purple     ", "orange", "red"]

int = 1

# for color in colors:
#     print(color)
#     color = color.split(' ')
#     print(color)

def blue_colored(value):
    global int
    print('it is blue')
    print(value)
    int += 1
    print(int)

def purple_colored(value):
    global int
    print('it is purple52349122330i')
    print(value + value.strip())
    int += 5
    print(int)

def orange_colored(value):
    global int
    print('it is orange' + str(int * 50))
    print(value + value.strip())
    int += 7
    print(int)

def colors(value):
    match value:
        case 'blue':
            blue_colored(value)
        case 'purple':
            purple_colored(value)
        case 'orange':
            orange_colored(value)
        case _:
            print("color does not exist")


for i in colors_list:
    colors(i)

