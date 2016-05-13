#!/usr/bin/env python
# -*- coding: utf-8 -*-

def zombieCluster(zombies):
    N = len(zombies)
    cluster = range(N)
    for i in range(N):
        for j in range(i + 1, N):
            if zombies[i][j] == '1':
                cluster[j] = cluster[i]
    return len(set(cluster))

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
