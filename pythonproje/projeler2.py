
#wordinator
"""
def wordsinator(word):
    i = 0
    while i < len(word):
        print(word[i])
        i += 1

userword = input('enter the word: ')
wordsinator(userword)
#OLDU


#2 sayi arasinda sayi bulucuinator
a=int(input('enter the first number: '))
b=int(input('enter the secent number: '))
for i in range(int(a)+1,int(b)):
    print(f'sayi {i}')
print() 
#OLDU 
"""

#asalsayinator
"""
def asalsayinator(number):
    a=0
    for i in range(2,int(number)):
        if number%i==0:
            a= a+1
        else:
    if a==0:
        print('sayiniz asaldir')
    else:
        print('sayiniz alsal degildir')


usernumber = int(input('enter the number: '))   
asalsayinator(usernumber)
#OLMADI
"""

#hesap makinesinator
"""
def hesapinator(num1, num2, work):
    if work =='+':
        result = num1+num2
        return result
    elif work =='-':
        result = num1-num2
        return result
    elif work =='*':
        result = num1*num2
        return result
    elif work =='/':
        result = float(num1)/float(num2)
        return result        


usernumber1 = int(input('enter the first number: '))
usernumber2 = int(input('enter the secont number: '))
userwork = input('choose your prosses: (+ - * / )    ') 
print(hesapinator(usernumber1, usernumber2,userwork))
#OLDU
"""

#bmi calculator
"""
def kiloinator(weight, height):
    index = weight/((height/100)**2)
    print(f'your index is {round(index,2)}')
    if index <=18.5:
        return 'skinny'
    elif index<=24.9:
        return 'normal '
    elif index<=29.9:
        return 'little fat'
    elif index<=39.9:
        return 'obez'
    else:
        return 'ultra obez olcen amk' 

userweight = float(input('enter your weight: '))
userhight = float(input('enter your height: '))
print(f'your index is {kiloinator(userweight,userhight) } ')
#OLDU 10 KILO VERMEM LAZIM AMK 
"""

#TICTAC GAME YAPCAM INS
"""
"""

#ADAM ASMACA YAPCAM INS
'''
import random

resim = ["""
   +---+
   |   |
       |
       |
       |
       |
--------""","""
   +---+
   |   |
   O   |
       |
       |
       |
--------""","""
   +---+
   |   |
   O   |
   |   |
       |
       |
--------""","""
   +---+
   |   |
   O   |
  /|   |
       |
       |
--------""","""
   +---+
   |   |
   O   |
  /|   |
       |
       |
--------""","""
   +---+
   |   |
   O   |
  /|   |
  /    |
       |
--------""","""
   +---+
   |   |
   O   |
  /|   |
  /    |
       |
--------"""]

word = random.choice(["python", "django", "terminal", "linux", "windows", "baskabirkod"])
usertry = 7
pic=0
useranswers=[]
x = 0
y = 0

for b in range(usertry): 
    answer = input('enter your answer: ')
    print(useranswers)
    y=y+1
    if answer =='exit':
        exit()    

    for index,char in enumerate(word):
        print(char)
        if char == answer:
            x = x+1
            print(f'you found the letter {char}')
            useranswers.append(answer)  
            break

    useranswers.append(answer)
    if x<=y:
        print(f'you didnt find the letter ')
        print(resim[int(pic)])
        pic = pic+1
        usertry= usertry - 1  
else: 
    print(f'LOOOSERR the answers is {word}')
#olmadiiii
'''
 