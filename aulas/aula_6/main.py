from leitor import Leitor

palavras_prejorativas = Leitor.carregar_palavras("termos.csv")

comentarios_bons = []
comentarios_prejorativos = []
contador = {}
contagem = 0

print("1 - Comentar\n2 - Sair")
opcao = input("Digite a opção: ")

while(opcao != "2"):

    if contagem > 0:
        opcao = input("\nDigite a opção: ")

    if opcao == "1":
        comentario = input("Digite: ")
        print(" ")

        if Leitor.contem_palavras_prejorativas(comentario, palavras_prejorativas):
            comentarios_prejorativos.append(comentario)
            Leitor.ocorrencia_prejorativa(comentario, palavras_prejorativas, contador)
            print("Comentário prejorativo detectado!!!")
        else:
            comentarios_bons.append(comentario)
            print("Comentário autorizado!")

    elif opcao == "2":
        Leitor.exibir_listas(comentarios_prejorativos, comentarios_bons, contador)
        break

    else:
        print("Opção inválida!")

    contagem += 1
