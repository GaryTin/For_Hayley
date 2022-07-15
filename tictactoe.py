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
        #print(self.board)

    def choose(self,loc):
        if self.is_A_turn:
            self.board[loc] = "O"
        else:
            self.board[loc]= "X"

        self.is_A_turn = not(self.is_A_turn)

    def is_win(self, chosen_index) -> str:
        x = chosen_index%3
        y = chosen_index//3

        if (self.board[3*0+x] == self.board[3*1+x] and self.board[3*0+x] == self.board[3*2+x]) or (self.board[3*y+0] == self.board[3*y+1] and self.board[3*y+0] == self.board[3*y+2]):
            return self.board[chosen_index]
        if chosen_index % 2 == 0:
            #check diagonal
            if x+y == 2:
                if self.board[2]== self.board[4] and self.board[2]== self.board[6]:
                    return self.board[chosen_index]
            elif x==y:
                if self.board[0]== self.board[4] and self.board[0]== self.board[8]:
                    return self.board[chosen_index]
        return "N"

    def start_game(self):
        while True:
            self.draw_game()

            user_input = int(input("Please enter which index you want: "))

            while(self.board[user_input]!= "N"):
                user_input = int(input("Please enter a valid index: "))

            self.choose(user_input)

            if (self.is_win(user_input) != "N"):
                self.draw_game()
                print(self.is_win(user_input) + "Win")
                break

def main():
    tictactoe = TicTacToe()
    tictactoe.start_game()

if __name__ == "__main__":
    main()
