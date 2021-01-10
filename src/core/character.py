
from .dice import Dice


class Character( object ):
    """ Character 

        Parameters
        -----------
        string name
            A string representing the name of this character
        Dice dice_initiative
            Dice object to be rolled when initiative is handled
        bool managed
            Is this Character managed by the program?
    
    """


    __slots__ = [ "_dice_initiative", "_managed", "_name", "_uuid", "initiative" ]


    def __init__( self, name, dice_initiative, managed = True ):
        self._dice_initiative = dice_initiative
        self._managed = managed
        self._name = name

        # To be set later
        self._uuid = None
        self.initiative = 0


    def __str__( self ):
        return f"{self._name} {self.initiative} {self._uuid}"