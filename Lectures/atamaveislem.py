x = 5
x += 6 # bu x = x+6 demek
x -= 6 # bu x = x-6 demek
x *= 6 # bu x = x*6 demek 
x /= 6 # bu x = x/6 demek bu float olur 
x //= 6 # bu x = x/6 demek ama float olarak almaz tam kismini alir 
x **= 6 # bu demkeekki x ustu 6 demek 

values = 1, 2, 3
print(values)
x, y, z = values
print (values)
# ya direk 3 elemana 3 atama yapiyo sayisi onemli cunku 3 degere 3 atama olmali  fazla veya az olammaz 
#eger fazla values var ozaman atama yaprken son elemana list seklinde atar 
#mishal
babanen = 1,2,3,4,5,6
x,y,*z= babanen
#bunu yaparsan output olarak 1,2,[3,4,5,6] alirsin 


x,y,z=(6,4,3)
numbers= (1, 2, 5, 4, 7, 9)


#2 sayi iste sonra onlari carp x y z toplamindan cikar 
a = int(input('1. sayiYI cikra'))
b = int(input('2. sayiyi cikra'))
result = (a*b)-(x+y+z)
print(result)


#xi y ye bol ama kalansiz
result = x//y
print(result)

#burda xyz toplaminin mod 3unu alicam 
toplam = (x+y+z)
print(toplam%3)


#kuvvet alma 2 yildizla yazpilir
result = y**z
#bu y nin z kuveti demek 


#xyz yi numbersa atamak istersek 
x, *y, z = numbers 
#y ninn onunda yildiz var cunku x ilk sayiyi z en son sayiyi y ye 3 sayi kalir bundan dolayi
#yye yildiz koyarak ortafdaki elemanlari aliriz 
print(y)