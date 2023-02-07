#OBJECT ORIENTED PROGRAMING

#1st project
"""
class car():
    def __init__(self, model, color, hp, cylinder):
        self.model = model
        self.color = color
        self.hp = hp
        self.cylinder = cylinder

car1 = car("Kia-Sportage", "red", 110, 4)
car2 = car("Peugeot-2005","green", 90, 4)
"""


#2st project
"""
class employee():
    def __init__(self, name, surname,depertmant, no, salary, skills):
        print("employee class is working...")
        self.name = name
        self.surname = surname
        self.depertmant = depertmant
        self.no = no
        self.salary = salary
        self.skills = skills
    
    def showInfo(self):
        print(f'''
        ########################################################
        Name: {self.name}
        Surname:{self.surname}
        No: {self.no}
        Salary: {self.salary}
        Skills: {self.skills}
        ########################################################''')
    
    def upgradeSkills(self, newSkills):
            self.skills.append(newSkills)

class ceo(employee):
    def raiseSalary(self, extraMoney):
        self.salary += extraMoney

    def changeDepertmant(self, newDepertmant):
        self.depertmant = newDepertmant
    
employee1 = employee("yagmur", "akbas","software", "01234", 90000, ["pyhon","java", "C"])
employee1.showInfo()
employee1.upgradeSkills("php")
employee1.showInfo()

ceo1 = ceo("yagmur", "akbas","software", "01234", 90000, ["pyhon","java", "C"])
ceo1.changeDepertmant("ceo")
ceo1.raiseSalary(10000)
ceo1.showInfo()
"""


