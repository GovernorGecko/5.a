"""

    character.py

"""

from .dice import Dice


class Character( object ):
    """ Character 
    
    """


    __slots__ = [ "_initiative", "_name", "initiative", "uuid" ]


    def __init__( self, name, initiative ):
        self._initiative = initiative
        self._name = name
        self.initiative = 0
        self.uuid = ""


    def __str__( self ):
        return f"{self._name} {self.initiative} {self.uuid}"