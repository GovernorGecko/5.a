"""

    encounter.py

    TODO
    Build out base encounter tool
    Actions
        Standard
        Move
            Types
        Minor
    Disablers
        What affect actions?
    Map?


"""

import uuid

from .character import Character


class Encounter( object ):
    """ An Encounter, involving Characters 
    
    """


    __slots__ = [ "__characters" ]

    
    def __init__( self ):        
        self.__characters = []


    def __str__( self ):
        return str( self.__characters )


    def add( self, character ):
        """ An Encounter, involving PCs and NPCs

        :param name: A string, the person's name.
        :param age: An int, the person's age.
        """

        character.uuid = uuid.uuid1

        self.__characters.append( character )


    def initialize( self ):
        print( "hi" )

    
    def step( self ):
        print( "hi" )