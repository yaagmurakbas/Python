#LOOP

#1th project
"""
tuple = [[1,2,3],[4,5,6],[7,8],[9]]
sum  = 0

for x in range(len(tuple)):     #adam burda direk tuple dedi  len range ksimi yerine
    for y in range(len(tuple[x])):    #burdada direk x dedi len range kullanmak yerine 
        sum+=tuple[x][y]
        print(f"sum of numbers: {sum}")

dict = {"bir": 1, "iki":2, "uc":3, "dort":4}
for (x,y) in dict.items():
    print(f"key: {x}   value: {y}")
"""


#2th project
"""
chance = 8
name = "yaagmur"
password = 14072002

while True:
    userName =  input("ener user name: ")
    userPassword = int(input("enter user password:"))
    if chance>0:
        if((userName!=name)  and (userPassword==password)):
            chance-=1
            print("only user name is not correct")
        elif (userPassword!=password and (userName==name)):
            chance-=1
            print("only password is not correct")
        elif((userName!=name)  and (userPassword!=password)):
            chance-=1
            print("user name and password wrong")
        else:
            print(f"welcome {name}")
            break        
        print(f"you have {chance} chance")

    else:
        print("user account is bloced")
        break
"""


#3th project 
"""
print('''*************************************************************
Welcome to ATM

1 leftover query 
2 deposit money
3 withdraw money 
for leaving the applicattion press "q"

*************************************************************''')
money = 1000
while True:
    operation = input("enter the operation sing: ")
    if operation != "q":
        if operation == "1":
            print(f"bank account: {money} ")
        elif operation == "2":
            value = int(input("how much money  do you want  to deosit? :  "))
            money+=value
            print("operation successful")
            print(f"bank account: {money} ")
        elif operation == "3":
            value = int(input("how much money  do you want  to withdraw?"))
            if (value<=money):
                money-=value
                print("operation successful")
                print(f"bank account: {money} ")
            else:
                print("insufficient money")
        else:
            print("invaild operation")
    else:
        print("thx for choosing us take care asko")
        break
    print("do you have another operation orwant  to leave the applcation")
"""


#4th project
"""
userNum = int(input("enter the number: "))
result = 1
if userNum == 0:
    result = 1
else:
    for i in range(1,userNum+1):
        result*=i
print(f"factorial of {userNum} : {result}")
"""


#5th project 
"""
userNum = int(input("enter the number: "))
x = 1
y = 1
fibonacci = [x,y]  
if userNum>1:
    for i in range(1,userNum-1):
        print(f"x : {x}     y : {y}")
        a=y
        y+=x
        x=a
        fibonacci.append(y)
print(fibonacci)
"""


#6th project
"""
userNum = int(input("enter the number: "))
result = 0
for i in range(1,userNum):
    if userNum % i == 0:
        result+=i
if result == userNum:
    print(f"{userNum} is a perfect number")
else:
    print(f"{userNum} is not a perfect number")        
"""


#7th project
"""
#burda oncelikle basamaklari nasil saptiycagimi test etmem lazim
'''
num = int(input("enter the number: "))

#eger sayiya 123 dersek
print(num%10)   #birler
print(num%100)  #onlar ve birler
print(num%1000) #sayinin kendisini verdi 

print(num//10)  #yuzler ve onlar 
'''
userNum = int(input("enter the number: "))

if (userNum//100) == 0:
    x = (userNum%10) #birler basamagi
    y = (userNum//10) #onlar basagi
    if(userNum == ((x**2)+(y**2))):
        print(f"{userNum} is a armstrong number")
    else:
        print(f"{userNum} is not a armstrog number")
elif ((userNum//1000) == 0):
    x = (userNum%10) #birler basamagi
    y = ((userNum//10)%10)  #veya   (userNum%100)//10)  onlar basamagi
    z = (userNum//100) #yuzler basamagi
    if(userNum == ((x**3)+(y**3)+(z**3))):
        print(f"{userNum} is a armstrong number")
    else:
        print(f"{userNum} is not a armstrog number")
elif (userNum//10000) == 0:
    x = (userNum%10)
    y = ((userNum%100)//10)   
    z = ((userNum//100)%10)
    k = (userNum//1000)
    if(userNum == ((x**4)+(y**4)+(z**4)+(k**4))):
        print(f"{userNum} is a armstrong number")
    else:
        print(f"{userNum} is not a armstrog number")
#BURDAJI EN BUYUK HATAM BASAMAKLARI BOYLE AYIRMAK YERINE LEN KULLANMAMAK OLDU
#BIRAZ ZIRVALADIM
"""


#8th project
"""
for x in range(1,11):
    print("*****************")
    for y in range(1,11):
        print(f"{x} * {y} = {x*y}")
        y+=1
    x+=1    
"""


#9th project
"""
result = 1
while True:
    userNum = input("enter the number(for leaving press 'q'):   ")
    if userNum != "q":
        result *=int(userNum)
        print(f"result: {result}")
    elif userNum == "q":
        break 
    else:
        print("pls enter only number or q letter")
"""


#10th prioject
"""
num = []
for x in range(1,101):
    if (x%3==0):
        num.append(x)
    else:
        continue
print(num)    
"""


#11th project
"""
x = [i for i in range(1,101) if (i%2==0)]
print(x)
"""


#12th project
"""
numbers = [1,3,5,7,9,12,21]
for i in numbers:
    if i%3==0:
        print(i)   #3un kati sayilar
        print(i**3)     #3un kati sayilarin karesi  
toplam=0

for i in numbers:
    toplam=toplam+i    #sayi toplamlari
print(toplam)    
        
cities = ['kocaeli','istanbul','ankara','izmir','rize'] 
for city in cities:
    if len(city)>=5:
        print(city)
"""


#13th project
"""
products = [
    {'name':'samsung1','price':'3000'},
    {'name':'samsung2','price':'4000'},
    {'name':'samsung3','price':'5000'},
    {'name':'samsung4','price':'6000'}
]

toplam = 0
for i in products:
    toplam = toplam + int(i['price'])  
print(toplam)

for i in products:
    if int(i['price'])<=5000:
        print(i['name'])
"""

#14th project
"""
import random
number = random.randint(1,100)

hak = (1,2,3,4,5)
for items in hak:
    usernumber = int(input('sayi gir ullan '))
    if items<5:
       if number == usernumber:
           if items==5:
               puan=20
           elif items==1:
               puan=100  
           elif items==2:
               puan=80
           elif items==3:
               puan=60
           elif items==4:
               puan=40
           print(f'helal olsun koc bildin puanin {puan}')
       elif usernumber< number:
           print(f'bu biraz az old {items} . hakkinizi kullandiniz kalan hak sayiniz {5-items}')  
       elif usernumber> number:  
           print(f'bu biraz fazla oldu {items} . hakkinizi kullandiniz kalan hak sayiniz {5-items}')
           
    else:
        print(f'hakkiniz kalmadi slk ve 0 puan aldin sayi: {number} ')
"""


#15th project
"""
userNumber = int(input('sayi gir ulan'))
 
if userNumber>1:
    for a in range(2,1000):
        if userNumber % a == 0:
            print(f'{userNumber} asal degildir  ')
            break
        else:
            print(f'{userNumber}  asaldir')
            break
else:
    print('1 asal degildir' )            
"""