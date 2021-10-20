#traditional board size (6*7)
r = 6       #Row
c = 7       #Column
p = 4       #Pieces to connect

#but we will also support (r*c) board with connecting p pieces
while True:
    try:
        r, c, p = input("Enter the values of Row, Column and Pieces: ").split()
        r, c, p = int(r), int(c), int(p)
    except:
        print("Please enter integer value")

    if p == 0:
        print("You cannot have 0 pieces to connect.")
        p = int(input("Please enter a positive, non-zero integer for the number of pieces to connect: "))
    if r < 1 and c < 1 and p < 1:
        print("Wrong Board.")
        print("Please enter the positive, non-zero integers")
        if p == 0:
            print("You cannot have 0 pieces to connect.")
            p = int(input("Please enter a positive, non-zero integer for the number of pieces to connect: "))
            break
    else:
        break

#creating board board 
class Board():
    def __init__(self):
        self.board = [[' ' for _ in range(c)] for _ in range(r)]
        self.turns = 0
        self.last_move = [-1, -1] #[row, column]

    def displayboard(self):
        print()

        # Print the slots of the board board
        for i in range(r):
            print('|', end="")
            for j in range(c):
                print(f"{self.board[i][j]}|", end="")
            print()
            print('-' * c * 2, end="")
            print('-')
        print()

    #for alternate chance to each player
    def whichplayer(self):
        players = [p1, p2]
        return players[self.turns % 2]
    
    #checking borders
    def checkborder(self, row, col):
        return (row >= 0 and row < r and col >= 0 and col < c)

    def turn(self, column):
        #check is there any space avilable in column
        for i in range(r-1, -1, -1):
            if self.board[i][column] == ' ':
                self.board[i][column] = self.whichplayer()
                self.last_move = [i, column]
                self.turns += 1
                return True
        return False

    #checking for winner
    def iswinner(self):
        lastrow = self.last_move[0]
        lastcol = self.last_move[1]
        lastcolor = self.board[lastrow][lastcol]

        #declaration of diractions
        vu=[[-1, 0], 0, True]       #vertical upward direction 
        vd=[[1, 0], 0, True]        #vertical downward direction
        hl=[[0, -1], 0, True]       #horizontal left direction
        hr=[[0, 1], 0, True]        #horizontal right direction
        ul=[[-1, -1], 0, True]      #up-left direction
        dr=[[1, 1], 0, True]        #down-right direction
        ur=[[-1, 1], 0, True]       #up-left direction
        dl=[[1, -1], 0, True]       #down-left direction

        directionarray = [vu,vd,hl,hr,ul,dr,ur,dl]

        #checking for matching pieces
        for a in range(p):
            for d in directionarray:
                row = lastrow + (d[0][0] * (a+1))
                col = lastcol + (d[0][1] * (a+1))

                if d[2] and self.checkborder(row, col) and self.board[row][col] == lastcolor:
                    d[1] += 1
                else:
                    #not in this direction
                    d[2] = False

        #check possible direction pairs for connecting pieces
        for i in range(0, c, 2):
            if (directionarray[i][1] + directionarray[i+1][1] >= p-1):
                self.displayboard()
                if lastcolor==p1:
                    pler=1
                else:
                    pler=2
                print(f"Player {pler} is the winner!")
                return lastcolor   
        #if winners is not found
        return False

def play():
    #initialize the game board
    board = Board()

    boardOver = False
    while not boardOver:
        board.displayboard()

        #take input for column from player
        correctmove = False
        while not correctmove:
            if board.whichplayer()==p1:
                pler=1
            else:
                pler=2
            playermove = input(f"Player {pler}, what column do you want to put your piece? ")
            try:
                correctmove = board.turn(int(playermove)-1)
            except:
                print("Please choose a number between 1 and", c)

        #end the game if winner is found
        boardOver = board.iswinner()
        
        #draw game if it's tie
        if not any(' ' in x for x in board.board):
            print("The Game is a draw..")
            return

if __name__ == '__main__':
    ch = 1
    while ch == 1:
        p1 = input("Player one, do you red or yellow (r or y)? ")
        if p1 == 'r' or 'y':
            if p1 == 'r':
                p2 = 'y'
            else:
                p2 = 'r'
        else:
            print("Wrong Choice..!")
            continue
        play()
        ch = int(input("Do you want to play again(0-no, 1-yes)? "))
