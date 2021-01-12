import operator
from random import randrange

from ..modular.tokenizer import tokenize


class Roll:
    """ Roll
    
    Handles returning a random number, given a count and size of dice.

    Parameters
    ----------
    count Int
        Number of dice
    size Int
        Numbers on the dice

    """

    __slots__ = [ "_count", "_size" ]


    def __init__( self, count, size ):
        self._count = count
        self._size = size

    
    def roll( self ):
        """ 'Rolls' our dice.

        Returns
        -------
        int Roll
            The result of our randomization.

        """
        t = 0
        for _ in range( 0, self._count ):
            t += randrange( 0, self._size ) + 1
        return t


class Dice:
    """ Dice

    Parameters
    ----------
    string Statement
        A dice statement, in the format of #d#+#+d# or the such that is parsed for rolling.

    """

    __slots__ = [ "_sequence" ]


    def __init__( self, statement ):

        # Init our sequence
        self._sequence = []

        # Iterate our statement, turning it into a sequence of commands.
        for token in tokenize( statement.lower(), specifications = [ ( "DICE", r"\d*[d]\d*" ) ] ):

            # Dice is in #d# format, need to ensure # exists and add.
            if token._type == "DICE":

                dice_split = token._value.split( "d" )

                if not dice_split[ 0 ]:
                    dice_split[ 0 ] = 1
                if not dice_split[ 1 ]:
                    dice_split[ 1 ] = 1

                # If we don't include an operation between dice, this inserts add.
                if len( self._sequence ) and type( self._sequence[ len( self._sequence ) - 1 ] ) in ( int, tuple ):
                    self._sequence.append( operator.add )
                
                self._sequence.append( Roll( int( dice_split[ 0 ] ), int( dice_split[ 1 ] ) ) )

            # For operation we only care about add and subtract.
            elif token._type == "OP":

                if token._value == "+":
                    self._sequence.append( operator.add )

                elif token._value == "-":
                    self._sequence.append( operator.sub )

                else:
                    raise RuntimeError( f"Unexpected OP Token of value {token._value}" )

            # Standard number, add as is.
            elif token._type == "NUMBER":
                self._sequence.append( token._value )

            # Anything else... is a problem.
            else:
                raise RuntimeError( f"Unexpected {token}" )
        


    def roll( self ):
        """ Roll

        Returns
        -------
        int
            The rolled value of this die.
        
        """
        #return ( self._count * ( randrange( self._size ) + 1 ) ) + self._modifier

        sequence = self._sequence.copy()

        for i in range( 0, len( sequence ) ):
            if isinstance( sequence[ i ], Roll ):
                sequence[ i ] = sequence[ i ].roll()

        total = sequence[ 0 ]
        for i in range( 0, len( sequence ) ):
            if type( sequence[ i ] ) != int:
                total = sequence[ i ]( total, sequence[ i + 1 ] )

        return total