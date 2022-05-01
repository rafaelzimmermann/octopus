from adafruit_hid.keycode import Keycode

key_map = {
    'A': Keycode.A,
    'a': Keycode.A,
    'B': Keycode.B,
    'b': Keycode.B,
    'C': Keycode.C,
    'c': Keycode.C,
    'D': Keycode.D,
    'd': Keycode.D,
    'E': Keycode.E,
    'e': Keycode.E,
    'F': Keycode.F,
    'f': Keycode.F,
    'G': Keycode.G,
    'g': Keycode.G,
    'H': Keycode.H,
    'h': Keycode.H,
    'I': Keycode.I,
    'i': Keycode.I,
    'J': Keycode.J,
    'j': Keycode.J,
    'K': Keycode.K,
    'k': Keycode.K,
    'L': Keycode.L,
    'l': Keycode.L,
    'M': Keycode.M,
    'm': Keycode.M,
    'N': Keycode.N,
    'n': Keycode.N,
    'O': Keycode.O,
    'o': Keycode.O,
    'P': Keycode.P,
    'p': Keycode.P,
    'Q': Keycode.Q,
    'q': Keycode.Q,
    'R': Keycode.R,
    'r': Keycode.R,
    'S': Keycode.S,
    's': Keycode.S,
    'T': Keycode.T,
    't': Keycode.T,
    'U': Keycode.U,
    'u': Keycode.U,
    'V': Keycode.V,
    'v': Keycode.V,
    'W': Keycode.W,
    'w': Keycode.W,
    'X': Keycode.X,
    'x': Keycode.X,
    'Y': Keycode.Y,
    'y': Keycode.Y,
    'Z': Keycode.Z,
    'z': Keycode.Z,
    ' ': Keycode.SPACE,

}


def parse(value: str):
    result = []
    for c in value:
        if c in key_map:
            result.append(key_map[c])
    return result
