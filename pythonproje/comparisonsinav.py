number = int(input('bi sayi gir ulan'))
print(f'girdiginiz sayi 100den kucuk 0dan buyuk {(number>0) and (number<100)}')


number = int(input('bi sayi gir ulann'))
result = (number>0) and (number%2 == 0)
print(f'sayiniz hem cift hem odan buyuk : {result}')


username = 'babanen'
password = '12345'
 
username1 = input('username gir ulan')
password1 = input('password gir ulan')

result = (username==username1) and (password==password1)
print(f'girisin dogru kocum hg:{result}')


number1 = int(input('1. sayiyi gir ulan'))
number2 = int(input('2. sayiyi gir ulan'))
number3 = int(input('3. sayiyi gir ulan'))
print(f'number1 en buyuk: {number1>number2 and number1>number3}')
print(f'number2 en buyuk: {number2>number1 and number2>number3}')
print(f'number3 en buyuk: {number3>number1 and number3>number2}')


vize1 = int(input('1. viizeni gir ulan'))
vize2 = int(input('2. vizeni gir ullan'))
final = int(input('finalini gir ulan notunu hesapliycam'))

result = ((vize1+vize2)/100*60/2)+(final*40/100)
print(f'sinavdan gectiniz: {(final>70) or ((result>50) and (final>50))}')


height = input('boyunu gir ulan')
weight = input('kilonu cikra')
                                 #burda tanimlarkende integer diyebilirsin asagida islem yaparkende int diyebilirsin
bodyIndex = (int(weight)/(int(height) **2)*10000)
print(f'kilo indeksiniz: {bodyIndex}')


#INPUTTAN GELEN DEGERLER STRING OLUURRR ONU INT CEVIRMEN LAZIMMMMMMMMM