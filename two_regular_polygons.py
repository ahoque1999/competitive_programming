#!/usr/bin/python3
""" two regular polygons """


def main() -> None:
    """ do stuff """
    for _ in range(int(input())):
        n_inp, m_inp = list(map(int, input().split()))
        if n_inp // m_inp == n_inp / m_inp:
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    main()
