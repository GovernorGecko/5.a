
import operator
import random

from modular.tokenizer import tokenize

statements = "4-6d1-12D1+5d1+1"

sequence = []

class Roll:

    def __init__( self, count, size ):
        self.count = count
        self.size = size
    
    def roll( self ):
        t = 0
        for _ in range( 0, self.count ):
            t += random.randrange( 0, self.size ) + 1
        return t


for token in tokenize( statements.lower(), specifications = [ ( "DICE", r"\d*[d]\d*" ) ] ):

    if token._type == "DICE":

        dice_split = token._value.split( "d" )

        if not dice_split[ 0 ]:
            dice_split[ 0 ] = 1
        if not dice_split[ 1 ]:
            dice_split[ 1 ] = 1

        # If we don't include an operation between dice, this inserts add.
        if len( sequence ) and type( sequence[ len( sequence ) - 1 ] ) in ( int, tuple ):
            sequence.append( operator.add )
        
        sequence.append( Roll( int( dice_split[ 0 ] ), int( dice_split[ 1 ] ) ) )


    elif token._type == "OP":

        if token._value == "+":
            sequence.append( operator.add )

        elif token._value == "-":
            sequence.append( operator.sub )

        else:
            raise RuntimeError( f"Unexpected OP Token of value {token._value}" )

    elif token._type == "NUMBER":

        sequence.append( token._value )

    else:

        raise RuntimeError( f"Unexpected {token}" )


    print( token )

print( sequence )

def handle_operation( operation, x, y ):
    if isinstance( x, Roll ):
        x_val = x.roll()
    else:
        x_val = x
    if isinstance( y, Roll ):
        y_val = y.roll()
    else:
        y_val = y
    return operation( x_val, y_val )

total = 0    
for i in range( 0, len( sequence ) ):
    if isinstance( sequence[ i ], Roll ):
        sequence[ i ] = sequence[ i ].roll()

for i in range( 0, len( sequence ) ):
    if type( sequence[ i ] ) != int:
        sequence[ i + 1 ] = sequence[ i ]( sequence[ i - 1 ], sequence[ i + 1 ] )


print( sequence )
print( total )

#for s in sequence:
    #if 
