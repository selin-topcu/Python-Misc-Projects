import string

def ceasar(text, shift, alphabets):
    def shift_alphabet(alphabet): #'abcdefghijklmnopqrstuvwxyz'
        return alphabet[shift:] + alphabet[:shift] #'hijklmnopqrstuvwxyzabcdefg'

    shifted_alph = tuple(map(shift_alphabet, alphabets))
    final_alph = ''.join(alphabets) #'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    final_shifted_alph = ''.join(shifted_alph) #'hijklmnopqrstuvwxyzabcdefgHIJKLMNOPQRSTUVWXYZABCDEFG()*+,-./:;<=>?@[\\]^_`{|}~!"#$%&\''
    table = str.maketrans(final_alph, final_shifted_alph)
    return text.translate(table)


result_text = "Hi Guys"
print(ceasar(result_text, 7, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]))
