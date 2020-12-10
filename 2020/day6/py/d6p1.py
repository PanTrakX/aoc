#!/usr/bin/env python
# -*- coding: utf-8 -*-


def remove_doubles(string):
    return "".join(dict.fromkeys(string))


def main():
    answers = []
    with open("../input.txt", "r") as f:
        answers = [
            remove_doubles(line.strip().replace("\n", ""))
            for line in f.read().split("\n\n")
        ]
    counts = sum([len(a) for a in answers])
    print(counts)


if __name__ == "__main__":
    exit(main())
