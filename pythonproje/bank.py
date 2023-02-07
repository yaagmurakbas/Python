xaccount = { 'name':'yagmur',
    'accountno':'123456',
    'limit':5000,
    'extralimit':4000
    }

yaccount = {'name':'babanen',
    'accountno':'112233',
    'limit':8000,
    'extralimit':2000
}


def bank(account, number):
    print(f'merhaba {account["name"]}')
    if number <= int(account['limit']):
        account['limit'] = account['limit']- number
        print(f'cekim izleminiz basarili kalan bakiyeniz: {account["limit"] }')
    elif number > int(account['limit']):
        doublecheck = input('ek hesap kullanilsin mi (YES or NO): ')
        if doublecheck == 'yes' or 'YES':
            newlimit = account['extralimit']-(number-account['limit'])
            print(f'cekim izleminiz basarili extra limit kullanildi!!!! kalan extra bakiyeniz: {newlimit} ')
        else:
            print('bakiyeniz yetersiz')
    elif number > int(account['limit'])+ int(account['extralimit']):
        print('bakiyeniz yetersiz') 


usercheck = int(input('hesap nonu cikra: '))

if usercheck ==  int(xaccount['accountno']):
    usermoney = int(input(f'ne kadar para lazim it olu it {xaccount["name"]}: '))
    bank(xaccount, usermoney)
elif usercheck == int(yaccount['accountno']):
    usermoney = int(input(f'ne kadar para lazim it olu it {yaccount["name"]}: '))
    bank(yaccount, usermoney)
else:
    print('your information is wrong tyr again')


#burda hersey okey ama adam diyoku sozluk olarak degilde normal atama yapsaydik bu
#ana degeri degistirmezdi  scope.py de olan mevzu iste ama bu dick oldugundan oyle olmuyor