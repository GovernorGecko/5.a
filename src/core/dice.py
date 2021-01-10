
from random import randrange


class Dice( object ):
    """ Dice

    """

    __slots__ = [ "_count", "_size", "_modifier" ]


    def __init__( self, count, size, modifier ):
        self._count = count
        self._size = size
        self._modifier = modifier


    def roll( self ):
        """ Roll

        Returns
        -------
        int
            The rolled value of this die.
        
        """
        return ( self._count * ( randrange( self._size ) + 1 ) ) + self._modifier