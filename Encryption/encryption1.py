import string

text = 'hi buddy'  # reverse setting>> text = "op ibkkf"
shift = 7  # reverse setting>> shift = 26-7

alphabet = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
shifted = alphabet[shift:] + alphabet[:shift]  # 'hijklmnopqrstuvwxyz' 'abcdefg'
table = str.maketrans(alphabet,
                      shifted)  # {97: 104, 98: 105, 99: 106, 100: 107, 101: 108, 102: 109, 103: 110, 104: 111, 105: 112, 106: 113, 107: 114, 108: 115, 109: 116, 110: 117, 111: 118, 112: 119, 113: 120, 114: 121, 115: 122, 116: 97, 117: 98, 118: 99, 119: 100, 120: 101, 121: 102, 122: 103}

encrypted = text.translate(table)  # 'op ibkkf'

print(encrypted)
