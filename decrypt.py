import os
import pyaes

## Abrir o arquivo criptografado
file_name = "teste.txt.ramsomwaretroll"
file = open(file_name, "rb")
file_data = file.read()
file.close

## chave para descriptografia
key = b"ÜùæÿR(Ö»TªØ%õh'="
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## remove o arquivo criptografado
os.remove(file_name)

#cria o arquivo descriptografado
new_file = "teste.txt"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()