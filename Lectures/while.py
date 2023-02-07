x = 1
while x<=20:
    print(x)         #1 er 1er arttirmak icin
    x = x +1
print('bitti ulan')    


x=1
while x<=50:
    if x%2==0:         
        print(f'sayi cifttir {x}')
    elif x%2==1:                      #50ye kadar olan cift ve tek sayilarin ayrimi
        print(f'sayi tektir {x}')
    x = x + 1   
print('bitti amk')  


name = ''  #bosluk false demek
while not name.strip():                        #simdi burda bana geldi cikti enter yapip while a devam edersem while false gordugunden donmeye devam edicek isim girenen kadar 
    name = input('isminizi girin')     #isim girdikten sonra while dongusundencikar cunku artik true donmez bu uzden artik printe gecer
print(f'hosgeldin {name}')             # eger bosluk birakip enter derse enter da karakter olur ve true doner isim yazmak yerine bosluk ayni sey olur
#boslugu onlemek icin yapmam gereken strip kullanmak  bu bastaki ve sondaki bosluklarisiliceginden bizim bosluklarimiz olmaz
#namein basina while dongusunu yazaerknen yaptim ordan bak 
