# Design a N*N Tic Tac Toe game

import random

class GameBoard:
    def __init__(self, boardId: int):
        self.boardId = boardId
        self.boardSize = None
        self.board = []
    
    def setBoard(self):
        self.setBoardSize()
        self.board = [[None]* (self.boardSize) for _ in range(self.boardSize)]
    
    def setBoardSize(self):
        self.boardSize = input("Enter the size of the Tic Tac Toe Board: ")
        try:
            self.boardSize = int(self.boardSize)
            if self.boardSize < 3:
                print("Please enter a value greater than 2")
                self.setBoardSize()
            elif self.boardSize > 10:
                print("Warning! Due to memory constraints, please limit board size to 10.")
                self.setBoardSize()
        except ValueError:
            print("Please Enter a valid input")
            self.setBoardSize()

class Game:
    def __init__(self, gameId: int, player1: "Player", player2: "Player", gameBoard: "GameBoard"):
        self.gameId = gameId
        self.player1 = player1
        self.player2 = player2
        self.gameBoard = gameBoard
        self.isStarted = False
        self.isEnded = False
        self.isPlayer1 = True
    
    def printBoard(self):
        for r in self.gameBoard.board:
            for c in r:
                print(c or "-", end=" ")
            print()
    
    def startGame(self):
        self.printBoard()
        if self.isStarted:
            return "Game is already started"    
        self.isStarted = True

        movesCount = self.gameBoard.boardSize * self.gameBoard.boardSize
        self.makeMove()
        self.printBoard()
        movesCount -= 1
        winner = False
        while movesCount > 0:
            self.toggleMove()
            self.makeMove()
            self.printBoard()
            movesCount -= 1
            if self.isAnyPlayerWinning():
                winner = True
                if self.isPlayer1:
                    print("Congratulations! {} Won the game.".format(self.player1.playerName))
                else:
                    print("Congratulations! {} Won the game.".format(self.player2.playerName))
                break
        
        if not winner and self.isGameDraw():
            print("Game is drawn, well played {} and {}.".format(self.player1.playerName, self.player2.playerName))
        print("See ya!")
        self.isEnded = True
    
    def isGameDraw(self) -> bool:
        countNone = 0
        for r in self.gameBoard.board:
            for c in r:
                if c is None:
                    countNone += 1
        return countNone == 0

    def toggleMove(self):
        if self.isPlayer1:
            self.isPlayer1 = False
        else:
            self.isPlayer1 = True

    def checkMove(self) -> str:
        if self.isPlayer1:
            print("{}'s Turn ({}): ".format(self.player1.playerName, self.player1.playerSymbol))
            return self.player1.playerSymbol
        else:
            print("{}'s Turn ({}): ".format(self.player2.playerName, self.player2.playerSymbol))
            return self.player2.playerSymbol

    # O()
    def makeMove(self):
        move = self.checkMove()
        row = input("Enter row: ")
        col = input("Enter column: ")
        try:
            row = int(row)
            col = int(col)
            if row >= 1 and row <= self.gameBoard.boardSize and col >= 1 and col <= self.gameBoard.boardSize:
                if self.gameBoard.board[row-1][col-1] is None:
                    self.gameBoard.board[row-1][col-1] = move
                else:
                    print("Please choose another row/column values.")
                    self.makeMove()
            else:
                print("Please Enter a valid number between 1 and {}.".format(self.gameBoard.boardSize))
                self.makeMove()
        except ValueError:
            print("Please enter an integer value.")
            self.makeMove()
        
    # Time O(n*n) Space O(1)
    def isAnyPlayerWinning(self) -> bool:
        if self.isPlayer1:
            valueToCheck = self.player1.playerSymbol
        else:
            valueToCheck = self.player2.playerSymbol

        for row in range(self.gameBoard.boardSize):
            sameValueInRow = True
            sameValueInCol = True
            for col in range(self.gameBoard.boardSize):
                # checking rows
                if self.gameBoard.board[row][col] != valueToCheck:
                    sameValueInRow = False
                # checking columns
                if self.gameBoard.board[col][row] != valueToCheck:
                    sameValueInCol = False
            
            if sameValueInRow or sameValueInCol:
                return True

        sameValueInFirstDiagonal = True
        sameValueInSecondDiagonal = True
        for diagonal in range(self.gameBoard.boardSize):
            # checking first diagonal
            if self.gameBoard.board[diagonal][diagonal] != valueToCheck:
                sameValueInFirstDiagonal = False
            # checking second diagonal
            if self.gameBoard.board[diagonal][self.gameBoard.boardSize - diagonal - 1] != valueToCheck:
                sameValueInSecondDiagonal = False

        if sameValueInFirstDiagonal or sameValueInSecondDiagonal:
            return True
        
        return False

class Player:
    def __init__(self, playerId: int):
        self.playerId = playerId
        self.playerName = ""
        self.playerSymbol = ""
    
    def setPlayerName(self):
        self.playerName = input("Enter Player {}'s Name: ".format(self.playerId))
    
    def setPlayerSymbol(self, symbol: str):
        self.playerSymbol = symbol

if __name__ == "__main__":
    print("--------------------------------------------------------------------")
    print("|  Welcome to Tic Tac Toe, a game developed in Python by Rishabh!  |")
    print("--------------------------------------------------------------------")

    gameBoardId = 1
    player1Id = 1
    player2Id = 2
    gameId = 1

    gameBoard = GameBoard(gameBoardId)
    gameBoard.setBoard()
    
    player1 = Player(player1Id)
    player1.setPlayerName()
    player2 = Player(player2Id)
    player2.setPlayerName()
    print("Welcome Aboard {} and {} to the Game.".format(player1.playerName, player2.playerName))

    x = random.randint(0, 1)
    if x == 1:
        player1Symbol = "X"
        player2Symbol = "O"
    else:
        player1Symbol = "O"
        player2Symbol = "X"
    
    player1.setPlayerSymbol(player1Symbol)
    player2.setPlayerSymbol(player2Symbol)

    print("{} takes {} and {} takes {}".format(player1.playerName, player1Symbol, player2.playerName, player2Symbol))

    game = Game(gameId, player1, player2, gameBoard)
    game.startGame()

