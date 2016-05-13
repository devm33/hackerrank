#!/usr/bin/env python

def solution(args):
    pass


def main():
    T = int(raw_input())
    for i in range(T):
        print 'Case #%s:' % (i+1)
        solution(*map(int, raw_input().split()))


if __name__ == "__main__":
    main()
