import tkinter as tk

class Display:
    
    def __init__(self, hight, width):
      self.hight = hight
      self.width = width
      
    def run(args):
     pass
 
    def __del__(self):
        print('Destructor called.')
         

Display(10,10)
      
    