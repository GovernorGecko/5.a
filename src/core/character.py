"""

    character.py

"""

from .dice import Dice


class Character( object ):
    """ Character 
    
    """


    __slots__ = [ "_initiative", "_name", "uuid" ]


    def __init__( self, name, initiative ):
        self._initiative = initiative
        self._name = name