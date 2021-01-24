
from .character import Character

class Monster( Character ):

    def __init__( self, name, dice_initiative ):
        super().__init__( name, dice_initiative, True )
        print( "monster" )