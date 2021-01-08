'''

    Main

'''

import os

from core.encounter import Encounter

dir_path = os.path.dirname( os.path.realpath( __file__ ) )

e = Encounter()
e.add_pc( "test", 1 )
e.initialize()
e.step()