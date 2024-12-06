class Operations:
    def InitialPermutation(self,plaintext):
        PermutationList = [plaintext[1],plaintext[5],plaintext[2],plaintext[0],plaintext[3],plaintext[7],plaintext[4],plaintext[6]]
        return ''.join(PermutationList)
    def InversePermutation(self,plaintext):
        InversePermutationList = [plaintext[3],plaintext[0],plaintext[2],plaintext[4],plaintext[6],plaintext[1],plaintext[7],plaintext[5]]
        return ''.join(InversePermutationList)
    def ExclusiveOr(self,bit1,bit2):
        if bit1 == bit2:
            return '0'
        else:
            return '1'
    def convertToBinary(self,numero):
        if numero == 0 :
            return '00'
        if numero ==1:
            return '01'
        if numero ==2 :
            return '10'
        if numero ==3:
            return '11'
    def convertToDecimal(self,numero):
        if numero == '00':
            return 0
        if numero == '01':
            return 1
        if numero =='10':
            return 2
        if numero =='11':
            return 3
    def F(self,side,key):
        expansionPermutation= [side[3],side[0],side[1],side[2],side[1],side[2],side[3],side[0]]
        keyAplication=''
        for i in range(len(expansionPermutation)):
            keyAplication+=self.ExclusiveOr(expansionPermutation[i],key[i])
        S0 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
        S1 = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]
        firstOutput= list(self.convertToBinary(S0[self.convertToDecimal(keyAplication[0]+keyAplication[3])][self.convertToDecimal(keyAplication[1]+keyAplication[2])]))
        secondOutput = list(self.convertToBinary(S1[self.convertToDecimal(keyAplication[4]+keyAplication[7])][self.convertToDecimal(keyAplication[5]+keyAplication[6])]))
        firstOutput.extend(secondOutput)
        finalPermutation = [firstOutput[1], firstOutput[3], firstOutput[2], firstOutput[0]]
        return ''.join(finalPermutation)

    def fk(self,key,msg):
        leftSide = msg[0:4]
        rightSide = msg[4:8]
        resultOfF =  self.F(rightSide,key)
        leftSideXOR=''
        for i in range(len(leftSide)):
            leftSideXOR+=self.ExclusiveOr(leftSide[i],resultOfF[i])
        return leftSideXOR + rightSide

    def switchSide(self, msg):
        leftSide = msg[0:4]
        rightSide = msg[4:8]
        msg = rightSide + leftSide
        return msg