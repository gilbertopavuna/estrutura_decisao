turno = input('Em que turno você trabalha (M - matutino, V - vespertino, N -noturno): ').upper()
if turno == 'M':
    print('Bom dia!')
elif turno == 'V':
    print('Boa Tarde!')
elif turno == 'N':
    print('Boa Noite!')
else:
    print('Valor inválido!')
