
# region verificacao de entrada tipo int ====================IMPORTANT====================
# Loop infinito para solicitar ao usuário que digite um número inteiro positivo
while True:
    # Solicita ao usuário que digite um número inteiro e armazena o valor em 'num_str'
    num_str = input("Digite um número inteiro: ")
    
    # Verifica se todos os caracteres em 'num_str' são dígitos numéricos (0 a 9)
    if num_str.isdigit():
        # Converte 'num_str' para um número inteiro
        num = int(num_str)
        
        # Verifica se o número é positivo
        if num > 0:
            break  # Sai do loop se o número for positivo
        else:
            print("Digite um número inteiro positivo.")
    else:
        # Se 'num_str' não contiver apenas dígitos, imprime uma mensagem de erro e continua no loop
        print("Não digitou um número inteiro válido. Tente novamente.")

# Se o loop for interrompido, imprime o número inteiro positivo digitado
print("Você digitou um número inteiro positivo:", num)

#endregion verificacao de entrada tipo int

# region verificacao de entrada tipo int ou float ====================IMPORTANT====================
# Loop infinito para solicitar ao usuário que digite um número (inteiro ou de ponto flutuante)
while True:
    # Solicita ao usuário que digite um número e armazena o valor em 'entrada'
    entrada = input("Digite um número (inteiro ou de ponto flutuante): ")

    try:
        numero = float(entrada)  # Tente converter a entrada para um número de ponto flutuante
        # Verifica se o número é um número inteiro
        if numero.is_integer():
            print("Você digitou um número inteiro:", int(numero))
        else:
            print("Você digitou um número de ponto flutuante:", numero)
        break  # Sai do loop após a entrada válida
    except ValueError:
        # Se ocorrer um erro durante a conversão, imprime uma mensagem de erro e continua no loop
        print("A entrada não é um número válido. Tente novamente.")

# endregion verificacao de entrada tipo int ou float

# region verificacao de entrada contem uma vogal, acentuada ou não ====================IMPORTANT====================
# Define uma função chamada 'tem_vogal' que verifica se um texto contém pelo menos uma vogal
def tem_vogal(texto):
    # Itera sobre cada caractere no texto
    for caractere in texto:
        # Verifica se o caractere é uma letra (alfabética)
        if caractere.isalpha():
            # Se encontrar pelo menos uma vogal, retorna True
            return True

    # Se nenhum caractere alfabético for uma vogal, retorna False
    return False

# Solicita ao usuário que digite um texto e armazena o valor em 'texto_digitado'
texto_digitado = input("Digite um texto: ")

# Chama a função 'tem_vogal' para verificar se o texto digitado contém pelo menos uma vogal
if tem_vogal(texto_digitado):
    # Se a função retorna True, imprime que o texto contém pelo menos uma vogal
    print("O texto contém pelo menos uma vogal.")
else:
    # Se a função retorna False, imprime que o texto não contém nenhuma vogal
    print("O texto não contém nenhuma vogal.")

# endregion verificacao de entrada contem uma vogal, acentuada ou não

# region verificacao de entrada de nome, acentuada ou não, sem caracter especial, nem numero. Tem que instalar unidecode: escreva pip install unidecode ====================IMPORTANT===================
# Importa a função 'unidecode' da biblioteca 'unidecode'
from unidecode import unidecode
# Define uma função chamada 'nomeValid' que verifica se o texto contém apenas letras (considerando vogais acentuadas e cedilha)
def nomeValid(texto):
    # Normaliza a string, removendo a acentuação
    nomeSemAcento = unidecode(texto)
    # Substitui os espaços por uma string vazia e verifica se o restante contém apenas letras
    return nomeSemAcento.replace(" ", "").isalpha()
# Loop infinito para solicitar ao usuário que digite um nome válido
while True:
    # Solicita ao usuário que digite um nome
    nome = input("Digite um nome: ")

    # Verifica se o nome fornecido é válido usando a função 'nomeValid'
    if nomeValid(nome):
        # Se o nome for válido, sai do loop
        break
    else:
        # Se o nome não for válido, imprime uma mensagem de erro e continua no loop
        print("Nome inválido. O nome não deve conter números nem caracteres especiais. Por favor, digite novamente.")

# endregion 

# region verificacao de entrada de email valido ===================IMPORTANT===================
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
        print(f"Email valido: {email}")
        break  # Sai do loop se o e-mail for válido
    else:
        print("E-mail inválido. Por favor, digite novamente.")

#endregion