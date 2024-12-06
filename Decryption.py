from KeyGeneration import Key
from Operations import Operations
class Decryption(Key,Operations):
    def __init__(self,cipherText,key):
        super().__init__(key)
        self.cipherText = cipherText
    def decrypt(self):
        keys=self.keyGeneration()
        decryptMsg = self.InitialPermutation(self.cipherText)
        decryptMsg = self.fk(keys[1], decryptMsg)
        decryptMsg=  self.switchSide(decryptMsg)
        decryptMsg= self.fk(keys[0], decryptMsg)
        decryptMsg = self.InversePermutation(decryptMsg)
        return decryptMsg

