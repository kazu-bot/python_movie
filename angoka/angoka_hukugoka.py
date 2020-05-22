#暗号化と複合化

import string
import random

from Crypto.Cipher import AES

#plaintextの内容を読み込んで暗号化
print(AES.block_size)
print(string.ascii_letters)
key=''.join(
    random.choice(string.ascii_letters) for _ in range(AES.block_size)
)
iv=''.join(
    random.choice(string.ascii_letters) for _ in range(AES.block_size)
)
# plaintext = 'sdla;djk;aljfklajfkaj'
with open('plaintext.txt','r') as f,open('enc.dat', 'wb') as e:
    plaintext = f.read()
    cipher = AES.new(key,AES.MODE_CBC,iv)
    padding_length = AES.block_size - len(plaintext) % AES.block_size
    plaintext += chr(padding_length) * padding_length
    cipher_text = cipher.encrypt(plaintext)
    e.write(cipher_text)

cipher2 = AES.new(key,AES.MODE_CBC,iv)
decrypted_text = cipher2.decrypt(cipher_text)
print(decrypted_text[-1])
print(decrypted_text[:-decrypted_text[-1]])

#plaintextの内容を読み込んで複合化
with open('enc.dat', 'rb') as f:
    cipher2 = AES.new(key, AES.MODE_CBC, iv)
    decrypted_text = cipher2.decrypt(f.read())
    print(decrypted_text[:-decrypted_text[-1]].decode('utf-8'))