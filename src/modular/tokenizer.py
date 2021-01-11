# https://docs.python.org/3/library/re.html

from dataclasses import dataclass
import re

@dataclass( frozen = True, order = True )
class Token():
    _type: str
    _value: str
    _line: int
    _column: int


def tokenize( code, keywords = {} ):
    """ Tokenize

    Parameters
    ----------
    code String
        String to parse
    keywords Dictionary        
        {'IF', 'THEN', 'ENDIF', 'FOR', 'NEXT', 'GOSUB', 'RETURN'}

    """

    # What to look out for.
    token_specification = [
        ( 'NUMBER',   r"\d+(\.\d*)?" ),  # Integer or decimal number
        ( 'ASSIGN',   r"=" ),            # Assignment operator
        ( 'END',      r";"),             # Statement terminator
        ( 'ID',       r"[A-Za-z]+" ),    # Identifiers
        ( 'OP',       r"[+\-*/]" ),      # Arithmetic operators
        ( 'NEWLINE',  r"\n" ),           # Line endings
        ( 'SKIP',     r"[ \t]+" ),       # Skip over spaces and tabs
        ( 'MISMATCH', r"." ),            # Any other character
    ]

    # Token Regex
    token_regex = "|".join( "(?P<%s>%s)" % pair for pair in token_specification )

    # Iterate
    line_num = 1
    line_start = 0
    for match in re.finditer( token_regex, code ):
        kind = match.lastgroup
        value = match.group()
        column = match.start() - line_start
        if kind == 'NUMBER':
            value = float( value ) if '.' in value else int( value )
        elif kind == 'ID' and value in keywords:
            kind = value
        elif kind == 'NEWLINE':
            line_start = match.end()
            line_num += 1
            continue
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError( f'{value!r} unexpected on line {line_num}' )
        yield Token( kind, value, line_num, column )