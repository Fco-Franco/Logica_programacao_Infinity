# region prova 01 ======================================================================
# print("""Escreva um programa que peça ao usuário para adivinhar um número que você deverá escolher com antecedência até que ele acerte. Para ajudar o usuário, o programa deve informar se o número é maior ou menor que o número a ser adivinhado. Ao final, imprima o número adivinhado e a quantidade de tentativas.""")

# numEscolhido=int(50)
# tentativas=0
# print("\nEu escolhi um número inteiro e positivo. Tente adivinhar. Digite um numero: \n")

# while True:
#     numeroDigitado = input()
#     if numeroDigitado.isdigit(): # verifica se todos os caracteres em uma string são dígitos numéricos (0 a 9)
#         numeroDigitado = int(numeroDigitado)
#         tentativas+=1
#         if numEscolhido==numeroDigitado:
#             print(f"\nAcertou, o numero é {numeroDigitado}")
#             print(f"Voce acertou em {tentativas} tentativa(s)")
#             print("O número de tentativa(s) é contabilizado apenas considerando a quantidade de números inteiros e positivos digitados\n")
#             break
#         elif numEscolhido>numeroDigitado:
#             print("O número que eu escolhi é maior que o número digitado, tente novamente. Digite um número inteiro e positivo:")
#         elif numEscolhido<numeroDigitado:
#             print("O número que eu escolhi é menor que o número digitado, tente novamente. Digite um número inteiro e positivo:")
#     else:
#         print("Não digitou um número inteiro e positivo. Tente novamente. Digite um número inteiro e positivo: ")
# correcao: Você só esqueceu de colocar uma condicional no segundo 'elif'
# endregion

# region exercicios 02 ======================================================================
# cont = 0
# var = -1
# while cont < 2:

#     for var in range(0, 5):

#         cont = var
# print('Ok!')
# O código está correto e a saída será: Ok!

# cont = 0
# var = 0
# while True:
#     var = 3
#     if cont + var == 3:
#         break
#     var += cont
# print("Fim")
# endregion

# region prova 02 ======================================================================
# Desenvolva um programa que leia o nome, idade e sexo de 5 pessoas. No final do programa, exiba - A média de idade de todo o grupo. - Qual o nome da pessoa mais velha. - Quantas pessoas têm menos de 20 anos. - Quantas pessoas têm mais de 40 anos. - Qual o sexo da pessoa mais nova.

# Inicializando variáveis
# somaIdade = 0
# mediaIdade = 0
# idadeMaisVelha = 0
# nomeMaisVelha = ""
# qtdeMenor20 = 0
# qtdeMaior40 = 0
# idadeMaisNova = float('inf')
# sexoMaisNova = ""
# pessoas = {}
# pessoasMaisVelhasArray={}


# for i in range(3):# Entrada de informações
#     print(f"\nDados da pessoa {i + 1}:")

#     while True:#Verifica nome válido
#         nome = input("Digite o nome: ")
#         if nome.replace(' ', '').isalpha():
#             break
#         else:
#             print("Por favor, digite um nome válido sem caracteres especiais nem numeros.")

#     while True:#Verifica idade válida
#         idade = input("Digite a Idade: ")
#         if idade.isdigit(): # verifica se todos os caracteres em uma string são dígitos numéricos (0 a 9)
#             idade = int(idade) 
#             if idade > 0:
#                 break
#             else:
#                 print("A idade deve ser maior que 0(zero). Tente novamente.")
#         else:
#             print("Não digitou uma idade válida. A idade deve ser maior que 0(zero), e um número inteiro positivo, sem espaços. Tente novamente.")

#     while True:#Verifica sexo válido
#         sexo = input("Digite o Sexo (M-masculino ou F-Feminino): ").lower()
#         if sexo!="f" and sexo!="m":
#             print("Não digitou um sexo valido. O sexo deve M para masculino ou F para Feminino, sem espaços. Tente novamente.")
#         else:
#             break
#     print(f"""Dados da pessoa {i + 1}: 
#                 Nome: {nome}, Idade: {idade} anos, Sexo: {sexo}""")


#     if idade in pessoas:
#             pessoas[idade].append(nome)
#     else:
#         pessoas[idade] = [nome]
            
    
#     somaIdade += idade# Calculando média de idades

    
#     if idade > idadeMaisVelha:# Verificando pessoa mais velha
#         if idade in idadeMaisVelha:
#             pessoasMaisVelhasArray.append(nome)
#             idadeMaisVelha = idade
#             nomeMaisVelha = nome

    
#     if idade < 20:# Verificando pessoas com menos de 20 anos
#         qtdeMenor20 += 1

   
#     if idade > 40: # Verificando pessoas com mais de 40 anos
#         qtdeMaior40 += 1

    
#     if idade < idadeMaisNova:# Verificando pessoa mais nova
#         idadeMaisNova = idade
#         sexoMaisNova = sexo


# if somaIdade > 0:# Calculando média de idades
#     mediaIdade = somaIdade / 5

# # Resultados
# print(f"\nMédia de idade do grupo: {mediaIdade:.2f} anos.")
# for idade, nomes in pessoas.items():
#     if len(nomes) > 1:
#         print(f"Pessoas com a mesma idade ({idade} anos): {', '.join(nomes)}")

# if len(pessoasMaisVelhasArray) > 1:
#     print(f"As pessoas mais velha tem {idadeMaisVelha} anos. e são: {pessoasMaisVelhasArray}")
# else:
#     print(f"A pessoa mais velha é o(a) {nomeMaisVelha} e tem {idadeMaisVelha} anos.")
    
# print(f"Tem {qtdeMenor20} pessoa(s) com menos de 20 anos.")
# print(f"Tem {qtdeMaior40} pessoa(s) com mais de 40 anos.")
# if sexoMaisNova=="m":
#     sexoMaisNova="masculino"
# else:
#     sexoMaisNova="feminino"
# print(f"A pessoa mais nova é do sexo {sexoMaisNova}")

# endregion


# region prova 02 ======================================================================
# Desenvolva um programa que leia o nome, idade e sexo de 5 pessoas. No final do programa, exiba - A média de idade de todo o grupo. - Qual o nome da pessoa mais velha. - Quantas pessoas têm menos de 20 anos. - Quantas pessoas têm mais de 40 anos. - Qual o sexo da pessoa mais nova.
# somaIdade = 0
# mediaIdade = 0
# idadeMaisVelha = 0
# nomeMaisVelha = ""
# qtdeMenor20 = 0
# qtdeMaior40 = 0
# idadeMaisNova = 1
# # idadeMaisNova = float('inf')
# sexoMaisNova = ""
# pessoas = []
# pessoasMaisVelhasArray = []
# pessoasMaisNovasArray = []

# # Entrada de informações
# for i in range(3):
#     print(f"\nDados da pessoa {i + 1}:")

#     while True:  # Verifica nome válido
#         nome = input("Digite o nome: ")
#         if nome.replace(' ', '').isalpha():
#             break
#         else:
#             print("Por favor, digite um nome válido sem caracteres especiais nem números.")

#     while True:  # Verifica idade válida
#         idade = input("Digite a Idade: ")
#         if idade.isdigit():  # verifica se todos os caracteres em uma string são dígitos numéricos (0 a 9)
#             idade = int(idade)
#             if idade > 0:
#                 break
#             else:
#                 print("A idade deve ser maior que 0(zero). Tente novamente.")
#         else:
#             print("Não digitou uma idade válida. A idade deve ser maior que 0(zero), e um número inteiro positivo, sem espaços. Tente novamente.")

#     while True:  # Verifica sexo válido
#         sexo = input("Digite o Sexo (M-masculino ou F-Feminino): ").lower()
#         if sexo != "f" and sexo != "m":
#             print("Não digitou um sexo valido. O sexo deve M para masculino ou F para Feminino, sem espaços. Tente novamente.")
#         else:
#             break

#     print(f"""Dados da pessoa {i + 1}: 
#                 Nome: {nome}, Idade: {idade} anos, Sexo: {sexo}""")

    
#     somaIdade += idade # Calculando média de idades

    
#     if idade >= idadeMaisVelha:# Verificando pessoa mais velha
#         pessoasMaisVelhasArray.append((idade , nome, sexo))
#         idadeMaisVelha=idade

    
#     if idade < 20: # Verificando pessoas com menos de 20 anos
#         qtdeMenor20 += 1

    
#     if idade > 40: # Verificando pessoas com mais de 40 anos
#         qtdeMaior40 += 1

 
#     if idade >= idadeMaisNova:# Verificando pessoa mais velha
#         pessoasMaisNovasArray.append((nome, sexo))
#         idadeMaisNova=idade

#     if idade < idadeMaisNova:# Verificando pessoa mais nova
#         idadeMaisNova = idade
#         sexoMaisNova = sexo


# if somaIdade > 0:# Calculando média de idades
#     mediaIdade = somaIdade / 5

# # Resultados
# print(f"\nMédia de idade do grupo: {mediaIdade:.2f} anos.")

# if sexoMaisNova == "m":
#     sexoMaisNova = "masculino"
# else:
#     sexoMaisNova = "feminino"

# if len(pessoasMaisVelhasArray) == 1:
#     print(f"A pessoa mais velha é {pessoasMaisVelhasArray[0][1]} com {pessoasMaisVelhasArray[1]} anos.")
# else:
#     print(f"As pessoas mais velhas são: {','.join([nome for idade, nome in pessoasMaisVelhasArray])} , ambas com {pessoasMaisVelhasArray[1][0]} anos.")

# if len(pessoasMaisNovasArray) == 1:
#     print(f"A pessoa mais nova é do sexo {sexoMaisNova}.")
# else:
#     print(f"As pessoas mais novas são: {','.join([nome for idade, nome in pessoasMaisNovasArray])} , ambas com {pessoasMaisNovasArray[1][0]} anos.")

# print(f"Tem {qtdeMenor20} pessoa(s) com menos de 20 anos.")
# print(f"Tem {qtdeMaior40} pessoa(s) com mais de 40 anos.")

# endregion

# region prova https://infinityschool.eadplataforma.app/test/start/272/1740/5669/2591
# Faça um programa em python que determine em duas variáveis (senha e email) e que contenha uma senha e um email cadastrados antecipadamente, em seguida solicite ao usuário uma senha e um email e utilize o laço de repetição juntamente com a estrutura de condição para verificar se o email e a senha digitado pelo usuário é igual ao email e senha cadastrados antecipadamente. E enquanto a senha e o email que o usuário digitou não for igual ao email e senha cadastrados ele continue em um loop.

# Email e senha cadastrados
emailCadastrado = "eu@email.com"
senhaCadastrada = "123qs"

emailLogin = input("Digite o seu email: ")
senhaLogin = input("Digite a sua senha: ")
    
# Enquanto o email ou senha estiverem incorretos
while emailLogin != emailCadastrado or senhaLogin != senhaCadastrada:
    print("\nEmail ou senha incorretos. Tente novamente.")

    # Solicita novamente email e senha
    emailLogin = input("Digite o seu email: ")
    senhaLogin = input("Digite a sua senha: ")

# Se email e a senha são corretos
print(f"\nLogin bem-sucedido! Bem-vindo, {emailLogin} \n")

# endregion

# region prova https://infinityschool.eadplataforma.app/test/start/272/1741/5670/2588
# Faça um programa que solicite ao usuário que digite 10 valores para preencher uma lista. Em seguida, o programa deve separar os números pares e ímpares em listas diferentes. Por fim, exiba na tela os números pares, os números ímpares em uma tupla, a quantidade de números pares e ímpares presentes na lista, e a soma de todos os números pares e ímpares, respectivamente.

# Inicializa as listas para armazenar números pares e ímpares
numeros = []
pares = ()
impares = ()

# Solicita ao usuário que digite 10 valores
for _ in range(10):
    while True:
        try:
            num = int(input("Digite um número inteiro positivo: "))
            if num > 0:
                break  # Sai do loop se o número for inteiro e positivo
            else:
                print("Por favor, digite um número inteiro positivo.")
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

    # Se o loop terminar, significa que o número é válido. Adiciona a lista numeros
    numeros.append(num)


# Asiciona números pares e ímpares, nas respectivas listas
for numero in numeros:
    if numero % 2 == 0:
        pares += (numero,)  # Adiciona o número par à tupla pares
    else:
        impares += (numero,)  # Adiciona o número ímpar à tupla impares


# Resultados
print("Números :", numeros)
print("Números pares:", pares)
print("Números ímpares:", impares)
print("Quantidade de números pares:", len(pares))
print("Quantidade de números ímpares:", len(impares))
print("Soma dos números pares:", sum(pares))
print("Soma dos números ímpares:", sum(impares))

# endregion