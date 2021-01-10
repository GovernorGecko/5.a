"""

    Main

    TODO
    Encounter Tool
        Don't rely on input/output on console
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