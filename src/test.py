# https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285
# https://www.debuggex.com/cheatsheet/regex/python

import re

from modular.tokenizer import tokenize

statements = "d10+12D5=1"

p = re.search( "\d*[d]\d*", statements.lower() )
print( p.group( 0 ) )

order = [
    "NUMBER",
    "ID",
    "NUMBER",
    "OP"
]

#for token in tokenize( statements ):
    #print( token._type )