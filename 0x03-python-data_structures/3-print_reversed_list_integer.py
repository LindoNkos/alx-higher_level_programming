#!/usr/bin/python3
print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_lis)

if isinstance(my_list, list):
    reversed_list = my_list
    reversed_list.reverse()

    for element in reversed_list:
        print("{:d}".format(element))
