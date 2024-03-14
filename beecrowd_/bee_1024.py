n = int(input(''))

for i in range(n):
    texto = input('')
    codificado = ''
    terceira_parte = ''
            
    for caracter in texto:
        if caracter.isalpha() == True:
            codificado += chr(ord(caracter) + 3)
        else:
            codificado += caracter
    codificado = codificado[::-1]
    for caracter in range(len(codificado)//2,len(codificado)):
            terceira_parte += chr(ord(codificado[caracter]) - 1)
    resultado = codificado[:len(texto)//2] + terceira_parte     
    print(resultado)