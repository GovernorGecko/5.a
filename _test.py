"""

    NOTE
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


    TODO
    Encounter Tool
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

from src.core.character import Character
from src.core.dice import Dice
from src.core.encounter import Encounter

dir_path = os.path.dirname( os.path.realpath( __file__ ) )

e = Encounter()
e.add( Character( "Goblin", Dice( "d20+2" ) ) )
e.add( Character( "Orc", Dice( "d20" ) ) )
c = Character( "Lizard", Dice( "d20+1" ), False )
e.add( c )
cs = e.get_unmanaged_characters()
cs[ 0 ].initiative = 12
e.initialize()
#print( e )
#e.remove( c )
#print( e )

while True:

    worked, message, character = e.get_current_turn()

    i = input( f"{character._name}?" )

    if i == "x":
        break
    
    elif i == "d":
        e.remove( character )


    e.step()

"""
while True:

    command = input( "? " )

    if command == "x":
        break
"""