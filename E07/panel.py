import unittest

class Lamp(object):
    def __init__(self, visible, unvisible):
        self.visible = visible
        self.unvisible = unvisible
        self.has_disappeared = False
        self.possible_num = []
        self._analyze()

    def is_valid(self):
        if len(self.possible_num) != 0:
            if self.possible_num[0] == '-':
                return False
            else:
                return True
        else:
            return False

    def getMax(self, head=True, last=False):
        if self.is_valid():
            if head and not last:
                if self.possible_num[-1] == 0:
                    return '-'
            return self.possible_num[-1]
        elif self.has_disappeared:
            return ''
        else:
            return '-'

    def getMin(self, head=True, last=False):
        if self.is_valid():
            if head and not last:
                if self.possible_num[0] == 0:
                    if len(self.possible_num) >= 2:
                        return self.possible_num[1]
                    else:
                        return '-'
            return self.possible_num[0]
        elif self.has_disappeared:
            return ''
        else:
            return '-'

    def _analyze(self):
        patterns = [
          [int('3f', 16), int('40', 16)],
          [int('06', 16), int('79', 16)],
          [int('5b', 16), int('24', 16)],
          [int('4f', 16), int('30', 16)],
          [int('66', 16), int('19', 16)],
          [int('6d', 16), int('12', 16)],
          [int('7d', 16), int('02', 16)],
          [int('27', 16), int('58', 16)],
          [int('7f', 16), int('00', 16)],
          [int('6f', 16), int('10', 16)],
          [int('00', 16), int('7f', 16)]
        ]
        for num in range(0,11):
            if patterns[num][0] == ( patterns[num][0] | self.visible ) and patterns[num][1] == ( patterns[num][1] | self.unvisible ):
                if num == 10:
                    self.has_disappeared = True
                else:
                    self.possible_num.append(num)
        if len(self.possible_num) == 0 and not self.has_disappeared:
            self.possible_num.append('-')

class Panel(object):
    def __init__(self, visible, unvisible):
        self.visibleList = visible.split(':')
        self.unvisibleList = unvisible.split(':')
        self.lampList = []

    def solve(self):
        for visible, unvisible in zip(self.visibleList, self.unvisibleList):
            lamp = Lamp(int(visible,16), int(unvisible,16))
            self.lampList.append(lamp)

        min_head = True
        max_head = True
        last = False
        ans_max = ''
        ans_min = ''
        for index, lmp in enumerate(self.lampList):
            if index == len(self.lampList) - 1:
                max_head = False
                min_head = False
                last = True
            if lmp.is_valid():
                maxNum = lmp.getMax(max_head, last)
                max_head = False
                if min_head:
                    if lmp.has_disappeared:
                        minNum = ''
                    else:
                        minNum = lmp.getMin(min_head, last)
                        min_head = False
                else:
                    minNum = lmp.getMin(min_head, last)
                    if minNum == '' or minNum == '-':
                        return '-'

            else:
                if lmp.has_disappeared:
                    if max_head and not last:
                        maxNum = ''
                    else:
                        return '-'

                    if min_head and not last:
                        minNum = ''
                    else:
                        return '-'
                else:
                    return '-'

            if maxNum == '-' or minNum == '-':
                return '-'
            else:
                ans_min += str(minNum)
                ans_max += str(maxNum)

        return ans_min + ',' + ans_max

class PanelTest(unittest.TestCase):
    def test_solve(self):
        for test_num, dataset in enumerate(TEST_DATA.split('\n')):
            dataset = dataset.rstrip()
            view, expected = dataset.split(' ')
            visible, unvisible = view.rstrip(',').split(',')
            panel = Panel(visible, unvisible)
            actual = panel.solve()
            print('---TEST {0}---'.format(test_num))
            self.assertEqual(expected, actual)
            print('OK')

TEST_DATA='''06:4b:46:64:6d,79:20:10:10:02, 12345,13996
41:00,3e:01, -
00:00,79:79, 1,11
02:4b:46:64,20:20:10:10, 1234,3399
06:2f:3f:27,40:00:00:40, 1000,7987
00:3d:2d:26,00:00:00:00, 600,9899
40:20:10,00:00:00, 200,998
00:00:00,40:20:10, 1,739
08:04:02:01,00:00:00:00, 2000,9999
00:00:00:00,08:04:02:01, 1,7264
08:04:02:01,01:02:04:08, -
04:02:01,02:04:08, 527,627
04:02:01:40:10,02:04:08:10:20, 52732,62792
00:30:07,00:01:10, -
37,00, 0,8
3f,40, 0,0
3f:3f,40:40, -
00:3f,40:40, 0,70
00:3f,38:00, 0,18
18,07, -
08,10, 3,9
42,11, 4,4
18,05, -
10:00,0b:33, -
14:02,00:30, 61,83
00:1a,3d:04, 2,2
00:28,38:40, 0,10
20:08:12,4f:37:24, -
02:4c:18,00:00:04, 132,992
4a:7a:02,10:00:30, 381,983
00:00:06,0b:11:08, 1,47
04:20:2c:14,39:08:50:09, -
02:06:02:02,00:31:18:11, 1111,9174
00:04:48:50,03:02:20:02, 526,636
00:58:42:40,00:20:08:12, 245,9245
08:08:60:00:32,76:67:02:16:04, -
00:00:00:08:02,06:1a:3b:20:11, 21,34
08:58:12:06:12,10:20:20:00:04, 32202,92292
00:10:74:4e:10,10:04:02:00:24, 2632,92692
44:76:0a:00:0c:44,39:08:11:09:02:11, -
00:00:44:0a:04:00,79:06:02:04:79:28, 5211,6211
30:02:02:2c:0e:02,00:08:04:02:20:01, 612531,872634
00:00:04:10:00:60,25:19:01:02:24:00, 1624,44629
04:18:54:38:00:14:70,10:65:09:01:6c:00:0d, -
18:04:26:20:04:24:1a,02:21:50:48:02:08:00, 6177540,6177678
00:08:34:00:00:64:06,18:24:02:00:61:08:61, 260141,7269141
00:02:0a:04:4a:00:20,18:21:24:02:04:60:19, 125214,7126214
'''

if __name__ == '__main__':
    unittest.main()
