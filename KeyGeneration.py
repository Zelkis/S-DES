
class Key:
    def __init__(self,Key):
        self.key = Key

    def keyGeneration(self):
        FirstPermutation = self.PermutationKey10(self.key)
        LeftShift1Bit = self.LeftShiftKey1(FirstPermutation)
        K1 = self.Pick8(LeftShift1Bit)
        LeftShift2Bits = self.LeftShiftKey2(LeftShift1Bit)
        K2 = self.Pick8(LeftShift2Bits)
        return [K1, K2]
    @staticmethod
    def PermutationKey10(key):
        permutationKeyList = [key[2],key[4],key[1],key[6],key[3],key[9],key[0],key[8],key[7],key[5]]
        return ''.join(permutationKeyList)

    def LeftShiftKey1(self, key):
        LeftList = list(key[0:5])
        RightList = list(key[5:len(key)])
        LeftShiftedList = [0 for i in range(len(LeftList))]
        RightShiftedList = [0 for i in range(len(RightList))]
        for number in range(0, len(LeftList)):
            if number == 0:
                LeftShiftedList.pop(len(LeftList) - 1)
                LeftShiftedList.insert(len(LeftList) - 1, LeftList[number])
            else:
                LeftShiftedList.pop(number - 1)
                LeftShiftedList.insert(number - 1, LeftList[number])
        for number in range(0, len(RightList)):
            if number == 0:
                RightShiftedList.pop(len(RightList) - 1)
                RightShiftedList.insert(len(RightList) - 1, RightList[number])
            else:
                RightShiftedList.pop(number - 1)
                RightShiftedList.insert(number - 1, RightList[number])
        LeftShiftedList.extend(RightShiftedList)
        return ''.join(LeftShiftedList)

    def LeftShiftKey2(self, key):
        LeftList = list(key[0:5])
        RightList = list(key[5:len(key)])
        LeftShiftedList = [0 for i in range(len(LeftList))]
        RightShiftedList = [0 for i in range(len(RightList))]
        for number in range(0, len(LeftList)):
            if number == 0:
                LeftShiftedList.pop(len(LeftList) - 1)
                LeftShiftedList.pop(len(LeftList) - 2)
                LeftShiftedList.insert(len(LeftList) - 2, LeftList[number])
                LeftShiftedList.insert(len(LeftList) - 1, LeftList[number + 1])
            else:
                if number != 1:
                    LeftShiftedList.pop(number - 2)
                    LeftShiftedList.insert(number - 2, LeftList[number])
        for number in range(0, len(RightList)):
            if number == 0:
                RightShiftedList.pop(len(RightList) - 1)
                RightShiftedList.pop(len(RightList) - 2)
                RightShiftedList.insert(len(RightList) - 2, RightList[number])
                RightShiftedList.insert(len(RightList) - 1, RightList[number + 1])
            else:
                if number != 1:
                    RightShiftedList.pop(number - 2)
                    RightShiftedList.insert(number - 2, RightList[number])
        LeftShiftedList.extend(RightShiftedList)
        return ''.join(LeftShiftedList)

    def Pick8(self, key):
        KeyList = list(key)
        Pick8List = [KeyList[5], KeyList[2], KeyList[6], KeyList[3], KeyList[7], KeyList[4], KeyList[9], KeyList[8]]
        return ''.join(Pick8List)