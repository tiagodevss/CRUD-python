#imports
import time
import pymysql

#MySQL
conexão = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "clientes"
)
cursor = conexão.cursor()

#script
print("\nOlá, seja bem vindo ao Cadastro de Clientes")
print("1 - Ver clientes cadastrados\n2 - Cadastrar novo cliente\n3 - Excluir cliente\n4 - Atualizar cadastro")
opçãoInicial = input("\nDigite o número da opção desejada: ")

if opçãoInicial == "1":
    print('Certo, você escolheu a opção: "Ver clientes Cadastrados"')
    cursor.execute("SELECT * FROM dados_do_cliente")
    valoresLidos = cursor.fetchall()[0]

    nome1 = valoresLidos[0]
    idade1 = valoresLidos[1]
    endereço1 = valoresLidos[2]
    whatsapp1 = valoresLidos[3]

    print(nome1, idade1, endereço1, whatsapp1)

if opçãoInicial == "2":
    print('Certo, você escolheu a opção: "Cadastrar novo cliente"')
    print('Insira os dados do cliente: \n')
    nomeCliente = input("Nome completo: ")
    idadeCliente = input("Idade: ")
    endereçoCliente = input("Endereço: ")
    whatsappCliente = input(str("Whatsapp do com DDD: "))
        #Comentando Dados no MySQL
    cadastrarSQL = "INSERT INTO dados_do_cliente (nome,idade,endereço,whatsapp) VALUES (%s,%s,%s,%s)"
    dados = []
    nome = nomeCliente
    idade = idadeCliente
    endereço = endereçoCliente
    whatsapp = whatsappCliente
    dados.append(nome)
    dados.append(idade)
    dados.append(endereço)
    dados.append(whatsapp)
    cursor.execute(cadastrarSQL, dados)
    conexão.commit()
    print("\nCliente cadastrado com sucesso!")

if opçãoInicial == "3":
    print('Certo, você escolheu a opção: "Excluir cliente"')
    resposta3 = input("Qual o nome da pessoa que você gostaria de excluir da tabela? ")

if opçãoInicial == "4":
    print('Certo, você escolheu a opção: "Atualizar cadastro"')