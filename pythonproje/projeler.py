
#crushinator
"""
import random

def crushinator():
    name =('cinar','atakan','taha','doruk','can','sahan')
    name2 = ('salak','mal','gerizekali','okuz','amci','sokuk')
    return(f'{random.choice(name)} {random.choice(name2)}dir aksini ibda eden vurduruyodur')

number=int(input('kac eski crusha sovsun  '))

while number>0:
    print(crushinator())
    number=number-1
    if number==0:
        break
#OLDUU
"""

#sicaklik degistirme
"""
print('if you will choose 1 that means f to c')
print('if you will choose 2 that means c to f')
option = int(input('1 or 2: '))

if option == 1:
    print((int(input('fahrenayt gir ulan'))-32)*1.8)
elif option == 2:
    print(int(input('celcius gir ulan'))*1.8+32)  
else:
    print('please choose only 1 or 2')    
#OLDUU
"""


#kac yil ay gun yasadin
"""
from datetime import *

info = datetime.strptime(int(input('d.m.Y')),'%d.%m.%Y')
result = datetime.now()-info
print(f'you survived {result} in this wordl simulation')
#OLMADII
"""


#SIFRELEME
"""
def encrypt(text, i, output=""):
    for char in text:
        output = (output,chr(ord(char) + i)
    return output

def decrypt(text, i, output2=""):
    for char in text:
        output = (output2,chr(ord(char) + i)
    return output2

i = int(input("Increment value: "))

text =input("Type your text: ")
print("Encrypted text: {}".format(encrypt(text, i)))

text = input("\nType for decrypt: ")
print("Decrypted text: {}".format(decrypt(text, i)))
#OLMADI 
"""


#uc bes bulucuinator
"""
def ucbes(a):
    if a % 3 == 0  :
         return 'uc'
    elif a % 5 == 0:
         return 'bes'
    elif a % 15 == 0:
         return 'uc bes'
    else:
         return str(a)     
    
length = int(input('son sayiyi yaz'))
for i in range(length):
    if i >0:
        print(ucbes(i))
#OLDU
"""


#rock paper scissors inator
"""
import random

print('if u can win 3 game u r the winner ')
pcchoice = ['r','s','p']
userscore = 0
pcscore = 0
while True:
    if userscore < 3 and pcscore <3:
        userchoice = input('choose : ')
        random.choice(pcchoice)
        if userchoice == 'r':
            if random.choice(pcchoice) == 'r':
                print('scorless -_-')
                print(f'user : {userscore} -- pc : {pcscore}') 
            elif random.choice(pcchoice) == 'p' :
                print('pc win :)')
                pcscore= pcscore+1
                print(f'user : {userscore} -- pc : {pcscore}')  
            elif random.choice(pcchoice) == 's':
                print('user win :(')
                userscore = userscore+1
                print(f'user : {userscore} -- pc : {pcscore}') 
        elif userchoice == 'p':
            if random.choice(pcchoice) == 'p':
                print('scorless -_-')
                print(f'user : {userscore} -- pc : {pcscore}') 
            elif random.choice(pcchoice)=='s':
                print('pc win :)')
                pcscore = pcscore+1
                print(f'user : {userscore} -- pc : {pcscore}') 
            elif random.choice(pcchoice) == 'r':
                print('user win :(')
                userscore = userscore+1
                print(f'user : {userscore} -- pc : {pcscore}') 
        elif userchoice == 's':
            if random.choice(pcchoice) == 's':
                print('scorless -_-')
                print(f'user : {userscore} -- pc : {pcscore}')  
            elif random.choice(pcchoice) == 'p':
                print('pc win :)')
                pcscore = pcscore+1
                print(f'user : {userscore} -- pc : {pcscore}') 
            elif random.choice(pcchoice) == 'r':
                print('user win :(')
                userscore = userscore+1  
                print(f'user : {userscore} -- pc : {pcscore}')    
    elif userscore == 3 or pcscore == 3:
        if userscore == 3:
            print('user win the game')
            break
        elif pcscore== 3 :
            print('pc win the game ')  
            break  
#false donme kisminda bi sikinti var %100 calisiyo diyemem hatalar var 
"""


#passwordinator
"""
import random
import string


def passwordinator(length, level, password= []):
    if  level == 1:
        chars = string.ascii_letters()
    elif level > 1:
        chars = (string.ascii_letters , string.digits)
    elif level > 2:
        chars = (string.ascii_letters , string.digits , string.punctuation)    

    for i in range(length):
        password.append(random.choice(chars))
    return ''.join(password)

passwordLength = int(input('kac cm kafidir :)')) 
passwordLevel = int(input('choose 1 or 2 or 3:  '))   
password = passwordinator(passwordLength , passwordLevel)
print(f'your password is {password}')
#OLDU 
"""


#medyuminator
"""
import random

answers = ["It is certain", "Outlook good", "You may rely on it", 
"Ask again later", "Concentrate and ask again", 
"Reply hazy, try again", "My reply is no", "My sources say no"]

question= input('ask your question ?')
print(f'your answers is : {random.choice(answers)}')
#OLDUU


#caracterfinderinator
def characterfindinator(text, characters='', output=0):
    for char in text:
        if char in characters:
            output = output+1
    return output

usercaracters =input('choose your characters: ')         
usertext= input('enter the text: ')
print(characterfindinator(usertext,usercaracters))
#OLDUU
"""


#FIBONACIINATOR
"""
def fibonaccinator(x,output=[]):
    a,b=1,1
    for i in range(x):
        a,b = b,a+b
        output.append(str(a))
    return output

length = int(input('choose the number limit: '))
print(fibonaccinator(length))
#OLDU
"""


number = int(input('enter the number'))
for i in range(int(1,number+1)):
    i=i*i
    
    

