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


class Node:
    """ nodes for the tree """

    def __init__(self, size, index) -> None:
        """ constructor """

        self.size: int = size
        self.index: int = index
        self.children: List[int] = []


class Tree:
    """ tree for the structure """

    def __init__(self, n_ini: int, s_ini: List[int]) -> None:
        """ constructor"""

        self.r_node = Node(s_ini[0], 1)
        self.n_in = n_ini
        self.s_ini = s_ini
        self.propagate_tree(self.r_node, n_ini, s_ini)
    
    def get_mdepth(self, r_node: Node) -> int:
        """ retrieve maximum depth of tree """

        if r_node.children == []:
            return 1

        ret = [
            self.get_mdepth(child) + 1
            for child in r_node.children
        ]

        return max(ret)

    def propagate_tree(self, r_node: Node, n_in: int, s_ini: List[int]):
        """ create branches recursively """

        r_node.children = [
            Node(s_ini[index-1], index)
            for index in range(r_node.index*2, n_in+1, r_node.index)
            if s_ini[index-1] > r_node.size
        ]
        if r_node.children == []:
            return

        for ind, _ in enumerate(r_node.children):
            self.propagate_tree(r_node.children[ind], n_in, s_ini)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """



# --------------------------------------------------
if __name__ == '__main__':
    main()
