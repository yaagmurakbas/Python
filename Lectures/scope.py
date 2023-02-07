'''
#fonksiyon icinde degistirdiginb  deger orda kalir ana degiskeni degidtirmrz

babanenin = 'amk'  #burdaki global name
def function (x):
    babanenin = 'elleri dert gormesin' #burda yaptigim degisim benim degerimi degistirmedi
    print(babanenin)    #burdaki atama local name olur 
function(babanenin)
print(babanenin) #burda degerimi yazdirdigimda hala  amk oluyo


name = 'babanen'
def function(newname):
    global name   #global namein fonksiyon icinde degistirilmesi iccin global komutunu kullandim
    name = newname   #global kulllandigimdan ilk deferde degistirdiggim name degeinin usutne islem yapmaya basladi yani global degisti           
    print(name)                 
function('amk')
print(name)

#PEKI 2 FONKSION IIC ICEYKEN GLOBAL NAME NASIL OLUR
'''
name = 'global'
def ehehe():
    name = 'babanen'
    def uwu():
        print(name)   #burda printledigin name ehehe deki name degeri olur     
    uwu()             #cunku orda bi ustteki fonksiyon onun icin global  odur 
ehehe()               #eger ben ehehe de babaneni atamasaydim en ustte cikicakti yani eger babanen olmasaydi global onun icin ilk atadigim gloal olur
print(name) #burdaki printte global bizim ilk globaldir

