#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

def offByOne(a, b):
    """return true if b can be made by removing one character from a.
    assumes len(a) == len(b) + 1
    """
    ai = 0
    incd = False
    for c in b:
        if a[ai] == c:
            ai += 1
        elif incd:
            return False
        else:
            incd = True
            ai += 1
            if a[ai] == c:
                ai += 1
            else:
                return False
    return True


class TestOffByOne(unittest.TestCase):

    def testPrefix(self):
        self.assertTrue(offByOne("abcd", "abc"))

    def testInfix(self):
        self.assertTrue(offByOne("abcd", "acd"))

    def testFalse(self):
        self.assertFalse(offByOne("abcd", "acb"))


def longestChain(words):
    word_len = {}
    for word in words:
        l = len(word)
        if l in word_len:
            word_len[l].append({'word': word, 'chain': 1})
        else:
            word_len[l] = [{'word': word, 'chain': 1}]

    max_chain = 1
    lengths = list(reversed(sorted(word_len.keys())))
    for i in range(1, len(lengths)):
        prev = lengths[i -1]
        cur = lengths[i]
        if prev == 1 + cur:
            for word_dict in word_len[cur]:
                matches = [wd for wd in word_len[prev] if offByOne(wd['word'], word_dict['word'])]
                if matches:
                    word_dict['chain'] += max([wd['chain'] for wd in matches])
                    if word_dict['chain'] > max_chain:
                        max_chain = word_dict['chain']
    return max_chain


class TestStringChain(unittest.TestCase):

    def testStringChain(self):
        self.assertEqual(4, longestChain(['a', 'b', 'ba', 'bca', 'bda', 'bdca']))

    def testNoChain(self):
        self.assertEqual(1, longestChain(['a', 'b', 'cd', 'efg', 'ghi', 'abcg']))


if __name__ == '__main__':
    unittest.main()
