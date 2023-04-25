aux1,aux2,aux3 = int(0),int(1),int(0)
print ( 'Pertence a fibonacci?')
numeroProcurado = int(input('Digite um inteiro: '))
while numeroProcurado > aux3:
    aux3 = aux1 + aux2
    aux1 = aux2
    aux2 = aux3
if numeroProcurado == 0 or numeroProcurado == 1:
    print ('O número faz parte da sequência.')
elif numeroProcurado == aux3:
    print ('O número faz parte da sequência.')
else:
    print ('O número digitado não faz parte da sequência.')
