from random import randint

mapa = [["A","A","A","A","A", "" ,"" ,"A","A","A","A","A"],
        ["A","","","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"A"],
        ["A","" ,"" ,"" ,"A","" ,"" ,"" ,"" ,"" ,"" ,"A"],
        ["A","E","E","E","A","E","E","E","G","G","G","A"],
        ["A","" ,"" ,"" ,"A","G","G","G","G","G","G","A"],
        ["A","E","E","E","A","G","G","G","G","G","G","A"],
        ["A","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"A"],
        ["A","" ,"" ,"" ,"" ,"" ,"" ,"" ,"G","G","G","A"],
        ["A","A","E","E","E","A","A","A","G","G","G","A"],
        ["A","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"A"],
        ["A","E","" ,"E","E","" ,"E","E","E","E","E","A"],
        ["A","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"A"],
        ["A","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" , "A"],
        ["A","A","A","A","A","A","G","G","G","E","E","A"],
        ["A","" ,"" ,"" ,"" ,"" ,"G","G","G","" ,"" ,"A"],
        ["A","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"A"],
        ["A","E","E","" ,"" ,"E","E","E","E","E","E","A"],
        ["A","" ,"G","G","G","G","" ,"" ,"G","G","G","A"],
        ["A","G","G","G","" ,"" ,"" ,"G","G","" ,"" ,"A"],
        ["A","A","A","A","A","A","G","A","A","A","A","A"]]

aux = 0

posicaoLinha = 19
posicaoColuna = 6


def aleatorio(valor):
    return randint(0,valor)

status = {

    "hp" :  aleatorio(100),
    "atk" : aleatorio(100),
    "Def" : aleatorio(100),
    "Sp.Atk" : aleatorio(100),
    "Sp.Def": aleatorio(100),
    "Speed": aleatorio(100)

}

pokemon = {

    "0" : "Ratata",
    "1" : "Pidgey",
    "2" : "Weedle", 
    "3" : "Caterpie",
    "4" : "Paras",
    "5" : "Charmander",
    "6" : "Bulbasaur",
    "7" : "Squirtle",
    "8" : "Pikachu",
    "9" :"Evee"
}

listPokemons = []

def atualizarPosicao(acao, valorPosicaoLinhaOuColuna):
    match acao:
        case 8:
            valorPosicaoLinhaOuColuna -= 1
            return valorPosicaoLinhaOuColuna
        case 2:
            valorPosicaoLinhaOuColuna += 1
            return valorPosicaoLinhaOuColuna
        case 4:
            valorPosicaoLinhaOuColuna -= 1
            return valorPosicaoLinhaOuColuna
        case 6:
            valorPosicaoLinhaOuColuna += 1
            return valorPosicaoLinhaOuColuna

def validarPosicao(linha, coluna, mapa):
    if(mapa[linha][coluna] == "A"):
        return False
    
def gramaPokemon():
    if(aleatorio(1) == 1):

        print("""

Um pokemon selvagem apareceu!
Capturar ou correr? [1-Capturar ou 2-Correr]

        """)

        op = int(input())
        if(op == 1):
            if(pokemon[str(aleatorio(9))] in listPokemons):
                print("Pokemon ja inserido")
            else:
                listPokemons.append(pokemon[str(aleatorio(9))])

        elif(op == 2):
            print("Fujão")

def validarValoresDeEntrada(op, valores):
    if op in valores:
        print()
    else:
        print("Valor invalido! Os valores disponiveis são {}".format(valores))

def menu():

    print("""

Bem-vindo!
A qualquer momento você pode escolher uma das opções:
 9 - Para abrir esse menu
 8 - Subir
 2 - Descer
 4 - Ir para esquerda
 6 - Ir para direta
 5 - Abrir Pokedex
 0 - Sair do Jogo

    """)

def menuPokedex():

    print("""

Digite
1 para Listar Detalhes
2 para Apagar Registro
0 para voltar ao menu principal
Escolha uma ação:

    """)

    op = int(input())
    validarValoresDeEntrada(op, [1,2,0])
    match op:
        case 1:
            for i in range(len(listPokemons)):
                print(listPokemons[i])
                print(status)
        case 2:
            deletPokemon = input("Digite a espécie do pokemon :")
            listPokemons.remove(deletPokemon)
        case 0:
            menu()

while (True):

    menu()  
    if(aux == 0):
        print("Entrando na Rota 1")
    print("Sua posição atual : [{}] [{}]".format(posicaoLinha, posicaoColuna))
    opcaoMenu = int(input(""))
    validarValoresDeEntrada(opcaoMenu, [9,8,2,4,6,5,0])
    aux += 1

    match opcaoMenu:
        case 0:
            print("Fim de jogo")
            break
        case 9:
            menu()
        case 8:
            try:
                posicaoLinha = atualizarPosicao(8, posicaoLinha)
                if(validarPosicao(posicaoLinha, posicaoColuna, mapa) == False):
                    print("Bump!")
                    posicaoLinha += 1
                elif(mapa[posicaoLinha][posicaoColuna] == "E"):
                    print("Bump!")
                    posicaoLinha += 1
                elif(mapa[posicaoLinha][posicaoColuna] == "G"):
                    gramaPokemon()
            except:
                print("Fim de jogo")
                break
        case 2:
            try:
                posicaoLinha = atualizarPosicao(2, posicaoLinha)
                if(validarPosicao(posicaoLinha, posicaoColuna, mapa) == False):
                    print("Bump!")
                    posicaoLinha -= 1
                elif(mapa[posicaoLinha][posicaoColuna] == "G"):
                    gramaPokemon()
            except:
                print("Fim de jogo")
                break
        case 4:
            posicaoColuna = atualizarPosicao(4, posicaoColuna)
            if(validarPosicao(posicaoLinha, posicaoColuna, mapa) == False):
                print("Bump!")
                posicaoColuna += 1
            elif(mapa[posicaoLinha][posicaoColuna] == "G"):
                gramaPokemon()
        case 6:
            posicaoColuna = atualizarPosicao(6, posicaoColuna)
            if(validarPosicao(posicaoLinha, posicaoColuna, mapa) == False):
                print("Bump!")
                posicaoColuna -= 1
            elif(mapa[posicaoLinha][posicaoColuna] == "G"):
                gramaPokemon()
        case 5:
            menuPokedex()
    if(len(listPokemons) == 10):
        print("Parabéns! Você completou a pokedex.")
        break
        
