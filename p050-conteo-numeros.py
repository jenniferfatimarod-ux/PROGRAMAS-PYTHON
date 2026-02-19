#p050-conteo-numeros.py
#Lee y cuenta números hasta 999

print("\033[2J\033[H")
print("Lee y cuenta números hasta 999\n")

s=c=cp=cn=cz=0
while True:
    num = int(input('Número: '))
    if num==999: break
    c+=1
    s+=num
    if num>0: cp+=1
    elif num<0: cn+=1
    else: cz+=1

print('\nReporte final')
print(f'Fueron {c} numeros')
print(f'suma : {s}')
print(f'pos : {cp}')
print(f'neg : {cn}')
print(f'ceros : {cz}')