#!/usr/bin/env python
# -*- coding: utf-8 -*-


def memodict(f):
    """ Memoization decorator for a function taking a single argument """
    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret 
    return memodict().__getitem__

@memodict
def solutions((N, K)):
    if N == 1 or K == 1:
        return 1 if K == 1 else 0
    return sum([solutions((N-i, K-1)) for i in range(N)])

def main():
    T = int(raw_input())
    for i in range(T):
        N, K = map(int, raw_input().split())
        print solutions((N, K))


if __name__ == "__main__":
    main()
