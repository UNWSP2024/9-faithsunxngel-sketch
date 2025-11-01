# Program #3: Average Numbers
# Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk.
# (please use the provided numbers.txt)
# Write a program that reads all of the numbers stored in the file and calculates their total.  

# The program should handle the following exceptions: 

# It should handle any IOError exceptions that are raised.
# It should handle any ValueError exceptions that are raised when the items that are read from the file 
# are converted to a number.
def sum_numbers_from_file():
    total = 0

    try:
        file = open("numbers.txt", "r")

        for line in file:
            try:
                number = int(line.strip())
                total += number
            except ValueError:
                print(f"ValueError: Could not convert '{line.strip()}' to an integer.")

        file.close()
        print(f"Total of all numbers: {total}")

    except IOError:
        print("IOError: Could not open file 'numbers.txt'.")
    print('In the sum_numbers_from_file function')

# You don't need to change anything below this line:
if __name__ == '__main__':
    sum_numbers_from_file()