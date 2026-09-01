notas = []

print("olá bem vindo ao sistema de notas")

print("lembrando que voçê pode adicionar quantas notas for necessário")

print("Vamos lá!")

entrada = (input("Digite sua nota:"))

entrada = float(entrada)

notas.append(entrada)


while True:
    entrada = input("Digite sua proxima nota:")

    entrada = float(entrada)

    notas.append(entrada)

    continua = input("Deseja adicionar mais notas? (s/n)")

    if continua.lower() != "s" :

        break

print("suas notas são:", notas)

maior = max(notas)

menor = min(notas)

print("a maior nota é:", maior)

print("a menor nota é:", menor)


aprovados = [n for n in notas if n >= 7]

reprovados = [n for n in notas if n < 7]

porc_aprov = (len(aprovados) / len(notas)) * 100

porc_reprov = (len(reprovados) / len(notas)) * 100

print(f"Aprovados: {porc_aprov:.2f}%")

print(f"Reprovados: {porc_reprov:.2f}%")


media = sum(notas) / len(notas)

if media >= 7:
    
    print("você está aprovado")

else:
        media < 7 

        print("você está reprovado")