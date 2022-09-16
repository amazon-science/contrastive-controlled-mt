#!/usr/bin/env python3

import sys
import string

def check_latin(s):
    total = 0
    latin = 0
    for line in s.splitlines():
        for c in line.lower():
            if c in string.ascii_lowercase + string.digits + string.punctuation:
                latin += 1
            total += 1
    return latin / total

if __name__ == "__main__":
    with open(sys.argv[1], encoding="utf-8") as f:
        print("% Latin", check_latin(f.read()) * 100)
