
def babaneninator(number):
    for i in range(number):
        file.write('babanenin amk\n')

file = open('deneme.txt',mode='w')
usernumber= int(input('sayiyi gir: '))
babaneninator(usernumber)
file.close()

file = open('deneme.txt', mode = 'r')
print(file.read()) #eger bir kisim karakter yazmak istersen read(9) bu ilk 9 karakteri yazar
file.close()

with open('deneme2.txt',mode = 'r+') as f:
    f.write('babanen')
    print(f.read())
    f.close()

#SATIR SATIR BOLME YOLLARI

a = a.readlines()  #yol 1 
 
for line in a:     #yol2 burda arada 2 bosluk olur ondan end kullandim 
     print(line,end = '')

#SEEK VE TELL KULLANIMI
a.seek(0)   #bunu yaprsan senin ilmecini en basa yollar
a.tell()    #bunu yaparsan imlecinin oldugu noktanin index numaasini soyler


#belirli bir kismi okurken mesela a.read(10) dedin ilk 10u yazdi sonra gene ayni
#seyi yaparsan imlecin kaldigi yerden 10 tane okur yani ilk 20 yi okumus olursun


#append kullaniminda eger write ile eklersen eskisini siler yeniden olusturur 
#ama append kullanirsan eskinin onune yeni yaziy yazar
#MISAL
with (open('deneme3.txt', mode = 'w')) as f:
    f.write('a')  #bunu sonra b yapsam mesela o zaman a dosyadan silinir 

with (open('deneme3.txt', mode = 'a')) as f:
    f.append('a')  #bunuu sonradan b yaparsam dosyada a b olarak yazilir a silinmez

#dosyayi kopyalama
#MISAL
with open('a.txt') as kopyalanicak:
    with open('b.txt', mode = 'w') as yazilicak:
        for line in kopyalanicak:           #for yerine readlines() kullanabilirsin
            yazilicak.write(line,end = '')
    print()
