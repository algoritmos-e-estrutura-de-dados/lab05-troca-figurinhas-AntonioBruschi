
def maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_da_joao):
    troca = 0
    repete = 0
    for figurinhas_da_maria in figurinhas_da_maria:
        troca += 1      
        if figurinhas_da_maria not in figurinhas_da_joao:
            x = figurinhas_da_joao
            figurinhas_da_joao = figurinhas_da_maria
            figurinhas_da_maria = x
        else:
            troca -= 1 
        if figurinhas_da_maria in figurinhas_da_joao:
            repete += 2
    troca -= repete 
    if troca < 0:
        troca = 0                   
    return troca



if __name__ == '__main__':
    A, B = input("escreva quantas figurinhas maria e joão tem, respectivamente, separadas por um espaço: ").split(' ')
    figurinhas_da_maria = input("escreva as figurinhas que Maria tem, separadas por espaço: ").split(' ')
    figurinhas_da_joao = input("escreva as figurinhas que João tem, separadas por espaço: ").split(' ')
    print("FIGURINHAS TROCADAS: ")
    print(maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_da_joao))
    
