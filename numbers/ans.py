#!/usr/bin/env python

DIGIT = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
TEEN = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
TEN = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
ORDER = ['', 'thousand', 'million', 'billion', 'trillion']

def printnum(num):
    order = 0
    ans = []

    if num == 0:
        return DIGIT[num]

    # import pdb; pdb.set_trace()

    while num > 0:
        ans.append(ORDER[order])
        order += 1

        cur_ten = num % 100
        if 9 < cur_ten < 20:
            ans.append(TEEN[cur_ten - 10])
        else:
            cur_digit = cur_ten % 10
            if cur_digit > 0:
                ans.append(DIGIT[cur_digit])
            ans.append(TEN[cur_ten // 10])

        cur_hundred = num % 1000
        if cur_hundred > 100:
            ans.append('hundred')
            ans.append(DIGIT[cur_hundred // 100])

        num = num // 1000

    return ' '.join(reversed(filter(len, ans)))

def main():
    T = int(raw_input())
    for i in range(T):
        print 'Case #%s: %s' % (i+1, printnum(int(raw_input())))

import unittest

class TestPrintNum(unittest.TestCase):

    def testPrintNum(self):
        self.assertEqual(printnum(0), 'zero')
        self.assertEqual(printnum(9), 'nine')
        self.assertEqual(printnum(12), 'twelve')
        self.assertEqual(printnum(32), 'thirty two')
        self.assertEqual(printnum(30), 'thirty')
        self.assertEqual(printnum(1234), 'one thousand two hundred thirty four')
        self.assertEqual(printnum(17319), 'seventeen thousand three hundred nineteen')
        self.assertEqual(printnum(107509), 'one hundred seven thousand five hundred nine')
        self.assertEqual(printnum(91107509), 'ninety one million one hundred seven thousand five hundred nine')


if __name__ == "__main__":
    # main()
    unittest.main()
