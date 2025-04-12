import random
computer_choice = random.choice(['rock', 'paper', 'scissors'])
user_choice = input("Entre ton choix (rock , paper , scissors) ").lower()
if user_choice not in ['rock', 'paper', 'scissors']:
    print("Choix invalide. Veuillez entrer 'rock', 'paper' ou 'scissors'.")
else:
    print(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print("Match Nul")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("Tu as gagné!")
    else:
        print("Tu as perdu!")