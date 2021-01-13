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
    Display Information
    Subtract HP
    Actions
    Disablers
    Map

"""

import os

from src.core.encounter import Encounter
from src.core.monster import Monster
from src.core.player import Player


dir_path = os.path.dirname( os.path.realpath( __file__ ) )

e = Encounter()
e.add( Monster( "Goblin", "d20+2" ) )
e.add( Monster( "Orc", "d20" ) )
c = Player( "Lizard", "d20+1" ) 
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

    elif i == "a":
        e.add( c )

    else:
        e.step()

"""
while True:

    command = input( "? " )

    if command == "x":
        break
"""