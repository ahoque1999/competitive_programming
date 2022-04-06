#!/usr/bin/python3
""" vasya and coins 800 """


def main() -> None:
    """ do stuff """

    for _ in range(int(input())):
        a_inp, b_inp = list(map(int, input().split()))
        if a_inp == 0:
            print(1)
            continue
        print(a_inp + b_inp * 2 + 1)


if __name__ == '__main__':
    main()
