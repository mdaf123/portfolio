print("Choose between rock, paper or scissors.")
print(" ")
x=""
while x not in ["rock","paper", "scissors"]:
  x=input("Rock, paper, scissors say shoot!: \n \n").lower()
  print(" ")
  if x not in ["rock", "paper", "scissors"]:
    print("Choose between rock, paper or scissors you dumbass")
    print(" ")

import random


k = random.randint(0,2)
y=["rock","paper","scissors"]
choice= y[k]
print(choice)
print(" ")
if x=="rock" and choice=="paper":
  print("You Lose!")
if x=="rock" and choice=="rock":
  print("Draw!")
if x=="rock" and choice=="scissors":
  print("You Win!")
if x=="paper" and choice=="paper":
  print("Draw!")
if x=="paper" and choice=="rock":
  print("You Win!")
if x=="paper" and choice=="scissors":
  print("You Lose!")
if x=="scissors" and choice=="paper":
  print("You Win!")
if x=="scissors" and choice=="rock":
  print("You Lose!")
if x=="scissors" and choice=="scissors":
  print("Draw!")
print(" ")
l=""
while l not in ["no","yes"]:
  l=input("Do you want to play again?: \n \n").lower()
  print(" ")
  if l not in ["no","yes"]:
    print("This is a yes or no question dumbass")
    print(" ")
if l=="no":
  print("ok buck")
while l=="yes":
  print("Choose between rock, paper or scissors.")
  print(" ")
  x=""
  while x not in ["rock","paper", "scissors"]:
    x=input("Rock, paper, scissors say shoot!: \n \n")
    print(" ")
    if x not in ["rock", "paper", "scissors"]:
      print("Choose between rock, paper or scissors you dumbass")
      print(" ")

  import random


  k = random.randint(0,2)
  y=["rock","paper","scissors"]
  choice= y[k]
  print(choice)
  print(" ")
  if x=="rock" and choice=="paper":
    print("You Lose!")
  if x=="rock" and choice=="rock":
    print("Draw!")
  if x=="rock" and choice=="scissors":
    print("You Win!")
  if x=="paper" and choice=="paper":
    print("Draw!")
  if x=="paper" and choice=="rock":
    print("You Win!")
  if x=="paper" and choice=="scissors":
    print("You Lose!")
  if x=="scissors" and choice=="paper":
    print("You Win!")
  if x=="scissors" and choice=="rock":
    print("You Lose!")
  if x=="scissors" and choice=="scissors":
    print("Draw!")
  print(" ")
  l=""
  while l not in ["no","yes"]:
    l=input("Do you want to play again?: \n \n").lower()
    print(" ")
    if l not in ["no","yes"]:
      print("This is a yes or no question dumbass")
      print(" ")
  if l=="no":
    print("ok buck")