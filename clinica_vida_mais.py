import matplotlib.pyplot as plt

class Paciente:
    def __init__(self, nome, idade, telefone):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone

pacientes = [
    Paciente("João", 30, "123-456-7890"),
    Paciente("Maria", 25, "987-654-3210"),
    Paciente("Pedro", 35, "555-555-5555")
]

def cadastrar_paciente():
    nome = input("Digite o nome do paciente: ")
    while True:
        idade = input("Digite a idade do paciente: ")
        if idade.isdigit() and 0 <= int(idade) <= 120:
            idade = int(idade)
            break
        else:
            print(" Idade inválida! Digite apenas números.")
    while True:
        telefone = input("Digite o telefone do paciente:(Apenas numéros)")
        if telefone.isdigit() and 8 <= len(telefone) <= 11:
            break
        else:
            print(" Telefone inválido! Digite apenas números.")
    paciente = Paciente(nome, idade, telefone)
    pacientes.append(paciente)
    print("Paciente cadastrado com sucesso!")



def listar_pacientes():
    if not pacientes:
        print("Nenhum paciente cadastrado.")
    else:
        print("Lista de Pacientes:")
        for paciente in pacientes:
            print(f"Nome: {paciente.nome}, Idade: {paciente.idade}, Telefone: {paciente.telefone}")

def buscar_paciente():
    nome = input("Digite o nome do paciente a ser buscado: ")
    for paciente in pacientes:
        if paciente.nome == nome:
            print(f"Nome: {paciente.nome}, Idade: {paciente.idade}, Telefone: {paciente.telefone}")
            return
    print("Paciente não encontrado.")


while True:
    print("\n===Bem-Vindo á Clínica Vida+===")
    print("\n1. Cadastrar paciente")
    print("2. Listar pacientes")
    print("3. Buscar paciente")
    print("4. Estatísticas")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        cadastrar_paciente()

    elif opcao == "2":
        listar_pacientes()

    elif opcao == "3":
        buscar_paciente()

    elif opcao == "4":
        print("===Gráfico===")
        if not pacientes:
            print("Nenhum paciente cadastrado.")
        else:
            idades = [paciente.idade for paciente in pacientes]
            media = sum(idades) / len(idades)
            media_arredondada = round(media)
            mais_velho = max(idades)
            mais_novo = min(idades)
            total_pacientes = len(idades)

            plt.bar(['Média Idade', 'Mais velho', 'Mais novo', 'Quantidades de Pacientes'], [media, mais_velho, mais_novo, total_pacientes])
            colour = ['blue', 'green', 'red', 'yellow']
            plt.xlabel('Estatísticas')
            plt.ylabel('Valores')
            plt.title('Gráfico de Estatísticas')
            plt.show()
            print("===Estatísticas===")
            print(f"Média de idade: {media_arredondada} anos")
            print(f"Paciente mais velho: {mais_velho} anos")
            print(f"Paciente mais novo: {mais_novo} anos")
            print(f"Total de pacientes: {total_pacientes}")

    elif opcao == "5":
        print("Saindo do programa. Até logo!")
        break
    print("Opção inválida. Tente novamente.")
