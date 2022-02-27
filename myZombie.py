import zombiedice

class myZombie : 
    def __init__(self , name):
        #All zombies must have names 
        self.name  = name
        
    def turn(self , gameState):
        #gameState is a dictionary with info about the current state of the game
        #You can choose to ignore it in your code
        
        diceRollResults = zombiedice.roll() #First Role
        #roll() returns a dictionary with keys 'brains' , 'shortgun' ,  and
        #'footsteps' with how many rolls of each type there were
        #The 'rolls' key is a list of (color , icon) tuples with the 
        # exact roll result information.
        # Examples of a roll() return value:
        