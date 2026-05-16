import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    score = 0
    
    for i in range (1, NUM_ROUNDS+1):
        print("Round", i)
        computer_num = random.randint(1,100)
        your_num = random.randint(1,100)
        

        print("Your number is", your_num)

        ans = input("Do you think your number is higher or lower than the computer's?: ")

        if (ans == "higher" and your_num>=computer_num) or (ans == "lower" and your_num<=computer_num):
            print("You were right! The computer's number was", computer_num)
            score+=1
        else:
            print("Aww, that's incorrect. The computer's number was", computer_num)
            
        print("Your score is now", score, "\n")

    print("Thanks for playing!")



if __name__ == "__main__":
    main()