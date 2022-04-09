# project to generate random names
import sys, random
import pandas as pd
# links to the github datasets for names
surnames = "https://raw.githubusercontent.com/smashew/NameDatabases/master/NamesDatabases/surnames/all.txt"

firstnames = "https://raw.githubusercontent.com/smashew/NameDatabases/master/NamesDatabases/first%20names/all.txt"

def read_csv(filename):
# import csv file through a link
    df = pd.read_csv(filename, header=None, on_bad_lines='skip')
    names = list(df[0])
    return names


def main():
    print("Hi! Welcome to the Random Name Generator!")
    print("This program will generate a random name for you.")
    first_names = read_csv(firstnames)
    sur_names = read_csv(surnames)
    while True:
        try:
            first_random = random.choice(first_names)
            sur_random = random.choice(sur_names)
            print(f"{first_random} {sur_random}")
            print("Would you like to generate another name? (y/n)")
            answer = input()
            if answer.lower() == "y":
                continue
            elif answer.lower() == "n":
                print("Thank you for using the Random Name Generator!")
                sys.exit()
            else:
                print("Invalid answer! Exiting Program...")
        except Exception as e:
            print("Exception occured: ", str(e))


if __name__ == "__main__":
    main()

