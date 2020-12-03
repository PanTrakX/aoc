#!/usr/bin/env python
# -*- coding: utf-8 -*-

geology = []
x_length = 0
y_length = 0


def determine(right, down) -> int:
    global geology
    global x_length
    global y_length

    current_pos = [0, 0]
    trees_encountered = 0

    while True:
        current_pos[0] = current_pos[0] + down
        current_pos[1] = (current_pos[1] + right) % x_length
        if current_pos[0] < y_length:
            if geology[current_pos[0]][current_pos[1]] == "#":
                trees_encountered += 1
        else:
            return trees_encountered


def main():
    global geology
    global x_length
    global y_length

    with open("../input.txt", "r") as f:
        geology = [line.strip() for line in f]

    x_length = len(geology[0])
    y_length = len(geology)

    s1 = determine(1, 1)
    s2 = determine(3, 1)
    s3 = determine(5, 1)
    s4 = determine(7, 1)
    s5 = determine(1, 2)

    print(s1 * s2 * s3 * s4 * s5)
    return 0


if __name__ == "__main__":
    exit(main())
