'''
#ASALINATOR AMA 2 SAYI ARASINDA OLANLARI BULUR 
def asalinator(num1,num2):
    numbers = []
    for i in range(num1,(num2+1)):
        for a in range(2,i):
            if  i % a ==0:
                print(f'{i} sayiiz asal degildir ')
                break
            else:
                print(f'{i} sayiniz asaldir')
                numbers.append(i)
                break
    print(numbers)        

usernumber1 = int(input('asalinatore sayi cikra ulan '))              
usernumber2 = int(input('asalinatore sayi cikra ulan '))    
asalinator(usernumber1,usernumber2)
#OLDU AYOL



#TAM BOEN BULMA
def tamboleninator(number):
    numbers=[]
    for i in range(1,number+1):
        if number%i==0:
            print(f'{i} {number}in tam bolenidir')
            numbers.append(i)
        else:
            continue   

usernumber = int(input('tam bolenleri bulunucak asayiyi cikra '))
tamboleninator(usernumber)
#OLDUUU



#ISTELINEN KEZ YAZDIRMA
def yazdirinator(number,word):
    for i in range(1,number+1):
        print(word)

userw = input('kelime cikra ')
usern = int(input('kac kez yazilsin '))
yazdirinator(usern,userw)
#OLDUUUU



#LSITEYE EKLEME
def listinator(*values):
    list = []
    for i in values:
        list.append(i)
    return list    

list = input('listeye yazilicak seyleri ver araya virgul koysrak ')
print(listinator(list))    
#OLDU
'''
