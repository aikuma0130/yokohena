import re
import unittest 


class Hexagon(object):
    def __init__(self, name):
        self.name = name
        self.right = chr( ord(name) + 1 )
        #self.left = chr( ord(name) - 1 )
        #self.up = chr( ord(name) - 5 )
        self.down = chr( ord(name) + 4 )

        if self.right in [ 'a', 'f', 'j', 'o', 's', 'x' ]:
            self.right = None
        #if self.left in [ 'e', 'i', 'n', 'r', 'w' ] or self.name == 'a':
        #    self.left = None
        #if self.up in [ 'e', 'n', 'w']:
        #    self.up = None
        if self.down in [ 'e', 'n', 'w' ] or self.name in ['s', 't', 'u', 'v', 'w']:
            self.down = None


class Tetromino(object):

    def __init__(self, hexagons):
        self.B = [ 'lqrv', 'nrvw', 'pqru', 'mqrw', 'mnrv', 'ruvw' ]
        self.D = [ 'mrvw', 'nqrv', 'quvw', 'mnrw', 'mqru', 'pqrv' ]
        self.I = [ 'tuvw', 'hmrw', 'imqu' ]
        self.hexagons = hexagons
        self.now = hexagons
        self.now_str = "".join([ s.name for s in self.now ])
        while True:
            if not self.move():
                break

    def move(self):
        _hexagons = []
        for hexagon in self.now:
            if hexagon.right != None:
                _hexagons.append(Hexagon(hexagon.right))
            else:
                break

        if len(_hexagons) == 4:
            self.now = _hexagons
            self.now_str = "".join([ s.name for s in self.now ])
            return True

        _hexagons = []
        for hexagon in self.now:
            if hexagon.down != None:
                _hexagons.append(Hexagon(hexagon.down))
            else:
                break

        if len(_hexagons) == 4:
            self.now = _hexagons
            self.now_str = "".join([ s.name for s in self.now ])
            return True

        return False

    def isB(self):
        if self.now_str in self.B:
            return True

    def isD(self):
        if self.now_str in self.D:
            return True

    def isI(self):
        if self.now_str in self.I:
            return True


class Solver(object):
    def __init__(self):
        pass

    def solve(self, inputs):
        hexagons = []
        sorted_inputs = [ s for s in inputs ]
        sorted_inputs.sort()
        for name in sorted_inputs:
            hexagons.append(Hexagon(name))
        tetromino = Tetromino(hexagons)

        if tetromino.isB():
            return "B"
        elif tetromino.isD():
            return "D"
        elif tetromino.isI():
            return "I"
        else:
            return "-"


TEST_DATA='''
/*0*/ test( "glmq", "B" );    
/*1*/ test( "fhoq", "-" );    
/*2*/ test( "lmpr", "-" );    
/*3*/ test( "glmp", "-" );    
/*4*/ test( "dhkl", "-" );    
/*5*/ test( "glpq", "D" );    
/*6*/ test( "hlmq", "-" );    
/*7*/ test( "eimq", "I" );    
/*8*/ test( "cglp", "-" );    
/*9*/ test( "chlq", "-" );    
/*10*/ test( "glqr", "-" );    
/*11*/ test( "cdef", "-" );    
/*12*/ test( "hijk", "-" );    
/*13*/ test( "kpqu", "B" );    
/*14*/ test( "hklm", "B" );    
/*15*/ test( "mqrw", "B" );    
/*16*/ test( "nrvw", "B" );    
/*17*/ test( "abfj", "B" );    
/*18*/ test( "abcf", "B" );    
/*19*/ test( "mrvw", "D" );    
/*20*/ test( "ptuv", "D" );    
/*21*/ test( "lmnr", "D" );    
/*22*/ test( "hklp", "D" );    
/*23*/ test( "himr", "D" );    
/*24*/ test( "dhil", "D" );    
/*25*/ test( "hlpt", "I" );    
/*26*/ test( "stuv", "I" );    
/*27*/ test( "bglq", "I" );    
/*28*/ test( "glmn", "-" );    
/*29*/ test( "fghm", "-" );    
/*30*/ test( "cdgk", "-" );    
/*31*/ test( "lpst", "-" );    
/*32*/ test( "imrw", "-" );    
/*33*/ test( "dinr", "-" );    
/*34*/ test( "cdin", "-" );    
/*35*/ test( "eghi", "-" );    
/*36*/ test( "cdeg", "-" );    
/*37*/ test( "bgko", "-" );    
/*38*/ test( "eimr", "-" );    
/*39*/ test( "jotu", "-" );    
/*40*/ test( "kotu", "-" );    
/*41*/ test( "lqtu", "-" );    
/*42*/ test( "cdim", "-" );    
/*43*/ test( "klot", "-" );    
/*44*/ test( "kloq", "-" );    
/*45*/ test( "kmpq", "-" );    
/*46*/ test( "qrvw", "-" );    
/*47*/ test( "mnqr", "-" );    
/*48*/ test( "kopt", "-" );    
/*49*/ test( "mnpq", "-" );    
/*50*/ test( "bfko", "-" );    
/*51*/ test( "chin", "-" );    
/*52*/ test( "hmnq", "-" );    
/*53*/ test( "nqrw", "-" );    
/*54*/ test( "bchi", "-" );    
/*55*/ test( "inrw", "-" );    
/*56*/ test( "cfgj", "-" );    
/*57*/ test( "jnpv", "-" );    
/*58*/ test( "flmp", "-" );    
/*59*/ test( "adpw", "-" );    
/*60*/ test( "eilr", "-" );    
/*61*/ test( "bejv", "-" );    
/*62*/ test( "enot", "-" );    
/*63*/ test( "fghq", "-" );    
/*64*/ test( "cjms", "-" );    
/*65*/ test( "elov", "-" );    
/*66*/ test( "chlm", "D" );    
/*67*/ test( "acop", "-" );    
/*68*/ test( "finr", "-" );    
/*69*/ test( "qstu", "-" );    
/*70*/ test( "abdq", "-" );    
'''


class Test(unittest.TestCase):
    def test_solve(self):
        for test_num, line in enumerate(TEST_DATA.split('\n')[1:-2]):
            test_num += 1
            first_pattern = re.compile('^.*test\(')
            end_pattern = re.compile('\); *')
            line = first_pattern.sub('', line)
            line = end_pattern.sub('', line)
            line = line.replace(' ', '')
            line = line.replace('"', '')
            inputs, expect = line.split(',')
            solver = Solver()
            actual = solver.solve(inputs)
            print('----TEST {0}----'.format(test_num))
            print('inputs: {0}'.format(inputs))
            print('actual: {0}'.format(actual))
            self.assertEqual(actual, expect)
            print('OK')
        # For one testcase
        #for test_num, line in enumerate(TEST_DATA.split('\n')[1:-2]):
        #    test_num += 1
        #    if test_num == 1:
        #        first_pattern = re.compile('^.*test\(')
        #        end_pattern = re.compile('\); *')
        #        line = first_pattern.sub('', line)
        #        line = end_pattern.sub('', line)
        #        line = line.replace(' ', '')
        #        line = line.replace('"', '')
        #        inputs, expect = line.split(',')
        #        solver = Solver()
        #        actual = solver.solve(inputs)
        #        print('----TEST {0}----'.format(test_num))
        #        print('inputs: {0}'.format(inputs))
        #        print('actual: {0}'.format(actual))
        #        self.assertEqual(actual, expect)
        #        print('OK')

if __name__ == '__main__':
    unittest.main()
