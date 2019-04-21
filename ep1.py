# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: nevton coimbra, nevtoncmrc@al.insper.edu.br
# - aluno B: paulo vitor barro, paulovab@al.insper.edu.br

def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": {
                "andar professor": "Tomar o elevador para o andar do professor",
                "biblioteca": "Ir para a biblioteca"
            }
        },
        "andar professor": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
                "sala do professor": "entrar na sala do professor"
            }
        },
        "professor": {
            "titulo": "O monstro do Python",
            "descricao": "Voce foi pedir para o professor adiar o EP. "
                         "O professor revelou que é um monstro disfarçado "
                         "e devorou sua alma.",
            "opcoes": {}
        },
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada"
            }
        }
    }
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual


def main():
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()

    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]
        
        print()
        print("Saguao do perigo")
        print("-"*16)
        print("Voce esta no saguao de entrada do insper")

        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:

            print("Escolha sua opção: ")
            print()
            print("{0}" .format(cenarios["inicio"]["opcoes"]))
            print()
            escolha = input("O que você quer fazer? ")
            if escolha in opcoes:    
                print()
                print(cenarios[escolha]["titulo"])
                x = len(cenarios[escolha]["titulo"])               
                print("-"*x)
                print(cenarios[escolha]["descricao"])
                nome_cenario_atual = escolha
                print()
                if escolha == "biblioteca":
                    print("Escolha sua opção: ")
                    print()
                    print("voltar: voltar para o saguao")
                    escolha = input("O que você quer fazer? ")
                    if escolha in opcoes:
                        return carregar_cenarios()
                    else:
                        print("Sua indecisão foi sua ruína!")
                        game_over = True
                elif escolha == "andar professor":
                    print("Escolha sua opção: ")
                    print()
                    print()
                    
                        
                    
                
                
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True
                
                
            
            

    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()
