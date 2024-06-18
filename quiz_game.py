class quiz_game:

    def game(self):
        while True:
            try:
                game_status = input("Do you want to start the game Y/N: ")
                if game_status == "Y":
                    print("Okay you can start the game have fun")
                    break


                elif game_status == "N":
                    print("Okay thank you for using this code")
                    break

            except Exception as e:
                print("Invalid input")

    def getQuestions(self):
        point = 0
        while True:
            try:
                question = input("Is a integer a decimal number Y/N: ")
                if question == "N":
                    print("This is correct")
                    point += 1


                elif question == "Y":
                    print("This is incorrect")
                    point -= 1

                else:
                    print("Invalid input please type in Y or N to continue")
                    continue


                question = input("Do you add items to a list with pop or append: ")
                if question == "append":
                    print("This is correct")
                    point += 1


                elif question == "pop":
                    print("This is incorrect")
                    point -= 1

                else:
                    print("Invalid input please type in pop or append to continue")
                    continue


                question = input("Do you get a user input with print or input: ")
                if question == "input":
                    print("This is correct")
                    point += 1


                elif question == "print":
                    print("This is incorrect")
                    point -= 1

                else:
                    print("Invalid input please type in input or print to continue")
                    continue

                question = input("Do you end a while loop with break or continue: ")
                if question == "break":
                    print("This is correct")
                    point += 1


                elif question == "continue":
                    print("This is incorrect")
                    point -= 1

                else:
                    print("Invalid input please type in break or continue to continue")
                    continue


                question = input("Do you create a GUI Window with Tkinter Y/N: ")
                if question == "Y":
                    print("This is correct")
                    point += 1


                elif question == "N":
                    print("This is incorrect")
                    point -= 1

                else:
                    print("Invalid input please type in Y or N to continue")
                    continue

                print(f"You have: {point} points well done")

                break

            except Exception as e:
                print("Invalid input please follow the instructions to continue")
                continue


quiz = quiz_game()
quiz.game()
quiz.getQuestions()