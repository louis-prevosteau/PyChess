#!/usr/bin/python3

from pieces.Piece import Piece

chessDiagonals = [(1,1),(-1,1),(1,-1),(-1,-1)]

class Bishop(Piece):

    def availableMoves(self,x,y,gameboard, Color = None):
        if Color is None : Color = self.Color
        return self.AdNauseum(x, y, gameboard, Color, chessDiagonals)