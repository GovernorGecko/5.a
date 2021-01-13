
from .character import Character

class Player( Character ):

    def __init__( self, name, dice_initiative ):
        super().__init__( name, dice_initiative, False )
        print( "player" )