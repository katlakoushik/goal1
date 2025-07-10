class Student:
    def __init__(self):
        self.__name=""
        self.__marks=0
    def setname(self,name):
        self.__name=name
    def getname(self):
        print(self.__name)
    def setmarks(self,marks):
        if 0<marks<=100:
            self.__marks=marks
        else:
            print("Error: marks should be 0 to 100")
    def getmarks(self):
        print(self.__marks)
stud=Student()
stud.setname("Alice")
stud.setmarks(89)
stud.getname()
stud.getmarks()
stud.setname("Koushik")
stud.setmarks(190)
stud.getmarks()