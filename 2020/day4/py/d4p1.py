#!/usr/bin/env python
# -*- coding: utf-8 -*-

FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def main():
    passports = []

    with open("../input.txt", "r") as f:
        passports = [dict(x.split(":") for x in y.replace("\n", " ").split(" ")) for y in f.read().strip().split("\n\n")]

    valid_passports = sum([all(field in p for field in FIELDS)for p in passports])
    print(valid_passports)

    return 0


if __name__ == "__main__":
    exit(main())
