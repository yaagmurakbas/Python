
def squerinator (num):
    return num**2

usernum =[1,2,3,4,5]
result = map(squerinator,usernum)    #map senin anlayamaciagin bi cikti verir ondan dolayi 
print(list(result))                  #list yapman veya
for i in result:                     #for ile yazdirman lazim      
    print(i) 


#lambda kullanimi 
usernumbers = [1,2,3,4,5,6,70]   
print(list(map(lambda num: num**2 ,usernumbers)))  #fonctiona isim vermeden result olmadan yaptim

#mesela lambda yaisim vermek istedim onuda boyle yaparim
usernumber = [1,2,3,4,5]
function = lambda num : num**2
print(list(map(function,usernumber)))
#hatta isim verdikten sonra ileridede kullanabilirsin
print(function(3))  #burda 3un karesini alir direk


#filter kullanimi 
def checkinator (num):
    return num%2==0
number = [1,2,3,4,5,6]
print(list(filter(checkinator,number)))

#veya lambda kullanarak yap
number = [1,2,3,4,5,6]
print(list(filter(lambda num: num %2==0, number)))