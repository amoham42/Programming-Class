import random
# List & Array

int1 = 1
int2 = 2
int3 = 3

string = "Abdul"
string1 = "Maroof"
string2 = "Omid"

# user = int(input("0 > Rock | 1 > Paper | 2 > Scissors: "))
# computer = random.randint(0, 2)
Rock = 0  
Paper = 1
Scissors = 2

outcomes = {
    (Rock, Rock): 'Tied',
    (Paper, Paper): 'Tied',
    (Scissors, Scissors): 'Tied',
    (Rock, Paper): 'Lost',
    (Paper, Rock): 'Win',
    (Paper, Scissors): 'Lost'
}

# print(outcomes.get((user, computer)))

lst = []

#       0,   1,   2,   3 
lst2 = ["a", "b", "c", "d"]

str = "This is a program"
separate = str.split(" ") # جدا کردن
print(separate)
print(separate[1])
# print(lst1[0])

# function
def play(myList, i):
    print(myList[int(i)])

#      0, 1, 2, 3,  4,  5   
lst = [1, 2, 3, 10, 30, 40]
#               -3  -2  -1
# play(lst, -4)
# play(lst2, -3)
# play(lst, -2)
# play(lst, -1)

#function
#list
# .split()
# [::]

# for loops while loops
# dictionary
