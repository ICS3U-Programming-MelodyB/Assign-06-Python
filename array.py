#!/usr/bin/env python3
# Created by: Melody Berhane
# Created on: Jan 30, 2022
# This program asks the user what program they want to run
# They caneither merge two lists
# Remove duplicates from the list
# Or rotate a list to the left by a specif number.


# This function merges the two lists together
def merge_list(list_str_num, list_str_num2):
    # The first and second lists that hold the ints
    list_of_int = []
    list_of_int2 = []
    # loops through the lists that holds the strings and converts them to ints
    for str_num in list_str_num:
        # Converts string to int
        try:
            a_num = int(str_num)
            list_of_int.append(a_num)
        except Exception:
            print("Sorry but the input wasn't valid.")
    print("This is the first list: {}".format(list_of_int))
    # loops through the lists that holds the strings and converts them to ints
    for str_num2 in list_str_num2:
        # Converts string to int
        try:
            a_num2 = int(str_num2)
            list_of_int2.append(a_num2)
        except Exception:
            print("Sorry but the input wasn't valid.")
    print("This is the second list: {}".format(list_of_int2))
    # Creates the new list
    final_list = []
    # Adds the two lists togther, sorts them and assigns it to the final list.
    final_list = sorted(list_of_int + list_of_int2)
    # returns the final list to main
    return final_list


# This function removes any deplicates from the list
def remove(duplicate):
    # Creates the list
    final_list = []
    print("This is the list: {}".format(duplicate))
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    # Sorts through the final list
    final_list = sorted(final_list)
    # retuns final_list to main
    return final_list


# This function removes any deplicates from the list
def rotate_list(list_str_num3, number):
    list_of_int = []
    for str_num in list_str_num3:
        a_num = str_num
        list_of_int.append(a_num)
    print("This is the orginal list: {}".format(list_of_int))
    # Got code from;
    # https://www.geeksforgeeks.org/python-program-right-rotate-list-n/
    # I modified it by making it accept user input in main.
    if number > len(list_of_int):
        number = int(number % len(list_of_int))
    list_of_int = (list_of_int[-number:] + list_of_int[:-number])
    # returns list_of_ints to main
    return(list_of_int)


def main():
    # Prints instructions
    print("Which of the following programs would you like to run?")
    print("1 = Merge 2 lists")
    print("2 = Rotate list to the left")
    print("3 = Remove Duplicates")
    # Asks the user what prorgam they would like to run
    user_input = input("Please enter either 1, 2 or 3: ")
    print()
    # # Converts string to int
    try:
        user_input = int(user_input)
        # Gets user input so the lists can be merged
        if user_input == 1:
            str_of_num = input("Please enter a list of integers: ")
            str_of_num2 = input("Please enter another list integers: ")
            list_str_of_num = []
            list_str_of_num = str_of_num.split(",")
            list_str_of_num2 = []
            list_str_of_num2 = str_of_num2.split(",")
            final_list_user = merge_list(list_str_of_num, list_str_of_num2)
            print()
            print("This is the final merged list: {}".format(final_list_user))
        # Gets user input so the lists can rotated by the specific number
        elif user_input == 2:
            number_user = int(input("Please enter how much you would like"
                                    "to rotate it to the left: "))
            str_of_num3 = input("Please enter a list: ")
            list_str_of_num3 = []
            list_str_of_num3 = str_of_num3.split(",")
            final_list_user2 = rotate_list(list_str_of_num3, number_user)
            print()
            print("This is the list rotated {} times to the left: {}".
                  format(number_user, final_list_user2))
        # Gets user input so the lists can remove duplicates
        elif user_input == 3:
            str_of_num = input("Please enter a list: ")
            list_str_of_num = []
            list_str_of_num = str_of_num.split(",")
            duplicate = []
            for str_num in list_str_of_num:
                a_num = str_num
                duplicate.append(a_num)
            print()
            print("This is the list with no duplicates: {}".
                  format(remove(duplicate)))
        else:
            print("Sorry but the input wasn't valid.")
    except Exception:
        print("Sorry but the input was not valid.")
    print()
    print("Have a good day!")


if __name__ == "__main__":
    main()
