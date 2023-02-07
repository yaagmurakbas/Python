class Airway:
    name = "babanen"
    def __init__(self, code, startingPoint, finishPoint, passangerLimit, passenger):
        self.code = code
        self.startingPoint = startingPoint
        self.finishPoint = finishPoint
        self.passangerLimit = passangerLimit
        self.passenger = passenger
    def calculateEmptySeat(self):
        return(self.passangerLimit - self.passenger)                                                                                                                                                                                                                        

#class className :
#    degismesi gerekmeyen clasiin icindeki sabit degerler yani class object attribute
#    constructor olustumak icin  asadaki format kullanilir
#    def __init__(self, degisken paramerler virgulle sirala )   
#    burdaki self bizim object attributeslari atadigim seuysi yani ogenci adi vs)
#    burda object attributesleri tanimliycaz 
#          self.object attributes name = name bilgisini atar

p1 = Airway('TK54', 'ankara', 'istanbul', 300, 50)
p2 = Airway('TK84', 'antalya', 'istanbul', 350, 250)
print(f'p1 rmpty seat: {p1.calculateEmptySeat()}')
print(f'p1 code: {p1.code}, p1 capacty: {p1.passangerLimit}')
print(f'p2 code: {p2.code}, p2 capacty: {p2.passangerLimit}')

#updating
p1.code = 'YA1407'

print(p1)  #objemizin belirtilen adressini verir 
print(type(p1))  #type ollarak bakarsam bu person tipi olur


#EXAMPLE2
class Circle:
    pi = 3.14 
    def __init__(self, radius):
        self.cricleRadius = radius

    def circleAreacCalculator(self,):
        self.circleArea = self.cricleRadius**2 *self.pi 
        return self.circleArea

    def circumferenceCalculater(self):
        self.circumference = self.cricleRadius*2*self.pi
        return self.circumference

r1 = Circle(5)
print(f'cicle area:  {r1.circleAreacCalculator()}, circumference of the circle:  {r1.circumferenceCalculater()}')

