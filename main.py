from builtins import print
from cryptography.fernet import Fernet
from cryptography.
import rsa


(public_key,private_key)=rsa.newkeys(2048)

#Original file
f = open("abc.txt", "rb")
crypto=rsa.encrypt(f.read(), public_key)
f.close()

#Encrypted File
f = open('abcd.txt','wb')
f.write(crypto)
f.close()

#Decrypting File
f = open('abcd.txt','rb')
temp = f.read()
result = rsa.decrypt(temp, private_key).decode()
f.close()

#Save result
f = open('result.txt','w')
f.write(result)

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
