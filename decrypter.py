import pyaes

def decrypt(data, key):
    aes = pyaes.AESModeOfOperationCTR(key)
    decrypted_data = aes.decrypt(data)
    return decrypted_data

with open('encrypted.txt', 'rb') as file:
    encrypted_text = file.read()

key = b'mysecretpassword'

decrypted_text = decrypt(encrypted_text, key)

with open('decrypted.txt', 'w') as file:
    file.write(decrypted_text.decode('utf-8'))

print("Texto descriptografado com sucesso!")
