#!/usr/bin/env python
# -*- coding: utf-8 -*-

def visit(j, visited, zombies, N):
    for k in range(N):
        if zombies[j][k] == '1' and not visited[k]:
            visited[k] = True
            visit(k, visited, zombies, N)

def zombieCluster(zombies):
    N = len(zombies)
    visited = [False] * N
    clusters = 0
    for i in range(N):
        if not visited[i]:
            clusters += 1
            visited[i] = True
            visit(i, visited, zombies, N)
    return clusters

import unittest

class TestCluster(unittest.TestCase):
    def testSingles(self):
        self.assertEqual(4, zombieCluster([
                '1000',
                '0100',
                '0010',
                '0001']))


    def testChain(self):
        self.assertEqual(1, zombieCluster([
                '1100',
                '1110',
                '0111',
                '0011']))


    def testComplete(self):
        self.assertEqual(1, zombieCluster([
                '11111',
                '11111',
                '11111',
                '11111',
                '11111',
        ]))


    def testEveryOther(self):
        self.assertEqual(2, zombieCluster([
                '101010',
                '010101',
                '101010',
                '010101',
                '101010',
                '010101',
        ]))

    def testAllThroughLast(self):
        self.assertEqual(1, zombieCluster([
                '100001',
                '010001',
                '001001',
                '000101',
                '000011',
                '111111',
        ]))


    def testCluster(self):
        self.assertEqual(2, zombieCluster(['1100',
                                            '1110',
                                            '0110',
                                            '0001']))
        self.assertEqual(2, zombieCluster(['1100',
                                            '1100',
                                            '0011',
                                            '0011']))
        self.assertEqual(zombieCluster(['110000',
                                        '110000',
                                        '001001',
                                        '000110',
                                        '000110',
                                        '001001']), 3)


if __name__ == '__main__':
    unittest.main()
