class Animal: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
        self.age = 0 

    def move(self, direction):
        print(f'Moving to {direction}. <<< NOT INPLEMENTED YET >>>')

    def breed(self, x,y):
        return Animal(x,y)
    
class Zebra(Animal):
    def move(self, occupancy_grid):
        print('<<<not implemented>>>')