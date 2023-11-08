#!/usr/bin/env python3
# Created by: Finn Kitor
# Created on: November 8th, 2023
# This program asks the user to enter a positive number and then uses a loop to calculate to the power of two and display the result.


def main():
    # user will input the number to the terminal
    user_number_as_string = input("Enter a positive number: ")
    print("")
    # terminal will process if the number is valid or not valid from the user.
    try:
        user_number_as_int = int(user_number_as_string)
    except ValueError:
        print("{} is not a number.".format(user_number_as_string))
    else:
        if user_number_as_int > 0:
            # terminal replicates a for loop that calculates the power of two
            for loop_counter in range(user_number_as_int + 1):
                power_of_two = loop_counter**2
                print("{}^2 = {}".format(loop_counter, power_of_two))
        else:  # terminal will display an error if the number is not inputted correctly
            print("{} is not a positive number.".format(user_number_as_int))
    finally:
        print("Thanks for playing with my program!")


if __name__ == "__main__":
    main()
