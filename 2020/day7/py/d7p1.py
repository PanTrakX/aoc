#!/usr/bin/env python
# -*- coding: utf-8 -*-

# [!] DISCLAIMER [!]: The worst solution ever, but works quite fast.

rules = {}


def contains(value):
    global rules
    if "shiny gold" in value:
        return 1
    else:
        for item in value:
            if contains(rules[item]):
                return 1

    return 0


def parser(inp):
    c1 = inp.strip()
    c2 = c1.replace("contain", "").strip()
    c3 = c2.replace(".", "").strip()
    c4 = c3.replace(".", "").strip()
    c5 = c4.replace(",", "").strip()
    c6 = c5.replace("no other", "").strip()
    bags_split = c6.split("bags")
    li = []
    for x in bags_split:
        bag_split = x.strip().split("bag")
        for y in bag_split:
            if y != "":
                li.append(y.strip())

    key = ""
    value = []

    for index, item in enumerate(li):
        if index == 0:
            key = item
        else:
            value.append(item[2:])

    return key, value


def main():
    global rules
    with open("../input.txt", "r") as f:
        rules = dict(parser(line.strip()) for line in f.readlines())

    count = sum([contains(item) for item in rules.values()])
    print(count)
    return 0


if __name__ == "__main__":
    exit(main())
