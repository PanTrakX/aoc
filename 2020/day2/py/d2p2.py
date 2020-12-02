#!/usr/bin/env python
# -*- coding: utf-8 -*-

import operator


def main() -> None:
    input = []
    valid_pass = 0
    with open("../input.txt", "r") as f:
        input = [line.strip().replace(":", "").split() for line in f]

    for i in input:
        index, char, password = i[0].split("-"), i[1], i[2]
        if operator.xor(password[int(index[0]) - 1] == char, password[int(index[1]) - 1] == char):
            valid_pass += 1

    print(valid_pass)
    return 0


if __name__ == "__main__":
    exit(main())  # 391
