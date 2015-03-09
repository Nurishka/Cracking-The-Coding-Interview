class TaroJiroDividing(object):

    def getNumber(self, A, B):
        Taro = []
        Jiro = []

        while A % 2 == 0:
            Taro.append(A)
            A /= 2
        Taro.append(A)

        while B % 2 == 0:
            Jiro.append(B)
            B /= 2
        Jiro.append(B)

        res = 0
        for numi in Taro:
            for numj in Jiro:
                if numi == numj:
                    res += 1

        return res

        
