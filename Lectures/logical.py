#and kullanimi 2 tarafindaki sartlarin 2 sindende true citisi gelirse true veririr
x = 9
result = (x<10) and (x>5)
print(result)


#or kullanimi 2 taraftan 1 tanesindne true donmesi yeterli sonuc true cikar diyelim 2 side true sonuc gene true olur
x= -4
result = (x>0) or (x%2==0)  #burda pozitif veya cift sayi olmasi yeterli 


# not kullanimi sonucun tam tersini verir
x=6
result = not(x<0)
#normelde bu false ama not koydum basina bu yuzden ben true aldim



#MISAL
#hem cift hem  istedigim aralikta deger bulmak istiyorum ozaman 
print(int(input('sayi gir')))
result = ((x>5) and (x<10)) and (x % 2 == 0)
print(f'sayiniz hem cift hemde 5 le 10 arasinda:{result}')