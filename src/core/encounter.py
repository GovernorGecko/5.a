"""

    encounter.py

    TODO
    Build out base encounter tool


"""

class Encounter( object ):
    """ An Encounter, involving PCs and NPCs """

    __slots__ = [ "__pcs", "__npcs" ]

    
    def __init__( self ):
        
        self.__npcs = []
        self.__pcs = []


    def add_pc( self, name, initiative ):
        """ An Encounter, involving PCs and NPCs

        :param name: A string, the person's name.
        :param age: An int, the person's age.
        """

        self.__pcs.append( 
            [
                name,
                initiative
            ]
        )


    def initialize( self ):
        print( "hi" )

    
    def step( self ):
        print( "hi" )