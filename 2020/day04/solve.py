import sys
import re


passports = []
passport = {}
for line in sys.stdin:
    if not line.strip() and passport:
        passports.append(passport)
        passport = {}
    parts = line.split()
    passport.update([p.split(':') for p in parts])
if passport:
    passports.append(passport)


required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
required_ecl = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}


def validate1(passport):
    return required_fields.issubset(passport.keys())


def validate_hgt(hgt):
    return hgt.endswith('cm') and 150 <= int(hgt[:-2]) <= 193 \
        or hgt.endswith('in') and 59 <= int(hgt[:-2]) <= 76


def validate2(passport):
    return validate1(passport) \
        and 1920 <= int(passport['byr']) <= 2002 \
        and 2010 <= int(passport['iyr']) <= 2020 \
        and 2020 <= int(passport['eyr']) <= 2030 \
        and validate_hgt(passport['hgt']) \
        and re.match('#[0-9a-f]{6}$', passport['hcl']) \
        and passport['ecl'] in required_ecl \
        and re.match('\\d{9}$', passport['pid'])


def part1():
    print(len([p for p in passports if validate1(p)]))


def part2():
    print(len([p for p in passports if validate2(p)]))


part1()
part2()
