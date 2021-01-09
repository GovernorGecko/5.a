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


    __slots__ = [ "__characters", "__turn" ]

    
    def __init__( self ):        
        self.__characters = []
        self.__turn = -1


    def __str__( self ):
        return "\n".join( map( str, self.__characters ) )


    def add( self, character ):
        """ Adds a Character

        :param character: A Character class
        """

        # Create a UUID for this Character
        character.uuid = uuid.uuid1()

        # Add to our list
        self.__characters.append( character )


    def get_current_turn( self ):
        """ Returns the Character object for who's turn it currently is.

        """

        # Turn?
        if self.__turn >= 0 and self.__turn < len( self.__characters ):
            return self.__characters[ self.__turn ]
        return None


    def initialize( self ):
        """ Roll Initiative, store it

        """

        # We have enough characters?
        if len( self.__characters ) == 0:
            return False

        # Reset local turn
        self.__turn = -1

        # Iterate our characters, rolling init
        for character in self.__characters:
            character.initiative = character._initiative.roll()

    
    def step( self ):
        """ Step through the turns.

        """
        
        # Next turn!
        self.__turn = self.__turn + 1
        if self.__turn >= len( self.__characters ):
            self.__turn = 0