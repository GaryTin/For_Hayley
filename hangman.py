import random
import requests



def get_random_word() -> str:
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = requests.get(word_site)
    WORDS = response.content.splitlines()
    return str(random.choice(WORDS))[2:-1]

def get_all_pos(word,target):
    list =[]
    pos = 0
    for char in word:
        if char == target:
            list.append(pos)
        pos += 1
    return list

if __name__ == "__main__":
    answer = get_random_word()
    print(answer)
    answer = "apple"
    length = len(answer)

    while True:
        user_input = input("Please guess a word: ")
        if len(user_input)!= 1:
            print("Invalid Input! Pleases input again!")
        else:
            if get_all_pos(answer,user_input) == []:
                print(str(user_input)+" is not in the word! Please try again")
            else:
                print(str(user_input) + " is in the word!")




