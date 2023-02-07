#FUNCTIONS

#1th project
"""
def factorial(num):
    result = 1
    if num > 1:
        for i in  range(1,num+1):
            result*=i
    return result

userNum = int(input("enter the number: "))
print(f"{userNum}! = {factorial(userNum)}")
"""


#2th project
"""
#first way
def primeFinderinator1(num):
    x = 0
    for i in range(2,num):
        if num%i==0:
            x+=1
    if x == 0:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is NOT a prime number")
#second way
def primeFinderinator2(num):
    x = 0
    number = 2
    while number<num:    #direk true diyip sonra breakle cikartabilirim
        if(num%number==0):
            x+=1
        if(x!=0):
            break
        number+=1 
    if x == 0:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is NOT a prime number")   

userNum = int(input("enter the number:  "))
primeFinderinator1(userNum)
primeFinderinator2(userNum)
"""


#3th project
"""
def divisorinator(num):
    x = [1]
    for i in range(2,num+1):
        if num%i==0:
            x.append(i)
    return x        

while True:
    userNum = input("enter the number(leaving the appplication press 'q'):  ")
    if userNum =="q":
        print("u'r leaving the aplication....")
        break
    else:
        print(f"{divisorinator(int(userNum))} is divisor of {userNum}")
"""


#4th project
"""
def perfectNumberFinderinator(num):
    sum = 0
    for i in range(1,num):
        if (num%i==0):
            sum+=i
    if (sum == num):
        print(f"{num} is a perfect number")
    
num = 1
while num<1000:
    perfectNumberFinderinator(num)
    num+=1
"""


#5th project
"""
def ebobCalculatorinator(num1, num2):
    x = []
    if (num1>num2):
        bigNum = num1
        litNum = num2
    elif (num2>num1):
        bigNum = num2
        litNum = num1
    else:
        return num1
    for i in range(1,litNum+1):
        if((litNum%i==0) and (bigNum%i==0)):
            x.append(i)
    x.sort()
    return(x[-1])  

userNum1 = int(input("enter the first number: "))
userNum2 = int(input("enter the second number: "))
print(f"the EBOB of {userNum1} and {userNum2}: {ebobCalculatorinator(userNum1, userNum2)}")
"""


#6th project
"""
def ekokCalculatorinator(num1, num2):
    x = []
    if (num1>num2):
        bigNum = num1
        litNum = num2
    elif (num2>num1):
        bigNum = num2
        litNum = num1
    else:
        return num1
    if i in range(1, bigNum):

    
    

userNum1 = int(input("enter the first number: "))
userNum2 = int(input("enter the second number: "))
print(f"the EKOK of {userNum1} and {userNum2}: {ekokCalculatorinator(userNum1, userNum2)}")

"""


#7th project
"""
def spellinginator(num):
    birler =  ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
    onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]

    num1 = num%10
    num2 = num/10


    print("the spelling of the number: "+ onlar[num2] +" "+ birler[num1])
    
while True:
    userNum = input("enter the number: ")
    if (userNum == "q"):
        print("u'r leaving the application...")
        break
    else:
        spellinginator(int(userNum))
"""


#8th project
""" 
def pisagorFinder(x):
    pisagorList = list()
    for i in range(1,x+1):
        for j in range(1,x+1):
            k =(i**2+j**2)**0.5
            if(k == int(k)):
                pisagorList.append((i,j,int(k)))    
    return pisagorList

userNum = int(input("enter the upper limit: "))
for i in pisagorFinder(userNum):
    print(i)
    """


#9th project
""" 
def loop(word, number):
    print(word * number)

sayi1 = int(input('1. sayi yi gir '))
sayi2 = int(input('2. sayiyi gir '))

def  asalBul(sayi1, sayi2):
    for sayilar in range(sayi1,sayi2+1):
        if (sayilar > 1):
            for i in range(2,sayilar):
                if (sayilar%i==0):
                    print(i)
"""