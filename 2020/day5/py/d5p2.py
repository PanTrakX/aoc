#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import ceil, floor


def decoder(encoded):
    rows = [0, 127]
    columns = [0, 7]
    row = 0
    column = 0
    for char in encoded:
        if char == "F":
            rows[1] = floor((rows[0] + rows[1]) / 2)
            row = rows[1]
        elif char == "B":
            rows[0] = ceil((rows[0] + rows[1]) / 2)
            row = rows[0]
        elif char == "R":
            columns[0] = ceil((columns[0] + columns[1]) / 2)
            column = columns[0]
        elif char == "L":
            columns[1] = floor((columns[0] + columns[1]) / 2)
            column = columns[1]

    return row * 8 + column


def main():
    seats = []
    with open("../input.txt", "r") as f:
        seats = [s.strip() for s in f.readlines()]

    seat_ids = [decoder(s) for s in seats]

    for s in range(0, max(seat_ids)):
        if (s not in seat_ids) and (s + 1 in seat_ids) and (s - 1 in seat_ids):
            print(s)
            return 0


if __name__ == "__main__":
    exit(main())
