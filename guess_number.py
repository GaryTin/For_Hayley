import random as rd


def generate_random_no():
    return rd.randint(1, 100)


if __name__ == "__main__":
    ans = generate_random_no()
    #print(ans)
    is_correct = False
    upper = 100
    lower = 1
    count_guess = 1

    while not(is_correct) and (count_guess<=8):
        print("="*30)
        print("Round {}!".format(count_guess))
        print("The answer is between {} and {}.".format(lower, upper))

        try:
            guess = int(input("Guess Number: "))
        except Exception as e:
            print("invalid input")
            continue

        if guess > upper or guess < lower :
            print("out of range!")
            continue

        count_guess += 1

        if guess == ans:
            is_correct = True
        elif guess > ans:
            print("Too Large")
            upper = guess-1
        else:
            print("Too Small")
            lower = guess+1

    if is_correct:
        print('Yayyyy')
    else:
        print("Too many guess")





