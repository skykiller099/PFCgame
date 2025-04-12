import random
from languages import *
computer_choice = random.choice(['rock', 'paper', 'scissors'])
user_choice = input("Entre ton choix (rock , paper , scissors) ").lower()
if user_choice not in ['rock', 'paper', 'scissors' , 'r', 'p', 's','pierre', 'papier', 'ciseaux']:
    if user_choice in ['pierre', 'papier', 'ciseaux']:
        user_choice = user_choice.replace('pierre', 'rock').replace('papier', 'paper').replace('ciseaux', 'scissors')
    elif user_choice in ['r', 'p', 's']:
        if user_choice == 'r':
            user_choice = 'rock'
        elif user_choice == 'p':
            user_choice = 'paper'
        elif user_choice == 's':
            user_choice = 'scissors'
    print("Choix invalide. Veuillez entrer 'rock', 'paper' ou 'scissors'.")
else:
    print(f"Choix de l'ordinateur: {computer_choice}")
    if user_choice == computer_choice:
        print("Match Nul")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("Tu as gagné!")
    else:
        print("Tu as perdu!")