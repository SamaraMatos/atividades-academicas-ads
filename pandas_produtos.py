import pandas as pd

dados = {
    'nome' : ['produto A', 'produto B', 'produto c', 'produto A', 'produto E'],
    'quantidade de itens comprado' : [10, 20, 30, 10, 15],
    'tipo do item' : ['eletronico', 'roupas', 'alimentos', 'eletronico', 'alimneto'],
    'valor total' : [120, 20, 80, 120, 50]
}

df = pd.DataFrame(dados)
print(df)

df.drop_duplicates(keep='last', inplace=True)
print(df)

df["Preço do item"] = df['valor total'] / df['quantidade de itens comprado']
itens_acima_de_50 = df[df['Preço do item'] > 50]
print(itens_acima_de_50)
print(df)