#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    map = []
    current_pos = [0, 0]
    trees_encountered = 0
    x_length = 0

    with open("../input.txt", "r") as f:
        map = [line.strip() for line in f]

    x_length = len(map[0])
    y_length = len(map)

    while True:
        current_pos[0] = current_pos[0] + 1
        current_pos[1] = (current_pos[1] + 3) % x_length
        if current_pos[0] < y_length:
            if map[current_pos[0]][current_pos[1]] == "#":
                trees_encountered += 1
        else:
            print(trees_encountered)
            return 0


if __name__ == "__main__":
    exit(main())
