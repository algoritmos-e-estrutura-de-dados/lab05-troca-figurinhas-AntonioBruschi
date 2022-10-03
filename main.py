def maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_da_joao):
  trocadas = 0
  repete = 0
  for figurinhas_da_maria in figurinhas_da_maria:
    trocadas += 1
    if figurinhas_da_maria not in figurinhas_da_joao:
      x = figurinhas_da_joao
      figurinhas_da_joao = figurinhas_da_maria
      figurinhas_da_maria = x
    else:
      trocadas -= 1
    if figurinhas_da_maria in figurinhas_da_joao:
      repete += 2
  trocadas -= repete
  if trocadas < 0:
    trocadas = 0
  return trocadas


if __name__ == '__main__':
  A, B = input(
    "escreva quantas figurinhas maria e joão tem, respectivamente, separadas por um espaço: "
  ).split(' ')
  figurinhas_da_maria = input(
    "escreva as figurinhas que Maria tem, separadas por espaço: ").split(' ')
  figurinhas_da_joao = input(
    "escreva as figurinhas que João tem, separadas por espaço: ").split(' ')
  print("FIGURINHAS TROCADAS: ")
  print(maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_da_joao))
