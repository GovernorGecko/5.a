"""

    Main

"""

import os

from core.character import Character
from core.dice import Dice
from core.encounter import Encounter

dir_path = os.path.dirname( os.path.realpath( __file__ ) )

e = Encounter()
e.add( Character( "Goblin", Dice( 1, 20, 2 ) ) )
e.add( Character( "Orc", Dice( 1, 20, 0 ) ) )
e.initialize()
print( e )
e.step()

"""
while True:

    command = input( "? " )

    if command == "x":
        break
"""