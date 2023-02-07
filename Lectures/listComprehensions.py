#burda diyelimki range ile alidgin sayilari list icine atmak istedin 2 yool var 
#1. YOL
numbers = []
for x in range(20):
    numbers.append(x)
print(numbers)    

#2. YOL
numbers = [x for x in range(20)]
print(numbers)

#MISAL
babanen = []
for x in range(5):
    babanen.append(x**2)
print(babanen)


babanen = [x**2 for x in range(5)]
print(babanen)



numbers =[x**2 for x in range(10) if x%3==0]
print(numbers)



myString= 'BABANEN'
myList = [letter for letter in myString]
print(myList)



years = [2002,1979,1970]
years=[2021-x for x in years]
print(years)


result=[x if x%2==0 else 'tek' for x in range(10)]
print(result)


numbers = []
for z in range(3):
    for x in range (3):     # burda 2 doongu bir arada 
        numbers.append((z,x))
print(numbers)

numbers = [(x,y) for x in range(3) for y in range(3)] 
print(numbers)