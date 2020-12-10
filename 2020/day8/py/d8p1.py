#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    instructions = []
    with open("../input.txt", "r") as f:
        instructions = [i.strip() for i in f.readlines()]

    pos = 0
    positions = []
    acc = 0
    while True:
        cmd = instructions[pos]
        amount = int(cmd.split(" ")[1])
        if "acc" in cmd:
            if pos + 1 in positions:
                break
            acc += amount
            pos += 1
        elif "jmp" in cmd:
            if pos + amount in positions:
                break
            pos += amount
        elif "nop" in cmd:
            if pos + 1 in positions:
                break
            pos += 1

        positions.append(pos)

    print(acc)


if __name__ == "__main__":
    exit(main())
