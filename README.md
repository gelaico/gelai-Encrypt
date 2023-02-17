# gelai-Encrypt
Recursive Directory Encrypter/Decrypter pair

Very simple: threw it together in an hour or two

Install python3

open a command window and run:

pip install -r path/to/requirements.txt
  
 
 Once installed, move gelai-encrypt to any directory you want secured and run it
 
 Running gelai-encrypt.py will create a file "pass.bin" in that directory. Decrypt.py must be in the same directory as pass.bin to operate. It will consume pass.bin
    
    NOTE: Files (Both decrypted and encrypted) must individually be storeable in memory, as of 2/17/2023 it will crash if you run out of RAM. Please be careful
    
    NOTE: Please, I recommend having an extra copy of the folder you want to encrypt saved prior to running it, just to ensure data won't get lost
     
          Run through an encryption and decryption cycle on the copy once just to make sure nothing goes wrong
