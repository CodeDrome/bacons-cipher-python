
def encipher(plaintext, target_text):

    """
    Encipher plaintext to target text with binary 0
    as lower case and binary 1 as upper case
    """

    # remove all non-alphabetic characters
    # from plaintext and convert to upper case
    plaintext = ''.join([c for c in plaintext if c.isalpha()]).upper()

    # get a string of 0s and 1s representing the
    # formatting of the enciphered message letters
    binary_string = _string_to_bit_pattern(plaintext)

    # format the target text letters as upper or lower case
    # according to the bit pattern
    enciphered = _cased_text_from_bit_pattern(target_text, binary_string)

    return enciphered


def decipher(enciphered):

    """
    Decipher enciphered text assuming lower case letters
    represent binary 0 and upper case letters represent binary 1
    """

    print("\nDeciphering\n===========\n")

    # remove everything except letters
    enciphered = ''.join([c for c in enciphered if c.isalpha()])

    length = len(enciphered)
    letter_quintet = ""
    bit_pattern = ""
    deciphered = []

    for i in range(0, length, 5):

        # grab next 5 letters
        letter_quintet = enciphered[i: i+5]

        # get corresponding string of 5 bits
        bit_pattern = _letter_quintet_to_bit_pattern(letter_quintet)

        # get letter corresponding to bit pattern
        letter = chr(int(bit_pattern, 2) + 65)

        print(f"{letter_quintet} {bit_pattern} {letter}")

        deciphered.append(letter)

    return "".join(deciphered)


#------------------------------------------------------------
# "PRIVATE" FUNCTIONS
#------------------------------------------------------------

def _string_to_bit_pattern(string):

    """
    Convert string of letters to string of
    corresponding 5-bit patterns
    """

    binary_list = []
    bit_pattern = ""

    for letter in string:
        # get ASCII code, subtract 65 and format as 5 bit string
        bit_pattern = format(ord(letter) - 65, '05b')
        binary_list.append(bit_pattern)

    return "".join(binary_list)


def _cased_text_from_bit_pattern(target_text, binary_pattern):

    """
    Set case of target text according to string of 5-bit patterns

    0 => lower case
    1 => upper case

    Non-alpha characters are skipped
    """

    cased_text = []

    index = 0

    for bit in binary_pattern:

        while not target_text[index].isalpha():
            cased_text.append(target_text[index])
            index += 1

        if bit == "0":
            cased_text.append(target_text[index].lower())
        else:
            cased_text.append(target_text[index].upper())

        index += 1

    return "".join(cased_text)


def _letter_quintet_to_bit_pattern(letter_quintet):

    """
    Convert string of 5 letters to corresponding bit pattern
    Lower case => 0
    Upper case => 1
    """

    bit_pattern = []

    for c in letter_quintet:

        if(c >= "a" and c <= "z"):
            bit_pattern.append("0")
        elif(c >= "A" and c <= "Z"):
            bit_pattern.append("1")

    return "".join(bit_pattern)
