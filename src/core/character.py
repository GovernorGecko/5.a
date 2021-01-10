"""

    character.py

"""

from .dice import Dice


class Character( object ):
    """ Character 
    
    """


    __slots__ = [ "_initiative", "_managed", "_name", "_uuid", "initiative" ]


    def __init__( self, name, initiative, managed = True ):
        self._initiative = initiative
        self._managed = managed
        self._name = name
        self._uuid = None
        self.initiative = 0


    def __str__( self ):
        return f"{self._name} {self.initiative} {self._uuid}"