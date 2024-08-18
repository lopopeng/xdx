n= "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

def password(lena):
    p=''
    for i in range(lena):
        p+=random.choice(n)
    return p


import random
while True:
    o=input('Введите названия приложения')
    s={}
    p=''
    lena=int(input('Введите длину пароля'))
    for i in range(lena):
        p+=random.choice(n)
    s[o]=password(lena)
    print(p)