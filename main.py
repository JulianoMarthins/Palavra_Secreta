from random import choice
from time import sleep
import os


# Função de seleção das categorias das palavras secretas do jogo
def menu_escolha(categoria_jogo):
    while True:
        escolha = input(categoria_jogo)
        try:
            num = int(escolha)

            match num:
                case 1:

                    print("Você escolheu\n\033[1;34mTIMES DE FUTEBOL\033[m\n\n")
                    print('Palavra secreta selecionada:\nBoa sorte\n')
                    sleep(0.5)
                    lista = ['AMERICA', 'ATLETICO', 'BAHIA', 'BOTAFOGO', 'CORINTHINS', 'CORITIBA', 'CRUZEIRO', 'CUIABA',
                             'FLAMENGO',
                             'FLUMINENSE', 'FORTALEZA', 'GOIAS', 'GREMIO', 'INTERNACIONAL', 'PALMEIRAS', 'BRAGANTINO',
                             'SANTOS', 'AVAI', 'CEARA', 'CHAPECOENSE',
                             'CRICIUMA', 'GUARANI', 'JUVENTUDE', 'LONDRINA', 'SPORT', 'VITORIA', 'FIGUEIRENSE',
                             'NAUTICO', 'PAYSANDU', 'REMO', 'YPIRANGA',
                             'VASCO DA GAMA', 'SAO PAULO'
                             ]
                    return choice(lista)

                case 2:
                    print("Você escolheu\n\033[1;34mCIDADES BRASILEIRAS\033[m\n\n")
                    print('Palavra secreta selecionada:\nBoa sorte\n')
                    sleep(0.5)

                    lista = ['BRASILIA', 'SALVADOR', 'FORTALEZA', 'BELO HORIZONTE', 'MANAUS', 'CURITIBA', 'RECIFE',
                             'GOIANIA', 'BELEM',
                             'PORTO ALEGRE', 'GUARULHOS', 'CAMPINAS', 'SAO LUIS', 'SAO GONCALO', 'MACEIO',
                             'DUQUE DE CAXIAS', 'CAMPO GRANDE', 'NATAL', 'JOAO PESSOA',
                             'NOVA IGUACU', 'SANTO ANDRE', 'CUIABA', 'LONDRINA', 'PORTO VELHO', 'JUIZ DE FORA',
                             'JOINVILLE', 'FLORIANOPOLIS', 'PELOTAS'
                             ]
                    return choice(lista)

                case 3:
                    print("Você escolheu\n\033[1;34mBANDAS NASCIONAIS\033[m\n\n")
                    print('Palavra secreta selecionada:\nBoa sorte\n')
                    sleep(0.5)

                    lista = ['ANGRA', 'ARNALDO ANTUNES', 'BARAO VERMELHO', 'BIQUINI CAVADAO', 'CACHORRO GRANDE',
                             'CAPITAL INICIAL',
                             'CASCAVELLETES', 'CASSIA ELLER', 'CAZUZA', 'CHARLIE BROWN', 'CPM 22', 'DETONAUTAS',
                             'FREJAT', 'IRA', 'JOTA QUEST', 'KID ABELHA',
                             'LEGIAO URBANA', 'LOS HERMANOS', 'LOBAO', 'LULU SANTOS', 'MAMONAS ASSASSINAS', 'MATANZA',
                             'SKANK', 'SEPULTURA', 'RPM', 'ROUPA NOVA',
                             'ROBERTO CARLOS', 'RITA LEE', 'RAUL SEXIAS', 'RAIMUNDOS', 'PLEBE RUDE', 'PITTY',
                             'PEDRA LETICIA', 'PATU FU', 'NENHUM DE NOS', 'NANDO REIS'
                             ]
                    return choice(lista)

                case 4:
                    print("Você escolheu\n\033[\;34mMARCAS DE CARRO\033[m\n\n")
                    print('Palavra secreta selecionada:\nBoa sorte\n')
                    sleep(0.5)

                    lista = ['ASTON MARTIN', 'AUDI', 'BMW', 'CHERRY', 'CHEVROLET', 'CITROEN', 'FERRARI', 'FIAT', 'FORD',
                             'HONDA',
                             'HYUNDAI', 'JAGUAR', 'JEEP', 'KIA', 'LAMBORGHINI', 'HYUNDAI', 'LAND ROVER', 'MCLAREN',
                             'MERCEDES BENZ', 'MITSUBISHI', 'NISSAN',
                             'PEUGEOT', 'PORSCHE', 'RENAULT', 'SUBARU', 'SUZUKI', 'TOYOTA', 'VOLKSWAGEN', 'VOLVO'
                             ]
                    return choice(lista)

                case _:
                    print('Digite digiou um valor inválido')
                    continue
        except:
            print('Valor inválido\nDigite o número referente a sua escolha: ')


# Variavel recebe String com regras para informar o jogardor
regras = """\033[0;34m
                    Jogo de palavras secretas

                         Regras do jogo

        1°  Palavra não terá caracteres especiais como acentos, ç, etc...
        2°  Espaços são caracteres válidos
        3°  Só é permitido inserir um caracter por jogada
        4°  Você selecionará a categoria que deseja jogar
        5°  Você terá cinco vidas

                             Boa sorte
\033[m        
"""

# Menu de seleção das categorias de palavras secretas
categoria_jogo = """\033[0;34m

            Escolha sua categoria de palavras para jogar

        1   =>  Times do futebol brasileiro
        2   =>  Cidades brasileiras
        3   =>  Bandas nacionais
        4   =>  Marca de carros
\033[m
"""

vidas = 5
digitadas = str()
letras_acertadas = ' '
condicao_while = 0

print(regras)

# Acessa função de escolha da categoria
palavra_secreta = menu_escolha(categoria_jogo=categoria_jogo)

while condicao_while == 0:

    letra = input('\n\nDigite uma letra: ').upper()
    os.system('cls')

    # Valida quantidade de caracteres digitados pelo usuário
    if len(letra) == 0:
        print('\nDigite apenas uma letra')
        continue

    # Armazena cada caracter encontrado na palavra secreta, na variavel letras acertadas
    for letra_secreta in palavra_secreta:
        if letra in letra_secreta:
            sleep(0.7)
            letras_acertadas += letra
    print(f'\n\033[1;32mAcertou\033[m\nVidas: {vidas}\n')

    # Retorna ao usuário a letra acertada ou um # em caso de erro
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            print(letra_secreta, end='')

        else:
            print('#', end='')

    # Consome uma vida do usuário caso ele erre alguma letra, finaliza o jogo se não tiver mais vidas
    if letra not in palavra_secreta:
        vidas -= 1
        sleep(0.7)
        print(f'\n\033[1;31mVocê errou\033[m\nVidas: {vidas}\n')

        if vidas == 0:
            print(f'\n\033[1;31mVOCÊ PERDEU\033[m')

            while True:
                op = input('\n\nDeseja jogar novamente?\n[S]sim [N]não: ').upper()

                if 'S' in op:
                    sleep(0.7)
                    letras_acertadas = ' '
                    vidas = 5
                    palavra_secreta = menu_escolha(categoria_jogo=categoria_jogo)
                    print('Jogo Reiniciando')
                    sleep(0.7)
                    break


                elif 'N' in op:
                    print('\nObrigado por jogar\nEcenrrando programa')
                    sleep(0.7)
                    condicao_while = 1
                    break

                else:
                    print("Digite [S] para continuar\nDigite [N] para encerrar o programa")

    # Verificação de vitória
    espacos = palavra_secreta.count(' ')
    if espacos > 0:
        tot_letras = len(letras_acertadas) - espacos
    else:
        tot_letras = len(letras_acertadas)

    if tot_letras == len(palavra_secreta):
        sleep(0.7)
        print("\n\n\033[1;32mPARABÉNS\033[m\nVOCÊ \033[1;32mVENCEU\033[m")

        while True:
            op = input('\n\nDeseja jogar novamente?\n[S]sim [N]não: ').upper()

            if 'S' in op:
                sleep(0.7)
                letras_acertadas = ' '
                vidas = 5
                palavra_secreta = menu_escolha(categoria_jogo=categoria_jogo)
                print('Jogo Reiniciando')
                sleep(0.7)
                break

            elif 'N' in op:
                print('\nObrigado por jogar\nEcenrrando programa')
                sleep(0.7)
                condicao_while = 1
                break

            else:
                print("Digite [S] para continuar\nDigite [N] para encerrar o programa")