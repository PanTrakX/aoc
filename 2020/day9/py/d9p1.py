#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    inp = []
    with open("../input.txt", "r") as f:
        inp = [int(line.strip()) for line in f.readlines()]

    for i in range(25, len(inp)):
        does_sum = False
        for x in range(i - 25, i):
            for y in range(x, i):
                if inp[x] + inp[y] == inp[i]:
                    does_sum = True
        if does_sum:
            continue
        else:
            print(inp[i])

    return 0


if __name__ == "__main__":
    exit(main())
