#!/usr/bin/env python
# -*- coding: utf-8 -*-

# [!] DISCLAIMER [!]: The worst solution ever, but works quite fast.

rules = {}


def contains(value):
    global rules
    items = rules[value]
    count = 0
    count = len(items)

    for i in items:
        count += contains(i)

    return count


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
            times = int(item[:2])
            new_item = item[2:]
            for _ in range(times):
                value.append(new_item)

    return key, value


def main():
    global rules
    with open("../input.txt", "r") as f:
        rules = dict(parser(line.strip()) for line in f.readlines())

    count = contains("shiny gold")
    print(count)
    return 0


if __name__ == "__main__":
    exit(main())
