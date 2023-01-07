#!/usr/bin/python3
def element_at(my_list, idx):
    """get an element at a given index, 
    return the element when found or none if the element is negetive
    or else if element is out of range of the list length"""

    if idx < 0 or idx > (len(my_list) - 1):
        return None
    else:
        return my_list[idx]
