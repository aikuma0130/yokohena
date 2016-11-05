import unittest


class Pentagon(object):
    def __init__(self):
        self.now = [ 500, 500 ]
        self.t = [ 0, 2 ]
        self.tr = [ 2, 1 ]
        self.tl = [ -2, 1 ]
        self.dr = [ 1, -2 ]
        self.dl = [ -1, -2 ]

    def _swap(self):
        self.t = self.t[::-1]
        self.tr = self.tr[::-1]
        self.tl = self.tl[::-1]
        self.dr = self.dr[::-1]
        self.dl = self.dl[::-1]

    def _reverse(self, i):
        self.t[i] = -self.t[i]
        self.tr[i] = -self.tr[i]
        self.tl[i] = -self.tl[i]
        self.dr[i] = -self.dr[i]
        self.dl[i] = -self.dl[i]

    def move(self, direction):
        #print(self.now)
        if direction == 't':
            self.now[0] += self.t[0]
            self.now[1] += self.t[1]
            self._reverse(0)
            self._reverse(1)
        elif direction == 'tr':
            self.now[0] += self.tr[0]
            self.now[1] += self.tr[1]
            self._swap()
            self._reverse(1)
        elif direction == 'dl':
            self.now[0] += self.dl[0]
            self.now[1] += self.dl[1]
            self._swap()
            self._reverse(1)
        elif direction == 'tl':
            self.now[0] += self.tl[0]
            self.now[1] += self.tl[1]
            self._swap()
            self._reverse(0)
        elif direction == 'dr':
            self.now[0] += self.dr[0]
            self.now[1] += self.dr[1]
            self._swap()
            self._reverse(0)

import collections
class Field(object):

    def __init__(self):
        self.direction = collections.deque(['t','tr','dr','dl','tl'])
        self.field = [ [None] * 1000 for i in range(1000) ]
        self.pentagon = Pentagon()
        self.field[self.pentagon.now[0]][self.pentagon.now[1]] = 0
        self.move_count = 0

    def solve(self, inputs):
        for command in inputs:
            if command == 'F':
                self.move_count += 1
                self.pentagon.move(self.direction[0])
                #print('move to {0}'.format(self.direction[0]))
                if self.is_visited(self.pentagon.now):
                    return str(self.move_count) + ',' + str(self.field[self.pentagon.now[0]][self.pentagon.now[1]])
                else:
                    self.field[self.pentagon.now[0]][self.pentagon.now[1]] = self.move_count
                    self.change_direction('t')
            elif command == 'c':
                self.change_direction('c')
            elif command == 'a':
                self.change_direction('a')
        return '-'

    def is_visited(self, now):
        if self.field[now[0]][now[1]] == None:
            return False
        else:
            return True

    def change_direction(self, direction):
        if direction == 't':
            if self.direction[0] == 't':
                pass
            elif self.direction[0] == 'tr':
                self.direction.rotate(-1)
            elif self.direction[0] == 'tl':
                self.direction.rotate(1)
            elif self.direction[0] == 'dr':
                self.direction.rotate(1)
            elif self.direction[0] == 'dl':
                self.direction.rotate(-1)
        elif direction == 'a':
            self.direction.rotate(1)
        elif direction == 'c':
            self.direction.rotate(-1)

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
            print('inputs: {0}'.format(inputs))
            print('actual: {0}'.format(actual))
            self.assertEqual(actual, expect)
            print('OK')
        # For one testcase
        #for test_num, line in enumerate(TEST_DATA.split('\n')):
        #    if test_num == 12:
        #        line = line.rstrip()
        #        inputs, expect = line.split(' ')
        #        field = Field()
        #        actual = field.solve(inputs)
        #        print('----TEST {0}----'.format(test_num))
        #        print('inputs: {0}'.format(inputs))
        #        print('actual: {0}'.format(actual))
        #        self.assertEqual(actual, expect)
        #        print('OK')

if __name__ == '__main__':
    unittest.main()
