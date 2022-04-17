#!/usr/bin/python3
""" getting skateboard 1300 """

from unittest import TestCase


class Test(TestCase):
    """ test cases """

    def test_get_subs(self):
        """ test the function get substring """

        self.assertEqual(get_subs('123'), ['1', '12', '123', '2', '23', '3'])
        self.assertEqual(
            get_subs('1234'),
            ['1', '12', '123', '1234', '2', '23', '234', '3', '34', '4']
        )

    def test_answer(self):
        """ test that answer returns the number of
        substrings divisible by 4 given a string """

        self.assertEqual(answer('124'), 4)
        self.assertEqual(answer('04'), 3)
        self.assertEqual(answer('5810438174'), 9)

    def test_count_048(self):
        """ test count 4 8 function """

        self.assertEqual(count_1_div_4('124'), 1)
        self.assertEqual(count_1_div_4('1244'), 2)
        self.assertEqual(count_1_div_4('4844'), 4)
        self.assertEqual(count_1_div_4('48440'), 5)
    
    def test_count_2_div_4(self):
        """ test count 2 divisible by 4 function """

        self.assertEqual(count_2_div_4('124'), 3)
        self.assertEqual(count_2_div_4('12'), 1)
        self.assertEqual(count_2_div_4('4321'), 2)


def get_subs(str_1) -> list:
    """ return a list of all substrings given a string """

    n_str = len(str_1)
    return [
        str_1[ind1: ind1 + len_]
        for ind1 in range(n_str) for len_ in range(1, n_str - ind1 + 1)
    ]


def count_1_div_4(str_1) -> int:
    """ return number of single digits that are divisible by 8 """

    return sum([1 for char in str_1 if char in '048'])


def count_2_div_4(str_1) -> int:
    """ count the number of two length substrings 
    from the back, divisible by 4 """

    n_str = len(str_1)
    return sum(
        [
            ind
            for ind in range(n_str-1, 0, -1)
            if int(str_1[ind-1:ind+1]) % 4 == 0
        ]
    )


def answer(str_1):
    """ return the number of substrings divisible by 4 """

    return count_1_div_4(str_1) + count_2_div_4(str_1)


def main() -> None:
    """ do stuff """

    print(answer(input()))


if __name__ == '__main__':
    main()
