import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

conexao = sqlite3.connect("dados_venda.db")
cursor = conexao.cursor()

df_vendas = pd.read_sql_query("SELECT * FROM vendas1", conexao)

df_vendas['data_venda'] = pd.to_datetime(df_vendas['data_venda'])

vendas_categoria = df_vendas.groupby('categoria')['valor_venda'].sum().reset_index()

df_vendas["mes"] = df_vendas["data_venda"].dt.month
vendas_mensais = df_vendas.groupby("mes")["valor_venda"].sum().reset_index()

cursor.execute('''
CREATE TABLE IF NOT EXISTS vendas1 (
    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
    data_venda DATE,
    produto TEXT,
    categoria TEXT,
    valor_venda REAL
)
''')

cursor.execute("SELECT COUNT(*) FROM vendas1")
if cursor.fetchone()[0] == 0:
    cursor.execute('''
    INSERT INTO vendas1 (data_venda, produto, categoria, valor_venda) VALUES
    ('2023-01-01', 'Produto A', 'Eletrônicos', 1500.00),
    ('2023-01-05', 'Produto B', 'Roupas', 350.00),
    ('2023-02-10', 'Produto C', 'Eletrônicos', 1200.00),
    ('2023-03-15', 'Produto D', 'Livros', 200.00),
    ('2023-03-20', 'Produto E', 'Eletrônicos', 800.00),
    ('2023-04-02', 'Produto F', 'Roupas', 400.00),
    ('2023-05-05', 'Produto G', 'Livros', 150.00),
    ('2023-06-10', 'Produto H', 'Eletrônicos', 1000.00),
    ('2023-07-20', 'Produto I', 'Roupas', 600.00),
    ('2023-08-25', 'Produto J', 'Eletrônicos', 700.00),
    ('2023-09-30', 'Produto K', 'Livros', 300.00),
    ('2023-10-05', 'Produto L', 'Roupas', 450.00),
    ('2023-11-15', 'Produto M', 'Eletrônicos', 900.00),
    ('2023-12-20', 'Produto N', 'Livros', 250.00);
    ''')

conexao.commit()

print("Prévia dos dados de vendas:")
print(df_vendas.head())

print("\nEstatísticas descritivas:")
print(df_vendas.describe())

print("\nVendas por categoria:")
print(vendas_categoria)

print("\n Vendas mensais")
print(vendas_mensais)

plt.subplot(1,2,1)
sns.barplot(data=vendas_categoria, x="categoria", y="valor_venda", palette="viridis")
plt.title("Vendas por Categoria")

plt.subplot(1,2,2)
sns.lineplot(data=vendas_mensais, x="mes", y="valor_venda", marker="o")
plt.title("vendas_mensais (2023)")
plt.xlabel("mes")
plt.ylabel("Valor das Vendas")

plt.tight_layout()
plt.show()

print("\nConclusão e Insights:")
print("- A categoria **Eletrônicos** foi a que mais faturou ao longo do ano.")
print("- As vendas tiveram picos no início do ano (janeiro) e voltaram a crescer no final (novembro/dezembro).")
print("- Livros representam uma categoria de baixo faturamento, mas podem ser explorados com promoções.")
print("- Roupas tiveram vendas consistentes ao longo do ano, representando estabilidade para o negócio.")