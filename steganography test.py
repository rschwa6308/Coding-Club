from random import choice


words = open("words.txt").read().split("\n")


index = 6893
length = 10000


message = "this is a test message!"






def mess_en(plaintext, index, length):
    mess = [choice(words) for x in range(length)]

    composite = " ".join(mess[:index] + plaintext.split(" ") + mess[index:])

    return composite



def mess_de(cipher, index):
    composite = cipher.split(" ")
    return " ".join(composite[index: index+10])




cipher = mess_en(message, index, length)

print cipher

print "\n\n"

print mess_de(cipher, index)



