#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_inf(index, instructions):
    pos = 0
    positions = []
    acc = 0
    new_instructions = []
    for ind, i in enumerate(instructions):
        if ind == index:
            new_str = i
            if "jmp" in i:
                new_str = new_str.replace("jmp", "nop")
            elif "nop" in i:
                new_str = new_str.replace("nop", "jmp")
            new_instructions.append(new_str)
        else:
            new_instructions.append(i)

    try:
        while True:
            cmd = new_instructions[pos]
            amount = int(cmd.split(" ")[1])
            if "acc" in cmd:
                if pos + 1 in positions:
                    return True, acc
                acc += amount
                pos += 1
            elif "jmp" in cmd:
                if pos + amount in positions:
                    return True, acc
                pos += amount
            elif "nop" in cmd:
                if pos + 1 in positions:
                    return True, acc
                pos += 1

            positions.append(pos)

    except IndexError:
        return (False, acc)


def main():
    instructions = []
    with open("../input.txt", "r") as f:
        instructions = [i.strip() for i in f.readlines()]

    for index, i in enumerate(instructions):
        if ("jmp" in i) or ("nop" in i):
            results = is_inf(index, instructions)
            if results[0] == False:
                print(results[1])
                return 0

    return 1


if __name__ == "__main__":
    exit(main())
