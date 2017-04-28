

#reverse returns the plaintext in reversed order
def reverse(plaintext):
    return plaintext[::-1]

##print reverse("he boot too big")







#caesar shifts each character in the plaintext by a given shift through the alphabet (mod 26)
#letters not in the set alphabet are ignored

import string

def caesar_en(plaintext, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = string.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)

def caesar_de(encryption, shift):
    return caesar_en(encryption, -shift)

##print caesar_de(caesar_en("he boot too big", 5), 5)






#substitution returns the plaintext with substitutions made based upon a given dictionary

def substitution_en(plaintext, replacements):
    for key, value in replacements.iteritems():
        plaintext = plaintext.replace(key, value)
    return plaintext

def substitution_de(cipher, replacements):
    return substitution_en(cipher, {value: key for key, value in replacements.iteritems()})

##key = {"h": "4", "e": "3", "x": "X"}
##print substitution_de(substitution_en("this is a test plaintext", key), key)






#convert_to_ascii returns a string comprised of concatinated 2-digit ascii values of each char in plaintext, seperated by a space
def convert_to_ascii(plaintext):
    return " ".join([str(ord(char)) for char in plaintext])

def convert_from_ascii(cipher):
    return "".join(chr(int(num)) for num in cipher.split(" "))

##print convert_from_ascii(convert_to_ascii("he boot too big"))






plaintext = "he boot too big XD"


cipher = substitution_en(caesar_en(reverse(plaintext), 10), {"o": "0"})

attempt = reverse(caesar_de(substitution_de(cipher, {"o": "0"}), 10))

print cipher

print attempt












