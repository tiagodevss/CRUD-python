#imports
import pymysql
import InterfaceCRUD

#PySimpleGUI
InterfaceCRUD

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
    selecionardados = cursor.execute("SELECT * FROM dados_do_cliente ORDER BY id ASC")
    valoresLidos = cursor.fetchall()
    for (id, nome, idade, endereço, whatsapp) in valoresLidos:
        print("|ID|======|NOME|=====|IDADE|======|ENDEREÇO|======|WHATSAPP|======\n{} |===| {} |===| {} Anos |===| {} |===| {}".format(id, nome, idade, endereço, whatsapp))


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
    resposta3 = input("Qual o ID da pessoa que você gostaria de excluir da tabela? ")
    cursor3 = "DELETE FROM dados_do_cliente WHERE id = %s"
    dados3 = []
    id = str(resposta3)
    dados3.append(id)
    cursor.execute(cursor3, dados3)
    conexão.commit()
    print("Cliente excluído com sucesso!")
    

if opçãoInicial == "4":
    print('Certo, você escolheu a opção: "Atualizar cadastro"\n')
    id4 = input("Qual o ID do cadastro que você quer atualizar? ")
    resposta4 = input("Qual informação você quer atualizar? \n1 - Nome\n2 - Idade\n3 - Endereço\n4 - Whatsapp\n\nResponda:")
    cursor4 = "UPDATE FROM dados_do_cliente WHERE id = %s"
    dados4 = []
    id = str(id4)
    dados4.append(id)
    cursor.execute(cursor4, dados4)
    conexão.commit()
    print("Cliente atualizado com sucesso!")
