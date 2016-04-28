#!/usr/bin/env python
# -*- coding: utf-8 -*-

def maxsum(N, M, arr):
    # first mod the array
    modarr = map(lambda x: x % M, arr)

    # initialize the max for subarray size 1
    curmax = max(modarr)

    sumsize = 1 # number of elements added to current
    sumarr = modarr[:]
    while sumsize < N and curmax < M - 1:
        for i in range(N-sumsize):
            sumarr[i] = sumarr[i] + modarr[i+sumsize]
            if sumarr[i] >= M:
                sumarr[i] -= M
            curmax = max(curmax, sumarr[i])
        sumsize += 1

    return curmax

def main():
    T = int(raw_input())
    for i in range(T):
        N, M = map(int, raw_input().split())
        arr = map(int, raw_input().split())
        print maxsum(N, M, arr)

if __name__ == "__main__":
    main()
