class Person():
    def __init__(self, fName,lName):
        self.FirstName = fName
        self.lastName = lName
        print('person created')
    def whoAmI(self):
        print('I am a person')    


class Student(Person):
    def __init__(self, firstName, LastName):
        Person.__init__(self, firstName, LastName)  #burda bunu yaparak hem persondaki initi hemde kendi initimi korudum
        print('student created')
#OVERRIDE DURUMU
#simdi bizim whiamI vardi eger eyni isimle bi fonksyon studente yazar ve onu cagirirsam o baskin gelir ve o calisir
#mesela cagirdim normalde I am a person yazardi ama 
#eger ayni isimli bir fonksyon studente kurar ve onu cagirirsam o zaman I am a student basar
    def whoAmI(self):
        print('I am a student')
#bunu yazdiktan sonra I am a students basar her whoami cagitrdigimda        

class Teacher:
    pass

p1 = Person('yagmur', 'akbas')
s1 = Student('yagmur', 'akbas')

p1.whoAmI()
s1.whoAmI()