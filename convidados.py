convidados = ("ANA JULIA" , "EMERSON" , "SAMARA" , "REBECA" , "CLEIDE")
confirmados = ["CLEIDE" , "REBECA"]
nao_confirmados = [convidado for convidado in convidados if convidado not in confirmados]
print("convidados que não confirmaram;")
for pessoa in nao_confirmados:
    print(pessoa)

print("Convidados que já confirmaram:")
for pessoa in confirmados:
    print(pessoa)