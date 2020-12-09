#!/usr/bin/env python
# -*- coding: utf-8 -*-

FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def check_passport(p):
    if not (all([field in p for field in FIELDS])):
        return 0
    if not (len(p["byr"]) == 4 and (1920 <= int(p["byr"]) <= 2002)):
        return 0
    if not (len(p["iyr"]) == 4 and (2010 <= int(p["iyr"]) <= 2020)):
        return 0
    if not (len(p["eyr"]) == 4 and (2020 <= int(p["eyr"]) <= 2030)):
        return 0
    msr = p["hgt"][-2:]
    if not (msr in ["cm", "in"]):
        return 0
    hgt = int(p["hgt"][:-2])
    if not ((msr == "cm" and (150 <= hgt <= 193)) or (msr == "in" and
                                                      (59 <= hgt <= 76))):
        return 0
    if not (len(p["hcl"]) == 7 and p["hcl"][0] == "#"):
        return 0
    if not (p["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
        return 0
    if not (p["pid"].isdigit() and len(p["pid"]) == 9):
        return 0

    print(p)
    return 1


def main():
    passports = []

    with open("../input.txt", "r") as f:
        passports = [
            dict(x.split(":") for x in y.replace("\n", " ").split(" "))
            for y in f.read().strip().split("\n\n")
        ]

    valid_pass = sum([check_passport(p) for p in passports])
    print(valid_pass)
    return 0


if __name__ == "__main__":
    exit(main())
