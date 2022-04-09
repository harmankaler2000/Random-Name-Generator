# Random Name Generator

A python script that generates random names (first and last) based on a list of names taken from the following github repository:

Names database: https://github.com/smashew/NameDatabases

The idea: To create a program that produces a random name and asks for user if they want to continue producing more names or exit.

Packages used:
Pandas - to read the raw csv file and get the names from the first index
Random - to genrate random names for the first and last nname from the list generated by reading the csv file

Pseudo Code for the program:
- list of first names
- list of surnames
- choose first name randomly
- Assign it to the first name variable
- choose second name randomly
- Assign it to the second name randomly
- print the names on the screen in the format "first_name" "sur_name"
- Ask user if they want to quit or continue
- if user chooses to continue
  - repeat the entire code
- if user chooses to quit
  - end the game and exit