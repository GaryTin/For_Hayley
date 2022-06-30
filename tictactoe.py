class TicTacToe():
    def __init__(self):
        self.board = ["N"]*9
        self.is_A_turn = True

    def draw_game(self):
        print("="*30)
        for i in range(11):
            for j in range(11):
                if j % 4 == 3:
                    print("|", end="")
                elif i % 4 == 3:
                    print("---", end="")
                elif i%4 == 1 and j%4==1 and self.board[3*(i//4)+(j//4)] != "N":
                    print(" {} ".format(self.board[3*(i//4)+(j//4)]), end="")
                else:
                    print("   ", end="")
            print()
        print(self.board)

    def choose(self,loc):
        if self.is_A_turn:
            self.board[loc] = "O"
        else:
            self.board[loc]= "X"

        self.is_A_turn = not(self.is_A_turn)





def main():
    tictactoe = TicTacToe()
    tictactoe.draw_game()

    tictactoe.choose(0)
    tictactoe.choose(1)
    tictactoe.choose(2)
    tictactoe.choose(4)
    tictactoe.draw_game()


if __name__ == "__main__":
    main()