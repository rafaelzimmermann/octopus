import collections
from adafruit_hid.keycode import Keycode

Key = collections.namedtuple('Key', ['char', 'code'])

key_map = {
    'A': Key('A', Keycode.A),
    'a': Key('a', Keycode.A),
    'B': Key('B', Keycode.B),
    'b': Key('b', Keycode.B),
    'C': Key('C', Keycode.C),
    'c': Key('c', Keycode.C),
    'D': Key('D', Keycode.D),
    'd': Key('d', Keycode.D),
    'E': Key('E', Keycode.E),
    'e': Key('e', Keycode.E),
    'F': Key('F', Keycode.F),
    'f': Key('f', Keycode.F),
    'G': Key('G', Keycode.G),
    'g': Key('g', Keycode.G),
    'H': Key('H', Keycode.H),
    'h': Key('h', Keycode.H),
    'I': Key('I', Keycode.I),
    'i': Key('i', Keycode.I),
    'J': Key('J', Keycode.J),
    'j': Key('j', Keycode.J),
    'K': Key('K', Keycode.K),
    'k': Key('k', Keycode.K),
    'L': Key('L', Keycode.L),
    'l': Key('l', Keycode.L),
    'M': Key('M', Keycode.M),
    'm': Key('m', Keycode.M),
    'N': Key('N', Keycode.N),
    'n': Key('n', Keycode.N),
    'O': Key('O', Keycode.O),
    'o': Key('o', Keycode.O),
    'P': Key('P', Keycode.P),
    'p': Key('p', Keycode.P),
    'Q': Key('Q', Keycode.Q),
    'q': Key('q', Keycode.Q),
    'R': Key('R', Keycode.R),
    'r': Key('r', Keycode.R),
    'S': Key('S', Keycode.S),
    's': Key('s', Keycode.S),
    'T': Key('T', Keycode.T),
    't': Key('t', Keycode.T),
    'U': Key('U', Keycode.U),
    'u': Key('u', Keycode.U),
    'V': Key('V', Keycode.V),
    'v': Key('v', Keycode.V),
    'W': Key('W', Keycode.W),
    'w': Key('w', Keycode.W),
    'X': Key('X', Keycode.X),
    'x': Key('x', Keycode.X),
    'Y': Key('Y', Keycode.Y),
    'y': Key('y', Keycode.Y),
    'Z': Key('Z', Keycode.Z),
    'z': Key('z', Keycode.Z),
    ' ': Key(' ', Keycode.SPACE),
}


def parse(value: str):
    result = []
    for c in value:
        if c in key_map:
            result.append(key_map[c])
    return result
