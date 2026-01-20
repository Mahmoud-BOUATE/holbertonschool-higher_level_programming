#!/usr/bin/python3

def search_replace(my_list, search, replace):

    for i in range(len(my_list)):
        if my_list[i] == search:
            new_list = my_list.copy()
            new_list[i] = replace
    return new_list
