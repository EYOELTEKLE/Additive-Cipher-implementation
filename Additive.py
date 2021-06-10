#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:    Implementation of Additive cipher for both encryption and decryption
#
# Author:      Eyoel Tekle
#
# Created:     30/03/2021
# Copyright:   (c) Eyoel Tekle 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#This simple program uses the additive cipher approach for encryption and decryption

#Mapper List is created

map = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# encryption function was created to implement additive cipher
def encrypt(plaintext,key):
    #converts the whole plain text to lowecase letters so as to map with the mapper function

    plaintext = plaintext.lower()

     #Empty list was initialized

    encrypte = []

    #iterate over the whole characters of the string
    for i in range(0,len(plaintext),1):

        #check if there is a spacing between the letters if not continue mapping
        if plaintext[i] != " ":

            #map the character value to the mapper list using index function
            ind = (map.index(plaintext[i]))

            #perform the additive cipher algo
            c = (ind + int(key)) % 26

            #store the newly encrypted character
            shifter = map[c]

            #push it to the list
            encrypte.append(shifter)

            #if there is spacing skip current loop
        else:
            pass

        #convert the list to string using the function listToString
    encrypted = listToString(encrypte)
    return encrypted

#function for decryption using additive cipher
def decrypt(decrypttext,key):
    #converts the decryptedtext to lowecase letters so as to map with the mapper function

    decrypttext = decrypttext.lower()

     #Empty list was initialized

    decrypte = []

    #iterate over the whole characters of the string
    for i in range(0,len(decrypttext),1):

        #check if there is a spacing between the letters if not continue mapping
        if decrypttext[i] != " ":

            #map the character value to the mapper list using index function
            ind = (map.index(decrypttext[i]))

            #check if it needs additive inverse using variable x
            x = ind - int(key)

            if x >= 0:
                #perform the additive cipher algo
                c = (ind - int(key)) % 26

                #store the newly plaintext character
                shifter = map[c]

                    #push it to the list
                decrypte.append(shifter)
            else:

                c = (ind - int(key)) + 26

                shifter = map[c]

                    #push it to the list
                decrypte.append(shifter)

            #if there is spacing skip current loop
        else:
            pass

        #convert the list to string using the function listToString
    decrypted = listToString(decrypte)
    return decrypted

def listToString(s):

    # initialize an empty string
    str1 = ""

    # return string
    return (str1.join(s))
while True:

    mode = int(input(" Please select mode of operation for the additive cipher?   ****Press 1 for encryption or press 2 for decryption?***"))
    if mode == 1:
        key = input("please enter the encryption key for the additive cypher ?")

        plaintext = input("please enter the plaintext ")

        print("The encrypted message is ",encrypt(plaintext,key))
    elif mode == 2:
        key = input("please enter the decryption key for the additive cypher ?")

        plaintext = input("please enter the encrypted message ")

        print("The plaintext message is ",decrypt(plaintext,key))
    else:
        print("Please choose the right Value")
