"""Project to generate random names"""
import sys
import random
import pandas as pd
# links to the github datasets for names
SURNAMES = "https://raw.githubusercontent.com/smashew/NameDatabases/master/NamesDatabases/surnames/all.txt"
FIRSTNAMES = "https://raw.githubusercontent.com/smashew/NameDatabases/master/NamesDatabases/first%20names/all.txt"

def read_csv(filename):
    """
    Function to read the csv file and return a list of names
    """
    names_df = pd.read_csv(filename, header=None, on_bad_lines='skip')
    names = list(names_df[0])
    return names


def main():
    """
    Main Function
    """
    print("Hi! Welcome to the Random Name Generator!")
    print("This program will generate a random name for you.")
    first_names = read_csv(FIRSTNAMES)
    sur_names = read_csv(SURNAMES)
    while True:
        try:
            first_random = random.choice(first_names)
            sur_random = random.choice(sur_names)
            print(f"{first_random} {sur_random}")
            print("Would you like to generate another name? (y/n)")
            answer = input()
            if answer.lower() == "y":
                continue
            if answer.lower() == "n":
                print("Thank you for using the Random Name Generator!")
                sys.exit()
            else:
                print("Invalid answer! Exiting Program...")
        except Exception as error:
            print("Exception occured: ", str(error))


if __name__ == "__main__":
    main()
