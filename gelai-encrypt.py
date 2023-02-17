#Programmer: Elaine George
#Date: 2/17/2023
#Purpose: Encrypts small files and generates a file with the decryption key
from cryptography.fernet import Fernet
import os
import base64

#Given a filename string and an encryption object, produce an encrypted version of that file
#TODO: it may behoove us to instead encrypt in chunks, as of now it will crash with files larger than ram can store in memory
#Note to self: Fernet is not intended for large-scale encryption, either replace it or look into workarounds.
def encr(file,fernet):
    f = open(file,'rb')
    fe = open("encrypted_" + file, 'wb')
    bytesArr = f.read()
    bytesEncrypt = fernet.encrypt(bytesArr)
    fe.write(bytesEncrypt)
    f.close()
    os.remove(file)
    fe.close()

#recursively run through a directory structure to pass file-names to the encryption function
def recr(fernet):
    listy = os.listdir()
    cwd = os.getcwd()
    for file in listy:
        if os.path.isdir(file):
            os.chdir(file)
            recr(fernet)
            os.chdir(cwd)
        else:
            if file not in ("gelai-encrypt.py","gelai-decrypt.py","pass.bin"):
                encr(file,fernet)
                
#generates a 32 byte base64 byte array to use as a key. Saves it in a pass.bin for easy storage and use in the decrypt.py file. If pass.bin already exists, than it is assumed that
#every file is encrypted. If new files are added, decrypt the directory and re-encrypt.
key = Fernet.generate_key()
if not os.path.exists("pass.bin"):
    fernet = Fernet(key)
    recr(fernet)
    file = open("pass.bin", "wb")
    file.write(key)
    file.close()
    input("press any key to quit...")
else:
    input("press any key to quit...")
