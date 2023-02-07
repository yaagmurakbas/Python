

def sayBabanen():
    print('babanen')
                             #burda fonctions olusturdum ve onu cagirdim
sayBabanen()  




def sayHello(name = 'uselessUser'):
    return 'hello ' + name
                        #burdaki olay su biz deften fonksiyonda name varsa name al yoksa uselessuser kullan dedik 
                        #ama sonra helllo name ile birlsertirdik sonra return ile msg kismina yani fonksiyonun calisetigi kisma geri y0ollafim
                        #burdan sonra akis normal devam etti 
msg = sayHello('babanen')    
print(msg)



def total(number1, number2):
    return number1+number2

result=total(15,68)
print(result)


def yasHesapla(dogumyili):
    yas = 2021- dogumyili



def  emekliligekacyilkaldi(dogumyili, isim):
    yas = yasHesapla(dogumyili)
    emeklilik =  65 - yas
    if emeklilik > 0:
        print(f'{isim} kisisi emekliliginize {emeklilik} yil kaldi')
    else:
        print('zaten emklisiniz amk ')    

a = int(input('dogum yilini gir ulan'))
b = input('adini soyle amk')

emekliliky = emekliligekacyilkaldi(a , b)



def changeName(n):
    n = 'ada'

name = 'yigit'
changeName(name)                #7.3 TEKRAR IZLE ANLAMADIMMM SAKIN KAFAYLa izle 
print(name)

name = changeName('ece')