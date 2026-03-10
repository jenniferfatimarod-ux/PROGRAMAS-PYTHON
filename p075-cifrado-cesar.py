#p075-cifrado-cesar.py
#Cifra un mensaje usando el cig¿frado de Cesar

print("\033[2J\033[H")
print('Cifra un mensaje usando el cifrado de Cesar')

mensaje_original = input('Mensaje a encriptar: ')
desplazamiento = int(input('Desplazamiento: '))
mensaje_cifrado = ''

for caracter in mensaje_original:
    if caracter.isalpha():
        codigo_ascii = ord(caracter)
        base = ord('a') if caracter.islower() else ord('A')
        codigo_nuevo = base + (codigo_ascii - base + desplazamiento) % 26
        mensaje_cifrado += chr(codigo_nuevo) 
    else:
        mensaje_cifrado = mensaje_cifrado + caracter

print(f'Mensaje original: {mensaje_original}')
print(f'Mensaje cifrado: {mensaje_cifrado}')