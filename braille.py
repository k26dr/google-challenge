def binbraille(c):
    SPACE = '000000'
    CAPITAL = '000001'
    letters = [32, 48, 36, 38, 34, 52, 54, 50, 20, 22]
    letters += [l+8 for l in letters]
    letters += [l+9 for l in letters[0:5]]
    letters.insert(22, 23)

    if c == ' ':
        return SPACE
    
    n = ord(c)
    caps = n < 91
    index = n - 65 if caps else n - 97
    braille = bin(letters[index])[2:]
    while len(braille) < 6:
        braille = '0' + braille
    return CAPITAL + braille if caps else braille
        

def answer(plaintext):
    braille = ''
    for c in plaintext:
        braille += binbraille(c)
        print(c, binbraille(c))
    return braille

question = "The quick brown fox jumped over the lazy dog"
correct = "000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100100010100110000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110"

for i,b in enumerate(answer(question)):
    if b != correct[i]:
        print(i)
