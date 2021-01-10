"""

    encounter.py

"""

import operator
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
        character._uuid = uuid.uuid1()

        # Add to our list
        self.__characters.append( character )


    def get_current_turn( self ):
        """ Returns the Character object for who's turn it currently is.

        """

        # Turn?
        if self.has_characters() and self.__turn >= 0 and self.__turn < len( self.__characters ):
            return self.__characters[ self.__turn ]
        return None


    def get_unmanaged_characters( self ):
        """ Returns a list of our unmanaged Character objects

        """

        # List to Return
        unmanaged_characters = []

        # We have any characters?
        if self.has_characters:
            for character in self.__characters:
                if not character.managed:
                    unmanaged_characters.append( character )

        # Return
        return unmanaged_characters        


    def has_characters( self ):
        """ Have Characters in our List?

        """
        return len( self.__characters ) > 0


    def initialize( self ):
        """ Roll Initiative, store it

        """

        # We have enough characters?
        if not self.has_characters():
            return False

        # Reset local turn
        self.__turn = -1

        # Iterate our characters, rolling init
        for character in self.__characters:
            if character._managed:
                character.initiative = character._initiative.roll()

        # Sort our Characters by Initiative
        self.__characters.sort( key = operator.attrgetter( "initiative" ), reverse = True )


    def remove( self, character ):
        """ Remove a Character

        """

        # We have enough characters?
        if not self.has_characters():
            return False

        # We have a uuid?
        elif not hasattr( character, "_uuid" ):
            return False

        # Iterate, trying to remove.
        if character in self.__characters:
            self.__characters.remove( character )
            return True

        # No workie
        return False

    
    def step( self ):
        """ Step through the turns.

        """
        
        # Next turn!
        self.__turn = self.__turn + 1
        if self.__turn >= len( self.__characters ):
            self.__turn = 0