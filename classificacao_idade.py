idade = int(input("Por favor, digite sua idade : "))

if idade < 12:
    print ("Recomendamos o filme infantil FILME 1")
elif 12 <= idade < 18:
    print("Recomendamos o filme adolescente FILME 2")
else:
    print("Recomendamos o FILME 3")

quantidade_ingressos = 5
if quantidade_ingressos > 0:
    print("Ingressos estão disponiveis")
else:
    print("Desculpe, todos os ingressos estão esgotados") 