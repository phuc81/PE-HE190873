import random

def guess_number():
    print("Enter a range for guessed number: ")
    range_limit = int(input())
    
    target_number = random.randint(1, range_limit)
    
    while True:
        guess = random.randint(1, range_limit)
        response = input(f"Is {guess} too high(h), too low(l), or correct(c): ")
        if response == "h":
            range_limit = guess - 1
        elif response == "l":
            range_limit = guess + 1
        elif response == "c":
            print(f"Welldone! the computer guess your number {guess} correctly!")
            break
        else:
            print("Ivalid input. PLease enter 'h', 'l', or 'c'.")

if __name__ == "__main__":
    guess_number()