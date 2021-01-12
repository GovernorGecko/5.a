
import operator
import uuid

from .character import Character


class Encounter( object ):
    """ An Encounter, involving Characters
    
    """


    __slots__ = [ "__characters", "__turn", "_running" ]

    
    def __init__( self ):        
        self.__characters = []        
        self.__turn = 0
        self._running = False


    def __str__( self ):
        return "\n".join( map( str, self.__characters ) )


    def add( self, character ):
        """ Adds a Character

        Parameters
        ----------
        character Character
            A Character object

        Returns
        -------
        ( bool, string )
            True/False to determine if successful, and a string of information.

        """

        # Character sent in is of correct type?
        if not isinstance( character, Character ):
            return False, "Variable passed in is not a Character object."

        # Create a UUID for this Character
        character._uuid = uuid.uuid1()

        # Add to our list
        self.__characters.append( character )

        # Return True
        return True, ""


    def get_current_turn( self ):
        """ Returns the Character object for who's turn it currently is.

        Returns
        -------
        ( bool, string, object )
            True/False, Message, and Character object or None on False from bool.

        """

        # We running an encounter?
        if not self._running:
            return False, "Encounter is not running, cannot return current turn.", None

        # We have characters?
        elif not self.has_characters():
            return False, "No characters added, cannot return current turn.", None

        # Okay, turn sanity check.
        elif self.__turn < 0 or self.__turn >= len( self.__characters ):
            return False, "Turn is beyond scope, rerun initialize", None

        # Everything is good.
        else:
            return True, "", self.__characters[ self.__turn ]


    def get_unmanaged_characters( self ):
        """ Returns a list of our unmanaged Character objects

        Return
        ------
        List
            Unmanaged Characters in an error. No error checking, since will return an empty or full List.

        """

        # List to Return
        unmanaged_characters = []

        # We have any characters?
        if self.has_characters:
            for character in self.__characters:
                if not character._managed:
                    unmanaged_characters.append( character )

        # Return
        return unmanaged_characters        


    def has_characters( self ):
        """ Have Characters in our List?

        Return
        ------
        bool
            True/False if we have characters in our List

        """
        return len( self.__characters ) > 0


    def initialize( self ):
        """ Initialize an encounter, sets to running and rolls initiative for managed characters.

        """

        # We have enough characters?
        if not self.has_characters():
            return False, "No Characters in List, please Add them."

        # Reset local turn
        self.__turn = 0

        # Set to running
        self._running = True

        # Iterate our characters, rolling init on managed characters
        for character in self.__characters:
            if character._managed:
                character.initiative = character._dice_initiative.roll()

        # Sort our Characters by Initiative
        self.__characters.sort( key = operator.attrgetter( "initiative" ), reverse = True )


    def remove( self, character ):
        """ Remove a Character

        Parameters
        ----------
        character Character
            Character object to remove
        
        Returns
        -------
        ( bool, string )
            True/False and message.

        """

        # Remove, if exists.
        if character in self.__characters:
            self.__characters.remove( character )

            # Running? And is this our turn?
            if self._running and self.get_current_turn()[ 2 ] == character:
                self.__turn += 1

            return True, ""

        # No workie
        return False, "Character not found."

    
    def step( self ):
        """ Step through the turns.

        """
        self.__turn = self.__turn + 1
        if self.__turn >= len( self.__characters ):
            self.__turn = 0


    def stop( self ):
        """ Stop the encounter.

        """
        self._running = False
