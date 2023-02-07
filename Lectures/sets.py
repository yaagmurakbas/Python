
fruits = {'orange', 'apple','banana'}
print(fruits[1])
#setlerde numara yoktur bundan dolayi index numarasini bilemezsin arattiginda bulamazsin

#elemanlarina for dongusu kullanarak ulasabilirsin
for x in fruits:
    print(x)
#boyle yaparsan elemanlari bastirirsin 
# liste elmanlarini siralayamazsin

#set listlereine eklem 2 sekilde yapilir 1.si add methoduyla 
fruits.add('cherry')
#2. yol update bizimkinin icine liste gpnder gonderebiliriz
fruits.update(['mango','grape'])
print(fruits)

#zaten var olan bir elemani eklemeye calisirsak o zaman eklenmez!!! 
#oldugu gibi gozukur 2. defa tekrarlanmaz 1 elemandan 1 kere olur 
myList = [1,2,3,4,14,12,32,2]
print(set(myList))
#burda set yaparsak bizim listemiz icindekii twkrarlanan ayni elemanlar
#1er kez olur 


fruits.remove('mango')  #silem methodu
fruits.discard('apple') #bunlammda dilebilirim
fruits.clear() #tum elemanlari siler
fruits.pop() #bunu yaparsan pop en sondakini siler 
#ama biz setllerde hangisinin en son oldugunu bilmiyoruz 
#bu yuzden hrehangi birini siler