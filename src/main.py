"""

    Main

    TODO
    Encounter Tool
        Don't rely on input/output on console
        Dice Object Tokenizer https://docs.python.org/3/library/re.html

class Spam(object):
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

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        if not (v > 0): raise Exception("value must be greater than zero")
        self._value = v

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