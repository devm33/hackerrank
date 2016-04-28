#!/usr/bin/env python
# -*- coding: utf-8 -*-

def counter_add(dictionary, key):
    if key in dictionary:
        dictionary[key] += 1
    else
        dictionary[key] = 1
    return dictionary

def occurrences(s):
    return reduce(counter_add, s, {})

def minsteady(n, s):
    occurs = occurrences(s)

    # TODO

    return 0

def main():
    n = int(raw_input())
    s = raw_input()
    print minsteady(n, s)

if __name__ == "__main__":
    main()
