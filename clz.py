
import keyclass



key = keyclass.load_key()

#encrypt file
f = open("encrypt me.mp3", "rb")
keyclass.encrypt_message(f.read())
f.close()

#decrypt File
f = open('encoded.file', 'rb')
keyclass.decrypt_message(f.read())
f.close()
