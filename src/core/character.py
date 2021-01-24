
from .dice import DiceToken


__all__ = [ "Character" ]


class Character( object ):
    """ Character 

        Parameters
        -----------
        string name
            A string representing the name of this character
        Dice initiative_dice_statement
            Dice object to be rolled when initiative is handled
        bool managed
            Is this Character managed by the program?
    
    """


    __slots__ = [ "_initiative_dice_token", "_managed", "_name", "_uuid", "initiative" ]


    def __init__( self, name, initiative_dice_statement, managed ):
        self._initiative_dice_token = DiceToken( initiative_dice_statement )
        self._managed = managed
        self._name = name

        # To be set later
        self._uuid = None
        self.initiative = 0


    def __str__( self ):
        return f"{self._name} {self.initiative} {self._uuid}"


    def roll_initiative( self ):
        """ Rolls Initiative!

        Returns
        -------
        int
            Our initiative, after rolling.
        """

        return self._initiative_dice_token.roll()


# We gotta be included!
if __name__ == '__main__':
    pass