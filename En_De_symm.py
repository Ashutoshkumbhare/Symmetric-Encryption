from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# the key must be of multiple of 16,we canalso use os.urandom(16) fn() here.
key = (b'ashutoshashutosh')
# since we are using CRT mode we need iv i.e initialising variable Hence we are using CTR we don't need of padding
iv = (b'kumbharekumbhare')
detalis = Cipher(algorithms.AES(key), modes.CTR(iv), default_backend())


def encryption(text):
    # this fn() simply takes a argument which is a simple human readable text and return in encrypted form
    string = text
    simple_string = detalis.encryptor()
    cipher_text = simple_string.update(string) + simple_string.finalize()
    return cipher_text


def encrypt_file(file_name):
    # this fn() takes a file name extract the data from the file and pass it to the encryption()
    fil1 = open(file_name, "rb")
    r = fil1.read()
    en_text = encryption(r)
    fil1.close()
    #######################
    # this will creat a same name of file with .enc included in it.
    fil1 = open(file_name + ".enc", "wb")
    fil1.write(en_text)
    os.remove(file_name)
    fil1.close()
    print("all done")


def decryption(text):
    org = text
    en_string = detalis.decryptor()
    org_string = en_string.update(org) + en_string.finalize()
    return org_string


def decrypt_file(file_name):
    fil1 = open(file_name, "rb")
    r = fil1.read()
    de_text = decryption(r)
    fil1.close()
    os.remove(file_name)
    #######################
    # [:-4] will delete last 4 alphabets fro the name of the file and return it back.
    fil1 = open(file_name[:-4], "wb")
    fil1.write(de_text)
    fil1.close()
    print("all done")

#just pass file name which u want to encrypt or decrypt to.
#encrypt_file("file_name")   <--- for encrypt
#decrypt_file("file_name")   <--- for decrypt
