#steganography example


char_positions = [5, 6, 7, 8, 9, 4, 0, 9, 15, 55, 70]

cipher = "well hello my friends.  This is a test string!  The real message is hidden in here 0.o"

def get_message(cipher, char_positions):
    return "".join([cipher[pos] for pos in char_positions])




print get_message(cipher, char_positions)
