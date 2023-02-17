#Programmer: Elaine George
#Date: 2/17/2023
#Purpose: Decrypts data encrypted via the paired encrypt.py file
from cryptography.fernet import Fernet
import os
import base64

#Given a filename string and an encryption object, produce an encrypted version of that file
#TODO: it may behoove us to instead encrypt and decrypt in chunks, as of now it will crash with files larger than ram can store in memory
#Note to self: Fernet is not intended for large-scale encryption, we cant use the same chunk size to decrypt as every encrypted chunk is inherintly larger than it's decrypted counterpart:
#Replace fernet/find a workaround
def decrypt(file,fernet):
    f = open(file,'rb')
    fd = open(file[len("encrypted_"):],'wb')
    bytesArr = f.read()
    bytesDecrypt = fernet.decrypt(bytesArr)
    fd.write(bytesDecrypt)
    f.close()
    os.remove(file)
    fd.close()
    
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
            if file not in ("gelai-encrypt.py","gelai-decrypt.py", "pass.bin") and file.startswith("encrypted_"):
                decrypt(file,fernet)

#Running encrypt.py creates a pass.bin file, we use it to decrypt the then encrypted files. This 'consumes' pass.bin so to speak
if os.path.exists("pass.bin"):
    f = open("pass.bin",'rb')
    key = f.read()
    fernet = Fernet(key)
    recr(fernet)
    f.close()
    os.remove("pass.bin")
    input("press any key to exit...")
else:
    print("Pass.bin not Found")
    input("press any key to quit...")
