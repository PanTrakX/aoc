#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    num_list = []
    with open('../input.txt', 'r') as f:
        num_list = [int(line.strip()) for line in f]

    for x in num_list:
        for y in num_list:
            if x + y == 2020:
                print(x * y)
                return 0
    return 1


if __name__ == '__main__':
    exit(main())
