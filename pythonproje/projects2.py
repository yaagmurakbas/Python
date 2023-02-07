#IF ELSE
 
#1th project
"""
print('''***********************************************************
CALCULATOR
addition = +
subtraction = -
multiplication = *
dicision = /

***********************************************************''')
x = int(input("enyer the first number: "))
y = int(input("enter the second number: "))
operation = input("enter the operation: ")

if operation == "+":
    print(f"{x} {operation} {y} =  {x+y}")
elif operation == "-":
    print(f"{x} {operation} {y} =  {x-y}")
elif operation == "/":
    print(f"{x} {operation} {y} =  {x/y}")
elif operation == "*":
    print(f"{x} {operation} {y} =  {x*y}")
else:
    print("pls be sure about writing right number and operation sign")


"""


#2th project
"""
print('''***************************************************
userName = yaagmur
password = 14072002
***************************************************
''')
userName = input("enter the userName: ")
password = int(input("enter the password: "))

key = ("yaagmur", 14072002) 

if userName != key[0] and password == key[1]:
    print("user name is not correct but password is true")
elif userName == key[0] and password != key[1]:
    print("user name is true but password is not correct")
elif userName != key[0] and password != key[1]:
    print("user name and are false")
else:
    print("WELCOME")

"""


#3th project
"""
weight = int(input("enter user weight value: "))
height = int(input("enter user height value: "))

BMI = weight/(height**2)

if(BMI<=18.5):
    print(f"user BMI index: {BMI} therefore user is skinny")
elif(BMI<=25 and BMI>18.5):
    print(f"user BMI index: {BMI} therefore user is normal")
elif(BMI<=30 and BMI>25):
    print(f"user BMI index: {BMI} therefore user is fat")
elif(BMI>30):
    print(f"user BMI index: {BMI} therefore user is obez")

"""


#4th project
"""
x = int(input("enter 1th number: "))
y = int(input("enter 2th number: "))
z = int(input("enter 3th number: "))

if(x>y and x>z):
    print(f"the biggest number: {x}")
elif(y>x and y>z):
    print(f"the biggest number: {y}")
elif(z>x and z>y):
    print(f"the biggest number: {z}")
else:
    print("pls enter diffrent numbers")
"""


#5th project
"""
midterm1 = int(input("enter 1th midterm grade: "))
midterm2 = int(input("enter 2th midterm grade: "))
final = int(input("enter final grade: "))

average = ((midterm1*30)+(midterm2*30)+(final*40))/100
 
if(average>=90):
    print(f"user grade average:{average}  letter grade: AA")
elif(average>=85):
    print(f"user grade average:{average}  letter grade: BA")
elif(average>=80):
    print(f"user grade average:{average}  letter grade: BB")   
elif(average>=75):
    print(f"user grade average:{average}  letter grade: CB")
elif(average>=70):
    print(f"user grade average:{average}  letter grade: CC")
elif(average>=65):
    print(f"user grade average:{average}  letter grade: DC")   
elif(average>=60):
    print(f"user grade average:{average}  letter grade: DD")
elif(average>=55):
    print(f"user grade average:{average}  letter grade: FD")   
elif(average>=50):
    print(f"user grade average:{average}  letter grade: FF")
else:
    print("pls enter real values")
"""


#6th project 
"""
corner = int(input("enter corner value of the shape: "))

if (corner == 3):
    side1 = int(input("enter the 1th side measured value o triangle : "))
    side2 = int(input("enter the 2th side measured value o triangle : "))
    side3 = int(input("enter the 3th side measured value o triangle : "))
    
    if(side1==side2==side3):
        print("all sides of traingle is sequal to each other therefore TYPE: eskenar trianle")
    elif(((side1==side2) and (side1!=side3)) or ((side2==side3) and (side2!=side1)) or ((side1==side3) and (side1!=side2))):
        print("only 2 of the sides are equal one of them is diffrent therefore TYPE: ikizkenar triangle")
    else:
        print("each side of the triangle is diffrent to each other terefore TYPE: cesitkenat triangle")

elif(corner == 4):
    side1 = int(input("enter the 1th side measured value o quadrilateral : "))
    side2 = int(input("enter the 2th side measured value o quadrilateral : "))
    side3 = int(input("enter the 3th side measured value o quadrilateral : "))
    side4 = int(input("enter the 4th side measured value o quadrilateral : "))
    if(side1==side2==side3==side4):
        print("all side of quadrilateral is equal to each other therefore TYPE: square")
    elif(((side1==side2) and (side3==side4) and (side1!=side3)) or ((side2==side3) and (side1==side4) and (side2!=side1))):
        print("twos of side of the quadrilateral is equal to each other therefore TYPE: rectangle" )
    else:
        print("ya yamuktur ya cokkenar dortgendir abi usendim yazamam hepsini aaaaa")
"""

#6th project
"""
yas = int(input('yasinizi giriniz '))
isim = input('isim gir ulan ')
egitim = input('egitim durumun ne')
if yas>=18:
    if (egitim == 'lise') or (egitim == 'universite'):
        print(f'{isim} kisisi ehliyet alabilirsiniz') 
    else:
        print(f'{isim} kisisi egitim durumunuz yeterli deil')
else:
    print(f'{isim} kisisi yasiniz yeterli degil') 
"""

#6. PROJEDE EN BUYUK HATAMM EGER HEPSI ESITSE ZATEN EN BASTAKKI IF CALISIR ELIFLERDEKI DIKDORTGEN VE IKIZKENAR UCGEN KOSUL BLOKLARINDA
#SADECE ESIT OLANLARI VERMEM YETERLI BIRDE FARKLI OLANLARI CIKLAMAM GEREK YOKTU BU NEDNELE HATA YAPTIN 
#DIKKATT ETTTT

     



