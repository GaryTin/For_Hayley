import random
import requests

class Wordle_game():
    def __init__(self,**kwargs):
        self.sol = self.get_random_word()
        self.count = 0
        if kwargs.get("test"):
            print(self.sol)


    def valid_word(self,word):
        if len(word)!= 5:
            return False
        else:
            checked =[]
            for c in word:
                if c in checked:
                    return False
                else:
                    checked.append(c)
        return True

    def get_random_word(self) -> str:
        word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
        response = requests.get(word_site)
        WORDS = response.content.splitlines()
        word = str(random.choice(WORDS))[2:-1]
        while not(self.valid_word(word)):
            word = str(random.choice(WORDS))[2:-1]
        return word

    def start_game(self):
        input_word = input("Please enter your word:\t")
        while not(self.check_answer_and_print(input_word)) or len(input_word)!=5:
            if len(input_word)== 5:
                self.count += 1
                if self.count == 6:
                    print("Oh no. You lose.")
                    print('Answer is {0}.'.format(self.sol))
                    break
            input_word = input("Please enter your word:\t")
        if self.check_answer_and_print(input_word):
            print("Nice! You get it!")


    def check_answer_and_print(self,input):

        if input == "I Love You":
            print('Special gift for u: {0}'.format(self.sol))
            return False
        elif len(input)!=5:
            print("Invalid input")
            return False
        i = 0
        correct = True
        print("\t"*6,end="")
        for word in input:
            if word in self.sol:
                if self.sol[i] == word:
                    print("♥",end="")
                else:
                    print("♡",end="")
                    correct = False
            else:
                print("*",end="")
                correct = False
            i += 1
        print()
        return correct

if __name__ == "__main__":
    game = Wordle_game(test = False)
    game.start_game()