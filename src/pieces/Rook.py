#!/usr/bin/python3

from pieces.Piece import Piece

chessCardinals = [(1,0),(0,1),(-1,0),(0,-1)]

class Rook(Piece):

    def availableMoves(self,x,y,gameboard ,Color = None):
        if Color is None : Color = self.Color
        return self.AdNauseum(x, y, gameboard, Color, chessCardinals)