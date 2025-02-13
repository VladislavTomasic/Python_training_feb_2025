def adunare(a, b):
    return a+b

print(adunare(10,20))


##clasa / sablon / template
class Operatii:
    def adunare(self, a, b):
        return a+b


##obiect
obiect = Operatii()
print(obiect.adunare(10,20))