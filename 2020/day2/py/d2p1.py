#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main() -> None:
    input = []
    valid_pass = 0
    with open("../input.txt", "r") as f:
        input = [line.strip().replace(":", "").split() for line in f]

    for i in input:
        rng, char, password = i[0].split("-"), i[1], i[2]
        counts = password.count(char)
        if counts >= int(rng[0]) and counts <= int(rng[1]):
            valid_pass += 1

    print(valid_pass)


if __name__ == "__main__":
    exit(main())
