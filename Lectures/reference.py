#bunlar value types=> str int float 
#BURDA Y YI DEGISTIRDIKTEN SONRA X ETKILENMEZ 
x= 5
y = 25
x=y
y = 30
print(x,y)

#bnlar reference types => list
#burda b yi degistirdim a da degisti cunku burda ana konu liste a veya be degil
a= ['123','456']
b=['123','456']
a=b
b[1]='789'
print(a,b) 
#simdi burdaki ozellik su value typlelar degiskenin kendisini depolaar ama reference type ta listenin adresi hatirlanir
#yani 500 degisken varssa bunlaer 1 adreste olur. anlamadiysan 3.20 videosundaki semaya bak en sonlarda '


#bunu buraya yazmam daha mantikli eldi bilmiyorum
#simdi
x=y= [1,2,3] #burda x ve y nin adressleri ayni ama z nin farkli
z = [1,2,3] 
print(x==z)  #simdi bu dogru demek cunku bu icindeki degiskenleri karsilastiri
ama
print(x is z)  #dersem bu degisir cunku bu adreslerini karsilastirir

#simdi burda baska bir onemli nokta var diyelimki listeleri baska adresslere kaydettik
#cunku icindekiler farkli peki sonradan icindeki degerleri esitlersek aynni aresse donermi 
# cevap hayirr

x=[1,2,3]   #icindekiler farkli o yuzden farkli adresslere kayit edilir 
y=[1,2]
#simdi degerleri esitleyelim 
del x [2]
print(x==y)  #bundan dogru ciktisi alirim ama 
print(x is y)  #bundan ynlis alirim cunku bu adresslere bakar bundan dolayi false verir

# ayni sekilde is not ta kullanilabilir soruyu tersten sormus olursun 



# simdi baska bir konu sorguluycaz liste icinde o deger varmi diye bakicaz
meyveler = ['muz','limon','portokal']
print('limon' in meyveler)
#oldugundan dolayi bana true verir olmayan bbisey yazarsama false verir 

