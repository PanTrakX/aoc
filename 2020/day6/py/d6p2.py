#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    answers = []
    with open("../input.txt", "r") as f:
        answers = [line.strip().split("\n") for line in f.read().split("\n\n")]

    new_answers = []
    for a in answers:
        new_a = set()
        for i, b in enumerate(a):
            if i == 0:
                if len(a) == 1:
                    new_a = set(b)
                else:
                    new_a = set(b) & set(a[i + 1])
            else:
                new_a = set(b) & set(new_a)
        new_answers.append("".join(new_a))

    counts = sum([len(a) for a in new_answers])
    print(counts)
    return 0


if __name__ == "__main__":
    exit(main())
