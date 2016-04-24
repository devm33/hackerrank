#!/usr/bin/env python
# -*- coding: utf-8 -*-

def modsum(M, arr):
    return reduce(lambda a, x: (a+x)%M, arr)

def maxsum(N, M, arr):
    # first check the subarrays of size 1
    modarr = map(lambda x: x % M, arr)
    curmax = max(modarr)

    # have we already peeked?
    if curmax == M - 1:
        return curmax

    # otherwise need check subarrays

    # can remove zeros since they do nothing
    modarr = [x for x in modarr if x != 0]
    N = len(modarr)

    subsize = N
    while subsize > 1 and curmax < M - 1:
        for offset in range(N - subsize + 1):
            curmax = max(curmax, modsum(M, modarr[offset:offset+subsize]))
        subsize -= 1

    return curmax

def main():
    T = int(raw_input())
    for i in range(T):
        N, M = map(int, raw_input().split())
        arr = map(int, raw_input().split())
        print maxsum(N, M, arr)

if __name__ == "__main__":
    main()
