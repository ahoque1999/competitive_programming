#!/usr/bin/env python3
"""
Author : ayman <ayman@localhost>
Date   : 2022-04-27
Purpose: module for utilities
"""

from typing import List

def split_s(str_1: str):
    """ split a string into a list of contiguous strings """

    n_str = len(str_1)
    
    temp = str_1[0]
    lis = []
    for ind in range(1, n_str):
        if str_1[ind] != str_1[ind-1]:
            lis.append(temp)
            temp = str_1[ind]
        else:
            temp += str_1[ind]
    lis.append(temp)

    return lis

def count0s(lis: List[int]) -> int:
    """ return number of 0s in list """

    return sum([1 for ele in lis if ele == 0])


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """



# --------------------------------------------------
if __name__ == '__main__':
    main()
