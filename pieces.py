# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 11:25:24 2021

@author: hermi
"""
#pieces 

class Piece:
    def __init__(self, colour, name, points, location =1):
        self.colour = colour
        self.name = name
        self.points = points
        self.loc = location
    def move(self):
        pass
        
        
class Pawn(Piece):
    def __init__(self, colour, shape = "P"):
      super().__init__(colour, "pawn", 1)
      self.shape = shape
     
    def move(self):
        super().move()
        #return new_loc
      

class Rook(Piece):
    pass
    
class Knight(Piece):
    pass
    
class Bishop(Piece):
    pass

class Queen(Piece):
    pass
    
class King(Piece):
    pass
