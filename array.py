#!/usr/bin/env python3
# Created by: Melody Berhane
# Created on: Jan 30, 2022
# This program asks the user for the unit, radius and height 
# It then calculates and displays the surface area and
# volume of a cylinder and cone.

def merge_list():
    str_of_num= input("Please enter a list: ")
    str_of_num2= input("Please enter another list: ")
    list_str_of_num = []
    list_str_of_num = str_of_num.split(",")
    list_str_of_num2 = []
    list_str_of_num2 = str_of_num2.split(",")
    #size_list_of_num = list.length
    list_of_int = []
    list_of_int2 = []
    for str_num in list_str_of_num:
        a_num = int(str_num)
        list_of_int.append(a_num)
    print (list_of_int)

    for str_num2 in list_str_of_num2:
        a_num2 = int(str_num2)
        list_of_int2.append(a_num2)
    print (list_of_int2)

    final_list = []
    final_list = sorted(list_of_int + list_of_int2)
    print(final_list)


def remove(duplicate):
    final_list = []
    print("This is the list: {}".format(duplicate))
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    final_list = sorted(final_list)
    return final_list
    
def rotate_list():
    n = int(input("Please enter how much you would like to rotate it to the left: "))
    str_of_num= input("Please enter a list: ")
    list_str_of_num = []
    list_str_of_num = str_of_num.split(",")
    list_of_int = []
    for str_num in list_str_of_num:
      a_num = str_num
      list_of_int.append(a_num)
    print ("This is the orginal list: {}".format(list_of_int))
    if n>len(list_of_int):
        n = int(n%len(list_of_int))
    list_of_int = (list_of_int[-n:] + list_of_int[:-n])
     
    print("This is the list rotated {} times to the left: {}".format(n, list_of_int))




def main():
    print("Which of the following programs would you like to run?")
    print("1 = Merge 2 lists")
    print("2 = Rotate list to the left")
    print("3 = Remove Duplicates")
    user_input = int(input("Please enter either 1, 2 or 3: "))
    if user_input == 1:
        merge_list()
    elif user_input == 2:
        rotate_list()
    elif user_input == 3:
        str_of_num= input("Please enter a list: ")
        list_str_of_num = []
        list_str_of_num = str_of_num.split(",")
        #size_list_of_num = list.length
        duplicate = []
        for str_num in list_str_of_num:
            a_num = int(str_num)
            duplicate.append(a_num)
        print("This is the list with no duplicates: {}".format(remove(duplicate)))
    else:
        print("Sorry but the input wasn't valid.")
    print("Have a good day!")

if __name__ == "__main__":
    main()