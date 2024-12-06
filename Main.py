from Encryption import Encryption
from Decryption import Decryption
teste1 = Encryption('01100011','1010000111')
print('Mensagem em texto plano no teste1: 01100011')
print(f'Mensagem criptografada no teste1: {teste1.encrypt()}')
decryption1  = Decryption(teste1.encrypt(),'1010000111')
print(f'Mensagem descriptograda no teste1:{decryption1.decrypt()} \n')
teste2 = Encryption('00010001','1010000010')
print('Mensagem em texto plano no teste2: 00010001')
print(f'Mensagem criptografada no teste2: {teste2.encrypt()}')
decryption2  = Decryption(teste2.encrypt(),'1010000010')
print(f'Mensagem descriptograda no teste2:{decryption2.decrypt()} \n ')
teste3 = Encryption('01010101','1110011001')
print('Mensagem em texto plano no teste3: 01010101')
print(f'Mensagem criptografada no teste3: {teste3.encrypt()}')
decryption3  = Decryption(teste3.encrypt(),'1110011001')
print(f'Mensagem descriptograda no teste3:{decryption3.decrypt()} \n ')
teste4 = Encryption('11101011','0000100000')
print('Mensagem em texto plano no teste4: 11101011')
print(f'Mensagem criptografada no teste4: {teste4.encrypt()}')
decryption4  = Decryption(teste4.encrypt(),'0000100000')
print(f'Mensagem descriptograda no teste4:{decryption4.decrypt()} \n ')






