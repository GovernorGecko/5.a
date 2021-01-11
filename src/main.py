"""

    Main

    TODO
    Encounter Tool
        Dice Object Tokenizer https://docs.python.org/3/library/re.html


    def __init__(self, description, value):
        self.description = description
        self.value = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, d):
        if not d: raise Exception("description cannot be empty")
        self._description = d


    Actions
        Standard
        Move
            Types
        Minor
    Disablers
        What affect actions?
    Map?
    

"""

import os

from core.character import Character
from core.dice import Dice
from core.encounter import Encounter

dir_path = os.path.dirname( os.path.realpath( __file__ ) )

e = Encounter()
e.add( Character( "Goblin", Dice( 1, 20, 2 ) ) )
e.add( Character( "Orc", Dice( 1, 20, 0 ) ) )
c = Character( "Lizard", Dice( 1, 20, 1 ), False )
e.add( c )
cs = e.get_unmanaged_characters()
cs[ 0 ].initiative = 12
e.initialize()
print( e )
#e.remove( c )
#print( e )
e.step()

"""
while True:

    command = input( "? " )

    if command == "x":
        break
"""