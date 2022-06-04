from art import logo
from art import vs
from game_data import data
from random import randint
import random
from replit import clear
def format(choice):
    if choice == choice_a:
      return f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}"
    if choice == choice_b:
      return f"Against B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}"  
def ask_user(ask,choice_a,choice_b):  
    if ask=='A':
      return choice_a['follower_count']
    else:
      return choice_b['follower_count']
def check_answer(ask, follower_count_a, follower_count_b):
    if follower_count_a>follower_count_b:
      return ask =='A'
    else:
      return ask=='B'
#Display art
print(logo)
score=0
#Generate a random account from the game_data
choice_b=random.choice(data)
game_continous=True
while game_continous:  
  choice_a=choice_b
  choice_b=random.choice(data)
  if choice_a==choice_b:
    choice_b=random.choice(data) 
  #Format the account data into printable format
  print(format(choice_a))
  print(vs)
  print(format(choice_b))
  #Ask user for a guess
  ask = input("Who has more followers? Type 'A'  or 'B': ")
  #print(ask_user(ask,choice_a,choice_b))
  #Check if user is correct
  follower_count_a=choice_a["follower_count"]
  follower_count_b=choice_b["follower_count"]
  is_correct= check_answer(ask, follower_count_a, follower_count_b)  
  #Give feedback to user
  clear()
  if is_correct:
    score+=1
    print(f"You are right! Current score: {score}.")
  else:
    game_continous=False
    print(f"Sorry, that is wrong. Final score: {score}. ")