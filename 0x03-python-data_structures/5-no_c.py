#!/usr/bin/python3
def no_c(my_string):
    """ remove all characterCc in the given string.
    and return the new string"""

     return ("".join([c for c in my_string if c not in ['c', 'C']]))
