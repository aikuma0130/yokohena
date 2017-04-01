import re
import unittest 


class Hexagon(object):
    def __init__(self, name):
        self.name = name
        self.right = chr( ord(name) + 1 )
        #self.left = chr( ord(name) - 1 )
        #self.up = chr( ord(name) - 5 )
        self.down = chr( ord(name) + 5 )

        if self.right in [ 'a', 'f', 'j', 'o', 's' ]:
            self.right = None
        #if self.left in [ 'e', 'i', 'n', 'r', 'w' ] or self.name == 'a':
        #    self.left = None
        #if self.up in [ 'e', 'n', 'w']:
        #    self.up = None
        if self.down in [ 'f', 'o', 'w'] or self.name in ['s', 't', 'u', 'v', 'w']:
            self.down = None


class Tetromino(object):

    def __init__(self, hexagons):
        self.B = [ 'mnrw', 'nrvw', 'pqru', 'mqrw', 'mnrv', 'ruvw' ]
        self.D = [ 'mrvw', 'nqrv', 'quvw', 'mnrw', 'mqru', 'pqrv' ]
        self.I = [ 'tuvw', 'hmrw', 'imqu' ]
        self.hexagons = hexagons
        self.now = hexagons
        self.now_str = "".join([ s.name for s in self.now ])

    def move(self):
        _hexagons = []
        for hexagon in self.hexagons:
            if hexagon.right != None:
                _hexagons.append(Hexagon(hexagon.right))
            else:
                break

        if len(_hexagons) == 4:
            self.now = _hexagons
            self.now_str = "".join([ s.name for s in self.now ])
            return True

        for hexagon in self.hexagons:
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
