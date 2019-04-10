
import binascii

def toHex(word):
    hexString = ''
    for letter in word:
        hexString += hex(ord(letter))[2:]
    return (hexString)

def drag(xorCipher, word, length):

    #the word used in this iteration
    word = toHex(word)
    wordLen = len(word)

    for i in range (0, length, 2):

        try:
            xCSliced = hex(int(xorCipher[i:(i + wordLen)], 16) ^ int(word, 16))
            pt = xCSliced[2:]
            print("index: ", (i/2), binascii.unhexlify(pt))

        except binascii.Error as e:
            print("error: ", e, ". Moving on..")

    print("*" * 20)


if __name__ == '__main__':
    #ciphertext1
    x = ''

    #ciphertext2
    y= ''

    #truncate x or y to the minimum of their lengths
    trunc = min(len(x), len(y))
    y = y[:trunc]
    x = x[:trunc]

    #xor the two ciphertexts
    z = hex(int(x, 16) ^ int(y, 16))

    while(1):
        word = input(str("word: "))
        drag(z, word, trunc)
