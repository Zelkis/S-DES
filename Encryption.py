from KeyGeneration import Key
from Operations import Operations

class Encryption(Key,Operations):
    def __init__(self,plaintext,key):
        super().__init__(key)
        self.plaintext = plaintext
    def encrypt(self):
        keys = self.keyGeneration()
        encryptMsg =self.InitialPermutation(self.plaintext)
        encryptMsg = self.fk(keys[0], encryptMsg)
        encryptMsg = self.switchSide(encryptMsg)
        encryptMsg = self.fk(keys[1], encryptMsg)
        encryptMsg = self.InversePermutation(encryptMsg)
        return encryptMsg


































