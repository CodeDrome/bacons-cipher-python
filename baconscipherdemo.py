import baconscipher


def main():

    print("------------------")
    print("| codedrome.com  |")
    print("| Bacon's Cipher |")
    print("------------------\n")

    plaintext = "Knowledge and human power are synonymous."

    target_text = "There were under the law, excellent King, both daily sacrifices and freewill offerings; the one proceeding upon ordinary observance, the other upon a devout cheerfulness: in like manner there belongeth to kings from their servants both tribute of duty and presents of affection.  In the former of these I hope I shall not live to be wanting, according to my most humble duty and the good pleasure of your Majesty’s employments: for the latter, I thought it more respective to make choice of some oblation which might rather refer to the propriety and excellency of your individual person, than to the business of your crown and state."

    enciphered = baconscipher.encipher(plaintext, target_text)
    print("Enciphered\n==========")
    print(enciphered)

    deciphered = baconscipher.decipher(enciphered)
    print("\nDeciphered\n==========")
    print(deciphered)


if __name__ == "__main__":
    main()
