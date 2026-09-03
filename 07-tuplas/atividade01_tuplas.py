# Autor: Daniel Pina
#Projeto: Tuplas

meses = ('jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez')
print(meses)
print(*meses)
print(*meses, sep=' | ')

semana = ('seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom')
print(*semana, sep=' | ')