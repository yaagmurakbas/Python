
#range( ) operatoru sayilari siralar

for items in range(10):
    print(items)               #BURDA 10 A KADAR YAZIDRIR

for items in range(2,10):
    print(items)               #BURDA 2 DEN 10A KADAR YAZDIRIR

#MISAL 1. YOL
index = 0
greeting = 'hello darkness my old friend'
for letter in greeting:
    print(f'{index} nolu harf = {letter}')
    index=index+1

#MISAL 2. YOL   
index = 0
greeting = 'hello darkness my old friend'
for letter in greeting:
    print(f'{index} nolu harf = {greeting[index]}')
    index=index+1

#MISAL 3. YOL 
greeting = 'hello darkness my old friend'
for index,letter in enumerate(greeting):
    print(f'{index} nolu harf = {letter}')


#zip kullanimi 
list1 = [1,2,3,4,5] 
list2 = ['a','b','c','d','e']
list3 = [100,200,300,400,500]
print(zip(list1,list2,list3))
#her elemani yari ayri yazmak istersen 
for item in zip(list1,list2,list3):
    print(item)



    


   