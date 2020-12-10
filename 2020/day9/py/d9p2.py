#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    inp = []
    with open("../input.txt", "r") as f:
        inp = [int(line.strip()) for line in f.readlines()]

    invalid_number = 0
    for i in range(25, len(inp)):
        does_sum = False
        for x in range(i - 25, i):
            for y in range(x, i):
                if inp[x] + inp[y] == inp[i]:
                    does_sum = True
        if does_sum:
            continue
        else:
            invalid_number = inp[i]

    for x_index, x in enumerate(inp):
        rang = []
        y_index = x_index + 1
        while sum(rang) < invalid_number:
            rang.append(inp[y_index])
            y_index += 1
        if sum(rang) == invalid_number:
            print(min(rang) + max(rang))
            return 0


if __name__ == "__main__":
    exit(main())
