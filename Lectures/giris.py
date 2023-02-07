print(2+2)
print(type(2.1))
if(3>2):
    print("babanen")
#bu bir komuttur 

# ister 
# boyle 
# yazarim 

"""
ister boyle yazarim 
"""
x, y, z = "babanen", "nin ", "amk"
print(x+y+z)   # toplu atama ve yazdirma 

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits    # bir listedekileri atama ve yazdirma 
print(f"{x} {y} {z}")

#print alirken farkli turdeki variablelari + kullanarak bastuiramasin ama bunu  , kullanarak yapabilirsin 
x = 5
y = "babanen"
#print(x +y)    error verirken 
print(x,y)     #error vermez


x = "1"
def function():
   #global x     #bunu kullanirsan function icinde local bir x uzerinde degilde global x uzerinde calisir 
    x  = "2"
    print(x)
function()
print(x)    


#x = ["apple", "banana", "cherry"]	list
#x = ("apple", "banana", "cherry")	tuple
#x = {"name" : "John", "age" : 36}	dict
#x = {"apple", "banana", "cherry"}	set

import random 
print(random.randrange(1,10))
