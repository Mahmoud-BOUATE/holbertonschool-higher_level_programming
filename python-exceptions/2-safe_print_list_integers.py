#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list if they are integers.

    Args:
        my_list: list of elements (any type)
        x: number of elements to access

    Returns:
        The number of integers actually printed
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            # ignore non-integer values
            pass
        except IndexError:
            # stop if we go beyond the list
            break
    print()  # new line after printing all integers
    return count
