import random


lst = [0, 1, 2]
def choose(user, computer):
        if user == computer:
            print(" Tied") # مساوی
    
# Option    > rock, paper, scissors

# random.randint()
user = int(input("0 > Rock | 1 > Paper | 2 > Scissors: "))
computer = random.randint(0, 2)


def game(user):
    if user == Rock:   # Rock
        if computer == Rock:
            print(" Tied") # مساوی
            print("Computer Choose Rock")
        elif computer == Paper:
            print(" Lost")
            print("Computer Choose Paper")
        else:
            print(" Win")
            print("Computer Choose Scissors")
    elif user == Paper: # Paper
        if computer == Rock:
            print(" Win") # مساوی
            print("Computer Choose Rock")
        elif computer == Paper:
            print(" Tied")
            print("Computer Choose Paper")
        else:
            print(" Loss")
            print("Computer Choose Scissors")
    else:   # Scissors
        if computer == Rock:
            print(" Lost") # مساوی
            print("Computer Choose Rock")
        elif computer == Paper:
            print(" Win")
            print("Computer Choose Paper")
        else:
            print(" Tied")
            print("Computer Choose Scissors")


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



print(outcomes.get((user, computer)))