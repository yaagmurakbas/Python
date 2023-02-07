
#break donguyu diek durdurur
#ama continue o sirasi gelen degerin dongusunu es gecer dongu devam eder
#anlamak isityosan pc nasil okuyosa oyle okumaya calis 
myCats = 'basik ve luis'

for letter in myCats:
    if letter == 'i':
        continue         #i ye geldiginde i yi atlar ve bask ve lus cikar
    print(letter)


for letter in myCats:
    if letter=='u':
        break          #u ya geldiginde u yu 'basik ve l' cikar
    print(letter)



x = 0
while x<5:
    x=x+1              #burda 2 olmadan siraliyo diger sayilari 
    if x==2:
        continue
    print(x)



x=0
while x<=50:
    x=x+1
    if x%2==0:
        continue   #cift olanlari atliyo tek olanlari topluyo
    result=0
    result=x+result
print(result)    
    




