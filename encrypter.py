import pyaes

def encrypt(data, key):
    aes = pyaes.AESModeOfOperationCTR(key)
    encrypted_data = aes.encrypt(data)
    return encrypted_data

with open('text.txt', 'r') as file:
    plaintext = file.read()

key = b'mysecretpassword'

encrypted_text = encrypt(plaintext, key)

with open('encrypted.txt', 'wb') as file:
    file.write(encrypted_text)

print("Texto criptografado com sucesso!")


