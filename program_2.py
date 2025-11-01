# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 
# (up to 1000).

import random

def main():
    amount = int(input("How many random numbers should be written to the file? (1–1000): "))

    while amount < 1 or amount > 1000:
        print("Error: Number must be between 1 and 1000.")
        amount = int(input("Enter a valid amount: "))

    file = open("random_numbers.txt", "w")

    for i in range(amount):
        number = random.randint(1, 500)
        file.write(str(number) + "\n")

    file.close()

    print(f"{amount} random numbers have been written to random_numbers.txt")

if __name__ == "__main__":
    main()