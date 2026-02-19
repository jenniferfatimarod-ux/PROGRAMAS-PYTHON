#p048-multiplos-continue.py
#Imprime los múltiplos de 0 a 200

print("\033[2J\033[H")
print("--Imprime los múltiplos de 10--\n")

#z=int(input('Ingrese el número mayor: '))
n=int(input('Ingrese el multiplo: '))

c=0
while c<200:
    c=c+1
    if c % n !=0:
        continue
    print(f'{c}', end=' ')
   

print(f'\nCiclo terminado: {c}')

