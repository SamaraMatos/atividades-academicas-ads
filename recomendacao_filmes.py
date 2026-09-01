filmes = ["filme 1 ", "filme 2 ", "filme 3 ", "filme 4" ,"filme 5 "]

print("BEM-VINDO À CLASSIFICAÇÃO DE FILMES!")
print("Você tem 4 filmes para classificar")
print("Digite '0' a qualquer momento para sair")

for filme in filmes :
    classificacao = input(f"Como você classificaria '{filme}' de 1 a 5 (ou 0 para sair)")

    if classificacao == '0' :
        print("Que pena que você não irá classificar mais os filmes")
        break

    try:
        classificacao = int(classificacao)
        if classificacao < 1 or classificacao > 5:
            print("Por favor digite uma classificação válida de 1 a 5:")
        else:
            print(f"Você classificou '{filme}' com {classificacao} estrela \n")
            print("Obrigado por classificar nos filmes")
    except ValueError:
        print("Por favor digite um número válido de 1 a 5:")