from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad , unpad 
import getpass

simple_key= get_random_bytes(32)

salt= b'\xc40\xab\xcc\xe1\x1d\x01q \x9b\xa9\xfe\x08\xa3\xd9\xe0\xfc-\x1f\x94\xad\xadbC\xfe\xca>\xfb\xd3vH\xea'
password= getpass.getpass("enter a password: ")

key= PBKDF2(password, salt, dkLen=32)

cipher= AES.new(key, AES.MODE_CBC)
# Prompt the user to input the message
message = getpass.getpass("Enter your message: ")

# Convert the input string to bytes
message_bytes = message.encode('utf-8')

# example message= b"hello secret world!" # b is neeeded for byte conversion
ciphered_data= cipher.encrypt(pad(message_bytes, AES.block_size))


choice=input("do you want to see your encrypted message?y/n: ")
if choice.lower()=="y":
    check=input("enter your password: ")
    if check==password:
        cipher= AES.new(key,AES.MODE_CBC, iv=cipher.iv)
        original= unpad(cipher.decrypt(ciphered_data), AES.block_size)
        if message_bytes==original:
            print(original.decode("utf-8"))
            exit(0)
        else:
            print("error in decryption")
    else:
        print("wrong password cannot decrypt data")
        print("encrypted data is:",ciphered_data)
elif choice.lower()=="n":
    ch=input("do you want to save the message?y/n")
    if ch.lower()=="y":
        with open("encrypted.bin", "wb") as f:
            f.write(cipher.iv)
            f.write(ciphered_data)
        f.close
        print("data stored successfully")
    else: 
        exit(0)
        
    
        
        
    



