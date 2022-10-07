def recebe():
  x = int(input("Escreva o valor em cm:"))
  return x


def converter(a):
  c = a/2.54
  arquivo = open('tarefa.txt', 'w')
  arquivo.write('o valor {} em centimetros equivale a {:.2f} polegadas'.format(a,c))
  arquivo.close()