import re
import unittest
from pprint import pprint


class Field(object):
    def __init__(self):
        self.field = [ [ 0 for i in range(100) ] for i in range(100) ]

    def solve(self, inputs):
        pass


TEST_DATA='''FcFcFaF 3,0
FccFaaFcFcF -
ccFaF -
cFcFaaF -
aFccFcFcF 4,1
cFaFaFaFaaF 4,0
cFccFaFaaFaF 5,1
cFaaFaaFcFcFccF 5,2
aaFaFaaFaFccFaFccF 6,0
aaFaaFcFccFcFccFccFaF 6,1
aFccFccFaaFccFcFcFcFaF 7,4
ccFaaFaaFaFccFaaFaFcFccFaaF -
aaFaFaFcFaFaaFaFaFaaFccFaaFaaF 8,3
aaFccFaFaFccFaaFaaFaaFccFccFcFaFaF 13,10
aFaFaaFaaFaaFccFaFccFaFaaFccFccFaaFccF 11,0
ccFccFcFaaFaaFaFccFaaFaFcFaaFaaFcFcFcF 10,2
aaFaaFaaFccFccFaFaaFaaFaFccFcFcFccFaaFaFccFccF 10,3
ccFaFccFaaFaaFcFccFaFcFccFccFaaFccFaFaaFaFaFccF 11,3
cFcFaFaaFaFccFaaFcFaFaaFccFaFaaFccFaFcFaaFccFcF 12,0
cFaFaaFcFaaFaaFaFccFaaFcFaaFccFaaFccFaFcFccFaFaFaFcFcF 19,16
aFaFccFaaFccFccFaFccFaFaaFccFaaFccFcFccFaFaFccFaaFccFcF 15,11
aFccFccFccFaaFaaFcFcFaaFccFaFcFccFaaFaFcFaaFcFaFccFccFaFaF 23,20
cFaFaaFcFaFaaFccFccFaaFaFccFccFccFaFaFccFccFccFaaFcFcFcFaF 22,18
aFcFaFccFccFaFccFaaFaFaaFaaFaFcFaFcFcFcFaFaFaaFaaFaFaaFcFccFaF 14,4
cFaFaaFcFaFccFcFccFaFaaFaaFaFcFccFccFaFcFaFaaFccFaFaFccFcFaFaFaaF 22,19
aaFaaFaFcFccFaaFcFaaFccFaFaFcFaFaaFaFaFaFcFccFaFaaFcFcFccFccFccFcF 16,11
cFaaFaFcFaFaaFccFaaFaFccFccFaaFccFcFaFaaFaaFaFccFcFccFccFaFaaFcFcFaF 26,23
cFaaFccFaFcFaFcFaaFccFaFccFaaFcFaFaaFccFaaFccFcFaFaaFaFcFccFccFaFcFaaFccFcF -
ccFccFaaFaFccFaaFaaFcFccFaaFaFcFccFccFccFaFaaFcFaFccFaaFcFcFaFccFaFccFaaFaaFaF -
aaFccFaFccFccFaaFccFaFcFccFaFccFcFcFaFcFcFaaFaaFcFccFccFcFaFaaFaFcFcFaaFaaFaaF 19,5
aFaaFccFaFaaFaaFccFccFaFcFaaFaaFaaFccFaFccFaaFaaFaFccFccFcFaaFaFccFccFaFcFaaFccF -
aaFaFaaFcFccFccFaFcFaaFaaFaFccFccFccFaFaaFccFcFaaFccFaaFccFaaFccFccFccFcFaaFcFaaFccF 30,23
aaFccFaFaaFccFcFaFccFaFcFccFaaFccFaFcFaaFccFaaFaFccFccFccFcFccFaFccFcFaaFaFcFccFcFaFaaF 32,17
ccFcFcFaFaaFaFaaFccFcFccFaFcFaFccFaaFcFccFcFaaFcFaaFcFaaFaaFcFaaFaFaFaFaaFccFaaFcFcFaFaF 18,14
ccFaFaaFaaFcFaaFaaFaaFaaFaaFaFccFcFaaFaFcFccFaaFcFaFaaFccFccFaaFcFaaFaaFaaFccFaaFcFcFaFaFccFaFcFccF 17,0
aaFccFccFaFcFaFcFaFccFccFccFaFccFccFcFaFcFaaFccFcFccFccFaaFcFccFaaFccFccFaFccFcFcFaaFaFccFcFaaFaaFcF 24,11
aaFccFaFccFaaFaaFcFaFcFaFcFaaFaaFccFaFcFaFaaFcFaaFaFcFaaFccFcFaaFccFaaFccFaaFccFcFaFcFaFccFaaFaaFccFaaF -
aFaaFaFaaFcFccFaaFccFaFcFaaFccFccFcFcFaFaFcFccFcFccFaaFcFaFcFaaFcFaFaaFccFaaFccFaFaaFaFcFaFccFaFaaFaFaaF 17,14
aaFcFaaFccFaaFaaFcFaaFccFccFaFcFaFcFccFcFaaFaaFaFcFaFcFaaFcFaFaaFaFccFccFccFcFaFaFcFcFaFcFaaFcFaaFcFcFaaF 27,23
ccFaFccFaFcFaFccFcFaaFccFccFcFaFccFccFaaFaaFaFaaFcFaaFccFcFaaFcFccFaaFcFaFccFccFaFccFaaFaaFcFcFccFaFccFcFcF 25,18
cFcFccFaFaaFaaFccFccFcFccFccFaFcFaaFcFccFccFcFccFaFaFaFaFaFaaFaFcFaFccFcFccFaaFccFaaFccFcFaFaaFccFaFccFcFaaF 16,4
aFcFcFaaFcFaaFcFaFaaFaaFaaFaFcFccFccFccFaFaaFaFaaFaaFcFcFccFaFaaFcFaFaaFccFaaFcFccFcFcFccFaaFcFaFccFaaFaaFccF 19,15
ccFaaFcFaFccFaFccFaFcFaaFaaFccFaaFccFcFaFaFccFaFaaFaFaaFaFaaFaaFccFaaFaFcFaaFaFaFcFaaFcFaFaaFaaFcFccFaaFaFaFaF 22,17
aaFcFaaFaFcFccFccFaFaFccFaFaaFaFcFccFaaFaaFaaFcFccFccFaFaaFccFcFaFaFcFaaFcFcFcFccFccFaaFcFcFaFccFccFccFaaFcFaaFcF 14,5
cFcFaFccFaaFaFccFaFccFaaFaFccFaaFaaFccFaaFccFaaFccFaFaaFaFaFaaFaaFccFaFcFaaFcFcFaFaFcFcFcFaFaaFcFaFcFaaFccFccFcFaaFaFccF 10,1
ccFaFcFaaFcFccFaFccFaaFccFaaFaaFcFaaFccFaaFccFccFcFaaFaaFcFaaFccFaaFcFcFaaFaFaFccFcFaFaFaFccFccFccFccFccFccFcFcFccFccFcF 25,13
aFccFaFcFaFcFaaFaaFcFaaFccFaFaaFaFcFaFaaFaaFaaFccFaaFaaFccFccFccFccFccFaaFaFcFaFaFccFaFccFcFccFcFcFccFcFccFccFccFccFccFaF 18,8
cFaaFcFaaFaFcFccFaaFcFccFcFaFccFaaFaaFccFccFccFaFcFccFcFaaFcFcFccFcFccFaFaFccFccFcFaFaFaaFcFaFcFccFccFccFaaFaFaFccFcFccFccF 25,22
aaFcFccFcFaFcFaFaFcFccFaFaaFaFcFccFccFaaFccFccFaaFaaFccFaaFaaFccFaaFccFcFaaFaFcFaFcFccFaaFccFaFaFccFaaFcFaaFaFccFaaFaaFccFccFcFaF -
aFaaFccFccFaaFaaFccFccFaaFaaFaFcFccFaFcFaaFaFccFaaFccFaFcFaFccFaaFaaFaFccFaFaaFaaFcFaaFccFaaFcFaFccFccFaaFaaFaaFaaFccFcFccFaaFaFaaFaaF -
aaFcFccFccFaFccFaFccFaaFaaFaaFccFaaFaaFccFaaFccFaFaaFccFccFaaFcFccFaFccFcFaaFaFccFccFccFaaFaFccFccFaFaaFccFccFccFaaFccFccFaFaFcFaFccFccF -'''

class Test(unittest.TestCase):
    def test_solve(self):
        for test_num, line in enumerate(TEST_DATA.split('\n')):
            line = line.rstrip()
            inputs, expect = line.split(' ')
            field = Field()
            actual = field.solve(inputs)
            print('----TEST {0}----'.format(test_num))
            print('actual: {0}'.format(actual))
            self.assertEqual(actual, expect)
            print('OK')
        # For one testcase
        #for num, line in enumerate(TEST_DATA.split('\n')):
        #    if test_num == 14:
        #        line = line.rstrip()
        #        inputs = line.split(' ')[0]
        #        expect = line.split(' ')[1]
        #        black = inputs.split(',')[0]
        #        white = inputs.split(',')[1]
        #        board = Board(black, white)
        #        actual = board.solve()
        #        print('----TEST {0}----'.format(test_num))
        #        print('actual: {0}'.format(actual))
        #        board.show_board()
        #        self.assertEqual(actual, expect)
        #        print('OK')

if __name__ == '__main__':
    unittest.main()
