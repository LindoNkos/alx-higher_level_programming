#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """replace an element in the list of the given index
    return original list if given index is negetive
    or out of range (the index number given is greater than the length of the list"""
    if idx >= 0 and idx <= (len(my_list) - 1):
        my_list[idx] = element
    return my_list
