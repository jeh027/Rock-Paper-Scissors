# Jesse Huang's Project 1 / Programming Assignment Module 6 / Intro to Programming

""" This program allows the user to pick either rock, paper, or scissors while the computer randomly does the same. The possibilities
    of this game: rock breaks scissors, paper covers rock, scissors cuts paper, or tie if both the bot and the player pick the same
    choice. """

import random

player_score = 0
bot_score = 0

repeat = True

while repeat == True:
    """ The interpreter takes in both the player's response as well as the bot's randomly generated response and processes who wins.
        If the game is tied, neither the player or the bot will recieve a point; however, if either the bot or the player wins, a point
        will be added to their score. """
    
    def interpreter(hum, bot_choice):
        global player_score
        global bot_score         
        #ALL TIE SITUATIONS
        if bot_choice == "Scissors" and hum == "Scissors":
            print()
            print("Result: the bot chose", bot_choice, "and you chose", hum,"; tie")
        elif bot_choice == "Rock" and hum == "Rock":
            print()
            print("Result: the bot chose", bot_choice, "and you chose", hum,"; tie")
        elif bot_choice == "Scissors" and hum == "Scissors":
            print()
            print("Result: the bot chose", bot_choice, "and you chose", hum,"; tie")
        #ROCK
        elif bot_choice == "Scissors" and hum == "Rock":
            print()
            print("Result: the bot chose", bot_choice, "and you chose", hum,"; You win!")
            player_score += 1
        elif bot_choice == "Rock" and hum == "Scissors":
            print()
            print("Result: the bot chose", bot_choice, "and you chose", hum,"; Bot wins")
            bot_score += 1
        elif bot_choice == "Rock" and hum == "Paper":
            print()
            print("Result: the bot chose", bot_choice, "and you chose", hum,"; You win!")
            player_score += 1
        elif bot_choice == "Paper" and hum == "Rock":
            print()
            print("Result: the bot chose", bot_choice, "and you chose", hum,"; Bot wins")
            bot_score += 1
        #SCISSORS
        elif bot_choice == "Scissors" and hum == "Paper":
            print()
            print("Result: the bot chose", bot_choice, "and you chose", hum,"; Bot wins")
            bot_score += 1
        elif bot_choice == "Paper" and hum == "Scissors":
            print()
            print("Result: the bot chose", bot_choice, "and you chose", hum,"; You win!")
            player_score += 1
        elif bot_choice == "Rock" and hum == "Scissors":
            print()
            print("Result: the bot chose", bot_choice, "and you chose", hum,"; Bot wins")
            bot_score += 1
        elif bot_choice == "Scissors" and hum == "Rock":
            print()
            print("Result: the bot chose", bot_choice, "and you chose", hum,"; You win!")
            player_score += 1
        #PAPER
        elif bot_choice == "Paper" and hum == "Rock":
            print()
            print("Result: the bot chose", bot_choice, "and you chose", hum,"; Bot wins")
            bot_score += 1
        elif bot_choice == "Rock" and hum == "Paper":
            print()
            print("Result: the bot chose", bot_choice, "and you chose", hum,"; You win!")
            player_score += 1
        elif bot_choice == "Scissors" and hum == "Paper":
            print()
            print("Result: the bot chose", bot_choice, "and you chose", hum,"; Bot wins")
            bot_score += 1
        elif bot_choice == "Paper" and hum == "Scissors":
            print()
            print("Result: the bot chose", bot_choice, "and you chose", hum,"; You win!")
            player_score += 1


    #Scoring system:
            
        print("")
        print("Your score: ", player_score)
        print("Bot's score: ", bot_score)
        print("")
        


    """ The bot function generates a random number from 1 to 3, each number associated with a different rock, paper, scissors
        choice and calls the interpreter function with the player's response and the bot's response in its parameters. """

    #bot input using random
    def bot(hum):
        bot_choice = random.randint(1, 3)
        if bot_choice == 1:
            bot_choice = 'Scissors'
            call = interpreter(hum, bot_choice) 
            return bot_choice
        elif bot_choice == 2:
            bot_choice = 'Rock'
            call = interpreter(hum, bot_choice)
            return bot_choice
        elif bot_choice == 3:
            bot_choice = 'Paper'
            call = interpreter(hum, bot_choice)
            return bot_choice


    """ The main function asks the player for an input of rock, paper, or scissors. """
        
    #human input
    def main():
        hum = input("Rock, Paper, Scissors: ").lower()  #ask user to enter an option
        if hum in ["rock", "r"]:                        #utilization of a list in the if ... elif ... else conditional statement 
            hum = 'Rock'
            call = bot(hum)
            return hum
        elif hum in ["paper", "p"]:
            hum = 'Paper'
            call = bot(hum)
            return hum
        elif hum in ["scissors", "scissor", "s"]:
            hum = 'Scissors'
            call = bot(hum)
            return hum
        else:
            print(hum, "is an invalid choice")

    main()        # first call




    #Insert whether the player wants to play again:

    play_again = input("Play again? [yes / no]: ").lower()
    if play_again == "yes":
        repeat = True
    elif play_again == "y":
        repeat = True
    else:
        print("The game has ended")
        print("Thank you for playing!!!")
        repeat = False

    






















    
