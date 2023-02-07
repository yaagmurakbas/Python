import os


print(os.getcwd())#bu bana hangi klasorde bulundugumu soyler

os.chdir('buraya yazicagim uzantiya dosyayi tasir')#string olarak dosya adressi vermezsen o zaman hata verir
print(os.getcwd())  #ustte yeni klasore tasimistik dosya konumuna yazdirirsan yeni adress verir

print(os.listdir)  #cikti gelen liste o klasordeki dosyalardir
    