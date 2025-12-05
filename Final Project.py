import random

# Generates menu for the game

def mainMenuC4():
    print("Welcome to Connect 4!")
    print("Option 1: 2-Player Game")
    print("Option 2: Play Computer")
    print("Option 3: Load Saved Games")
    print("Option 4: Start Custom Game")

    playerChoice = input("Choose an option. Type 1, 2, 3 or 4.\n")

# Checks users choice and lets them make choices about the game.

    try:

        # Plays classic connect4

        if playerChoice == str(1):
            playConnect()


        #Plays classic connect4 against computer

        elif playerChoice == str(2):
            playConnect(computer=True)


        # Loads save file

        elif playerChoice == str(3):
             print("Choose a save file.")
             print("Save file 1")
             print("Save file 2")
             print("Save file 3")
             saveFile = input("Type 1, 2 or 3.")

             savedTurn = int(loadSavedTurn(saveFile))
             savedBoard = list(loadSavedBoard(saveFile))
             ifComputer = bool(loadIfComputer(saveFile))

             playConnect(computer=ifComputer, isSave=True, inputTurn=savedTurn, inputBoard=savedBoard)


        # Allows player to modify board size. Can play in 2-player mode or against computer.

        elif playerChoice == str(4):
            print("Option 1: 2-Player")
            print("Option 2: Play computer")
            playerChoiceComputer = input("Please type 1 or 2.")

            if playerChoiceComputer == str(1):
                ifComputer = False

            elif playerChoiceComputer == str(2):
                ifComputer = True

            print("Choose number of columns (5-9) and rows (5-9)")
            choiceCols = int(input("Columns: "))
            choiceRows= int(input("Rows: "))

            if choiceCols not in range(5, 9):
                print("Please choose number in range 5 - 9.")
                mainMenuC4()

            elif choiceRows not in range(5, 9):
                print("Please choose number in range 5 - 9.")
                mainMenuC4()

            playConnect(computer=ifComputer, cols=choiceCols, rows=choiceRows)

    except:
        print("There was an error.")
        mainMenuC4()


# Loads the turn number from the save file so game resumes on correct turn.

def loadSavedTurn(saveFile):
    try:
        with open("savefile" + str(saveFile) + ".txt", "r") as file:
            savedGame = file.readlines()
            turnNumber = savedGame[0]
            return turnNumber

    except:
        print("Error loading file.")


# Loads whether the saved game was 2-player or 1-player.

def loadIfComputer(saveFile):
    try:
        with open("savefile" + str(saveFile) + ".txt", "r") as file:
            savedGame = file.readlines()
            computer = savedGame[1]
            return computer

    except:
        print("Error loading file.")


# Loads the saved board. Have not been able to work out how to convert board back into 2D list from string.

def loadSavedBoard(saveFile):
    try:
        with open("savefile" + str(saveFile) + ".txt", "r") as file:
            savedGame = file.readlines()
            savedBoard = savedGame[2]
            return savedBoard

    except:
        print("Error loading file.")

# Function to play the game.

def playConnect(computer=False, isSave=False, cols=7, rows=6, inputTurn=1, inputBoard=[]):

# Sets up default parameters.

    endGame = False
    turnNumber = 1
    board = [[0 for x in range(cols)] for y in range(rows)]


# If the game is loading a save file this if statement allows saved data to be loaded.

    if isSave == True:
        turnNumber = inputTurn
        board = inputBoard


# A function to print the board onto the console. It is called after every turn.

    def printBoard():

        for i in board:
            print(i)


# Function to check if the last move has resulted in either player winning the game.

    def checkWin(player):

        for i in range(cols - 1):
            for j in range(rows - 4):

                if board[i][j] == player and board[i][j + 1] == player and board[i][j + 2] == player and board[i][j + 3] == player:
                    print("Player " + str(player) + " has won!")
                    return True

        for i in range(cols - 4):
            for j in range(rows - 1):
                if board[i][j] == player and board[i + 1][j] == player and board[i + 2][j] == player and board[i + 3][j] == player:
                    print("Player " + str(player) + " has won!")
                    return True

        for i in range(cols - 4):
            for j in range(rows - 4):
                if board[i][j] == player and board[i + 1][j + 1] == player and board[i + 2][j + 2] == player and board[i + 3][j + 3] == player:
                    print("Player " + str(player) + " has won!")
                    return True

        for i in range(cols - 4):
            for j in range(2, rows - 1):
                if board[i][j] == player and board[i + 1][j - 1] == player and board[i + 2][j - 2] == player and board[i + 3][j - 3] == player:
                    print("Player " + str(player) + " has won!")
                    return True


# Function which allows player to save the game. This is an option after each turn (except computer's).

    def saveGame():

        print("Choose save file.")
        print("Save File 1\nSave File 2\nSave File 3\n")
        fileChoice = input("Please type 1, 2 or 3 to save game.\n"
                            "This will overwrite any previous saves.\n"
                            "Press any other button to return to menu.\n")

        if fileChoice == str(1):
            try:
                with open("savefile1.txt", "w") as file:
                    file.write(str(turnNumber) + "\n")

                    if computer == True:
                        file.write("True\n")

                    elif computer == False:
                        file.write("False\n")

                    file.write(str(board))

            except:
                print("Could not save game.")

        elif fileChoice == str(2):
            try:
                with open("savefile2.txt", "w") as file:
                    file.write(str(turnNumber) + "\n")

                    if computer == True:
                        file.write("True\n")

                    elif computer == False:
                        file.write("False\n")

                    file.write(str(board))

            except:
                print("Could not save game.")

        elif fileChoice == str(3):
            try:
                with open("savefile3.txt", "w") as file:
                    file.write(str(turnNumber) + "\n")

                    if computer == True:
                        file.write("True\n")

                    elif computer == False:
                        file.write("False\n")

                        file.write(str(board))


            except:
                print("Could not save game.")
                mainMenuC4()


# While loop which keeps the game in play until someone has won or the game has been saved.

    while endGame == False:

        printBoard()

        if checkWin(1):
            endGame = True
            mainMenuC4()
            continue

        if checkWin(2):
            endGame = True
            mainMenuC4()
            continue

# On even turns the computer or player 2 have a turn.

        if (turnNumber % 2) == 0 and computer == False:

            print("It is player two's go.")
            print("Pick a column to put a counter in.")

            try:
                player2Choice = input("Choose between 1 and " + str(cols) + " or press 'e' to exit.\n")
                count = 0

                if player2Choice.lower() == "e":
                    endGame = True
                    saveGame()
                    mainMenuC4()
                    continue

                # Checks if the column chosen is full before allowing a counter to be placed there.
                # If a counter is placed the board is updated.

                for i in board:

                    if board[count][int(player2Choice) - 1] == 0:
                        count += 1

                if count != 0:

                    board[count - 1][int(player2Choice) - 1] = 2
                    turnNumber += 1

                elif count == 0:

                    print("This column is full.")
                    print("Please select another.")

            except:
                print("Error.")
                print("Please type a number between 1 and " + str(cols) + " or press 'e' to exit.")


        # If the game is a one-player this section allows the computer to take a turn.

        elif (turnNumber % 2) == 0 and computer == True:

            count = 0
            computerChoice = random.randint(1, cols)

            for i in board:

                if board[count][int(computerChoice) - 1] == 0:
                    count += 1

            if count == 0:
                continue

            elif count !=0:
                board[count - 1][int(computerChoice) - 1] = 2
                turnNumber += 1


        # Player one has their turn on odd turns, therefore they go first.

        elif (turnNumber % 2) != 0:

            print("It is player one's go.")
            print("Pick a column to put a counter in.")

            try:
                player1Choice = input("Choose between 1 and " + str(cols) + " or press 'e' to exit.\n")
                count = 0

                if player1Choice.lower() == "e":
                    endGame = True
                    saveGame()
                    mainMenuC4()
                    continue

                for i in board:

                    if board[count][int(player1Choice) - 1] == 0:
                        count += 1

                if count != 0:

                    board[count - 1][int(player1Choice) - 1] = 1
                    turnNumber += 1

                elif count == 0:

                    print("This column is full.")
                    print("Please select another.")

            except:
                print("Error.")
                print("Please type a number between 1 and " + str(cols) + " or press 's' to save.")


# Calls the main menu which is the beginning of the game.

mainMenuC4()
