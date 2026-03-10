#p079-factorial-numeros.py
#Calucula el factoria de n numeros

print("\033[2J\033[H")
print("Calcula el factorial hasta n numeros")

try:
    n = int(input('Hasta que numero? '))

    for i in range(1,n+1):
        f = 1
        m = ''
        for j in range(1,i+1):
            m = m + str(j) 
            m += '*' if i!=j else ''
            f = f * j

        print(f'{j}! = {m} = {f:,}')
except ValueError:
    print('\nDebe ser un número!')