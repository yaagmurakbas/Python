#MODULES
#explaining part
"""
import math                #import etme 
print(dir(math))           #icerigindeki fonksyonleri goreme
print(help(math))          #fonksyonlarin ne yaptigi hakkinda aciklama

math.factorial(8)          #burda faktoriel fonkstyonun kullanimini gorduk 5in faktoriyelini yazar
math.floor(5.6)            #burda floor fonksyonu yani verilen degerden kucuk en buyuk sayi yazdirilir

import math as matematik    #burda math modulunu nun adini degistirdik bundan sonra matematik degeri kullanilarak yazilicak
matematik.factorial(5)      #ayni sey yukardakiyle

from math import *          #icindeki tum fonksyonlari import eder bu sayede direk kullanabiliriz
factorial(5)                #module adi olan math kullanilmadan fonskyonlar kullanilir

from math import floor,cell #sadece 2 fonksyonu import eder
#bu 2 si haricinde digerlerini import etmez yani digerlerini kullanamazsin
"""

#1st project
"""
import random 
import time  

print('''#############################################
GUESS THE NUMBER 
BETWEEN 1-40
#############################################''')
randomNum = random.randint(1,40)                        #1 ile 40 arasinda 1 sayi uretti random modulundeki randint fonksyonu kullanilarak
chance= 5
while True:
    if chance>0:
        userNum = int(input(f"you have only {chance} chance\nenter the number:   "))
        print("PROCESSING...")
        time.sleep(1)

        if userNum==randomNum:
            print("\nHelal lan")
            break

        elif userNum>randomNum:
            chance-=1
            print(f"\ntoo high...\nchance:{chance}")
        elif userNum<randomNum:
            chance-=1
            print(f"\ntoo low...\nchance:{chance}")
    else:
        print(f"\nLoserrr the number is {randomNum}") 
        break
"""

#2st project EKSIKLER VAR
"""
import math
print('''***********************************************************
CALCULATOR
addition = +
subtraction = -
multiplication = *
dicision = /
***********************************************************''')
x = int(input("enyer the first number: "))
y = int(input("enter the second number: "))
opr = input("enter the operation: ")

if opr == "+":
    print(f"{x} {opr} {y} =  {sum(x,y)}")
elif opr == "-":
    print(f"{x} {opr} {y} =  {(x,y)}")
elif opr == "/":
    print(f"{x} {opr} {y} =  {module1.div(x,y)}")
elif opr == "*":
    print(f"{x} {opr} {y} =  {module1.mult(x,y)}")
else:
    print("pls be sure about writing right number and operation sign")
"""

#3st project
"""
import module1
print('''***********************************************************
CALCULATOR
addition = +
subtraction = -
multiplication = *
dicision = /
***********************************************************''')
x = int(input("enyer the first number: "))
y = int(input("enter the second number: "))
opr = input("enter the operation: ")

if opr == "+":
    print(f"{x} {opr} {y} =  {module1.add(x,y)}")
elif opr == "-":
    print(f"{x} {opr} {y} =  {module1.sub(x,y)}")
elif opr == "/":
    print(f"{x} {opr} {y} =  {module1.div(x,y)}")
elif opr == "*":
    print(f"{x} {opr} {y} =  {module1.mult(x,y)}")
else:
    print("pls be sure about writing right number and operation sign")
"""

#4st project
"""
import datetime
giris = '14 july 2002'
giris = datetime.datetime.strptime(giris, '%d %B %Y')
now = datetime.datetime.now()
print(now)
print(giris)   
year = now-giris 
year= year/360   
print(year)
"""
