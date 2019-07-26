from Crypto import Random
from Crypto.Cipher import AES
import os
import os.path
from os import listdir
from os.path import isfile, join
import time
from .tools import encryptorTools



def main():

    key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
    enc = encryptorTools.Encryptor(key)

    if os.path.isfile('data.txt.enc'):
        while True:
            password = str(input("Enter password: "))
            enc.decrypt_file("data.txt.enc")
            p = ''
            with open("data.txt", "r") as f:
                p = f.readlines()
            if p[0] == password:
                enc.encrypt_file("data.txt")
                break

        while True:
            enc.clear()
            choice = int(input(
                "1. Press '1' to encrypt file.\n2. Press '2' to decrypt file.\n3. Press '3' to Encrypt all files in the directory.\n4. Press '4' to decrypt all files in the directory.\n5. Press '5' to exit.\n"))
            enc.clear()
            if choice == 1:
                enc.encrypt_file(str(input("Enter name of file to encrypt: ")))
            elif choice == 2:
                enc.decrypt_file(str(input("Enter name of file to decrypt: ")))
            elif choice == 3:
                enc.encrypt_all_files()
            elif choice == 4:
                enc.decrypt_all_files()
            elif choice == 5:
                exit()
            else:
                print("Please select a valid option!")
    
    else:
        while True:
            enc.clear()
            password = str(
                input("Setting up stuff. Enter a password that will be used for decryption: "))
            repassword = str(input("Confirm password: "))
            if password == repassword:
                break
            else:
                print("Passwords Mismatched!")
        f = open("data.txt", "w+")
        f.write(password)
        f.close()
        enc.encrypt_file("data.txt")
        print("Please restart the program to complete the setup")
        time.sleep(15)
