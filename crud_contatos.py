import sqlite3
conn = sqlite3.connect("contatos.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS contatos (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    telefone TEXT,
    email TEXT
)
""")

def printar_dados_bancos():
    cursor.execute("SELECT * FROM contatos")
    contatos = cursor.fetchall()
    print("contatos antes excluir:")
    for contato in contatos:
        print(contato)


dados_exemplo = [
    ('Maria', 'maria@hotmail.com', '48996004755'),
    ('Samara', 'samara@hotmail.com', '48996278844'),
    ('Ana', 'ana@hotmail.com', '48996447799')
]

cursor.executemany("""
INSERT INTO contatos (nome, email, telefone)
VALUES (?, ?, ?)
""", dados_exemplo)

printar_dados_bancos()

novo_telefone = 48996354876
contato_id = 1
cursor.execute("""
UPDATE contatos
SET telefone = ?
WHERE id = ?
""", (novo_telefone, contato_id))

printar_dados_bancos()

cursor.execute("""
DELETE FROM contatos
""", ())
cursor.fetchall()

conn.commit()
conn.close