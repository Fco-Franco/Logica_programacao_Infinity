
# Leia os dados de um usuário - nome, sobrenome, idade, email - e imprima-os enumerando os mesmos. Leia 4 notas de um aluno, calcule sua média e armazene em um dicionário as seguintes informações:a. Nome do aluno b. As 4 notas obtidas c. Maior nota d. Menor nota e. Média f. Situação Agora imprima as informações deste aluno na saída padrão

#Valida nome. Tem que instalar unidecode: escreva pip install unidecode============================
from unidecode import unidecode
def nomeValid(texto):
    nomeSemAcento = unidecode(texto)
    return nomeSemAcento.replace(" ", "").isalpha()
while True:
    nome = input("Digite um nome do aluno: ")
    if nomeValid(nome):
        break
    else:
        print("Nome inválido. O nome não deve conter numeros nem caracteres especiais. Por favor, digite novamente.")

#Valida sobrenome. Tem que instalar unidecode: escreva pip install unidecode============================
from unidecode import unidecode
def sobrenomeValid(texto):
    sobrenomeSemAcento = unidecode(texto)
    return sobrenomeSemAcento.replace(" ", "").isalpha()
while True:
    sobrenome = input("Digite um sobrenome do aluno: ")
    if sobrenomeValid(sobrenome):
        break
    else:
        print("Sobrenome inválido. O sobrenome não deve conter numeros nem caracteres especiais. Por favor, digite novamente.")

# Verificacao de entrada tipo int para idade 
while True:
    idade = input("Digite o idade do Aluno:  ")
    if idade.isdigit(): # verifica se todos os caracteres em uma string são dígitos numéricos (0 a 9)
        idade = int(idade) 
        if idade > 0:
             break
        else:
            print("Idade não pode ser 0(zero).")
    else:
        print("Não digitou uma idade válido. Tente novamente.")

# Verificacao de entrada para email 
import re
def emailValido(email):
    # Expressão regular para validar um endereço de e-mail
    padrao = re.compile(r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$')
    # Verifica se o e-mail corresponde ao padrão
    return padrao.match(email) is not None
# Loop infinito para solicitar ao usuário que digite um e-mail válido
while True:
    # Solicita ao usuário que digite um e-mail e armazena o valor em 'email'
    email = input("Digite o email do Aluno: ")
    # Chama a função 'validar_email' para verificar se o e-mail é válido
    if emailValido(email):
        break  # Sai do loop se o e-mail for válido
    else:
        print("E-mail inválido. Por favor, digite novamente.")

notas={}
aluno={ "Nome": nome , "Sobrenome": sobrenome, "Idade": idade, "Email":email}
somaNotas = 0
alunoPrint=(f"""Dados do Aluno: 
      Nome: {aluno['Nome']} {aluno['Sobrenome']}
      Idade: {aluno['Idade']}
      Email: {aluno['Email']}""")

print(alunoPrint)

qtdeNotas=int(input("Quantas notas vai lancar? "))
qtdeNotas=qtdeNotas+1

# Loop infinito para solicitar ao usuário que digite notas validas
for i in range(1,qtdeNotas):
    while True:
        try:
            nota = float(input(f"Digite a {i}ª nota do aluno: "))
            if 0 <= nota <= 10:
                notas[f"Nota {i}"] = nota
                somaNotas += nota
                break  # Sai do loop interno se a entrada for válida
            else:
                print("Digite uma nota válida (entre 0 e 10).")
        except ValueError:
            # Se ocorrer um erro durante a conversão, imprime uma mensagem de erro e continua no loop
            print("A entrada deve ser um numero e estar entre 0 e 10.")

media=somaNotas/len(notas)

print(f"""\nResumo:
   {(alunoPrint)}""")

print("\nNotas:" )
for i, (key, value) in enumerate(notas.items()):
    if i == len(notas) - 1:  # Último item
        print(f"    {key}: {value}", end="")
    else:
        print(f"    {key}: {value}", end=", ")

print(f"""\n    Média: {(media)}\n""")
