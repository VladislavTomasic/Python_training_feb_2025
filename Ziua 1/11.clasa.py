
# nume, prenume -> proprietati (ARE)
nume = "TIRIAC"
prenume = "ION"

#functii sau metode in clase - > scrie, invata

class Student:
    def __init__(self, nume, prenume) :
        self.nume = nume
        self.prenume = prenume
        pass
    def scrie(self):
        print("Studentul", self.nume, "scrie")

    def invata(self):
        print("Studentul invata")

student1 = Student("Tiriac", "Ion")
print(student1)
student1.scrie()
print(student1.nume)
student1.nume = "Andrei"
print(student1.nume)

student2 = Student("Halep", "Simona")
student2.scrie()