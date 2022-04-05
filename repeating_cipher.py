#!/usr/bin/python3
""" repeating cipher 800 """


def main() -> None:
    """ do stuff """

    n_inp = int(input())
    s_inp = input()

    def cip(inp):
        return int(0.5 * inp ** 2 + 1.5 * inp)

    print(''.join([s_inp[cip(i)] for i in range(n_inp) if cip(i) < n_inp]))


if __name__ == '__main__':
    main()
