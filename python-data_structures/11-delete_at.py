#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    new_list = my_list.copy()
    if 0 <= idx <= len(my_list) - 1:

        return my_list
    else:
        del (new_list[idx])
        return new_list

