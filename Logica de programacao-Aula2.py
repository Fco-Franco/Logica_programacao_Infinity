# https://www.invertexto.com/315aula2logica
# O .upper() transforma em maiusculo, e o .lower() em minusculo.
# O .strip() retira os espaços antes e depois do texto digitado.

# ==================================================================================
#region COMPARA NUMEROS
# print("")
# print("IF")
# print("Digite 2 numeros para comparar:")
# num1 = int(input("Digite o primeiro número : "));
# num2 = int(input("Digite o segundo número : "));
# print("")

# if num1 == num2:
#     print("Números iguais")
# else:
#     print("Números diferentes")
# print("")
#endregion 

# ==================================================================================
#region MAIOR DE IDADE
# print("")
# print("IF")
# idade1 = int(input("Digite a idade: "));
# print("")

# if idade1 >= 18:
#     print("Maior de idade")
# else:
#     print("Menor de idade")
# print("")
#endregion 

# ==================================================================================
#region TESTE NUMERO POSITIVO
# print("")
# print("elif")
# print("")
# num3 = int(input("Digite um número: "));
# print("")

# if num3 > 0:
#     print(num3," é positivo")
# elif num3 < 0:
#     print(num3," é negativo")
# else:
#     print(num3," é nulo")
# print("")
#endregion 

# ==================================================================================
#region TESTE DE COR
# print("")
# print("elif")
# print("")
# cor = input("Digite uma cor: ").upper().strip();
# print("")
# O .upper() transforma em maiusculo, e o .lower() em minusculo.
# O .strip() retira os espaços antes e depois do texto digitado.
# if cor == "VERMELHO":
#     print(cor, " - Pare")
# elif cor == "VERDE":
#     print(cor.upper(), " - Acelera")
# elif cor == "AMARELO":
#     print(cor.lower(), " - Atenção")
# else:
#     print("Cor inválida")
# print("")
#endregion 

# ==================================================================================
#region Condicionais 1
# print("")
# print("Condicionais")
# print("")
# num4 = int(input("Digite uma Numero inteiro: "));
# print("")
# if num4 >= 0 and num4 <= 10:
#     print(num4, " Numero válido")
# else:
#     print("Numero inválida - deve ser entre 0 e 10")
# print("")
#endregion 

# ==================================================================================
#region Condicionais 2
# print("")
# print("Condicionais")
# print("")
# sair = str(input("Deseja sair? (S/N) ")).lower().strip();
# print("")
# if sair == "s" or sair == "n":
#     print("Operação válida")
#     if sair == "s":
#         print("Tchau meu fi, vá com Deus")
#     else: 
#         print("Continue usando o programa")
# else:
#     print("Operação inválida")
# print("")
#endregion 

# ==================================================================================
#region Condicionais Match
# print("")
# print("Condicionais Match")
# print("")
# cor1 = str(input("Digite um cor [Amarelo | Verde | Vermelho] : ")).lower().strip()
# match cor1:
#     case "vermelho":
#         print("")
#         print("Pare sinal ta fechado")
#     case "verde":
#         print("")
#         print("Segue em frente que o sinal ta aberto, vá simbora")
#     case "amarelo":
#         print("")
#         print("Preste atenção que o sinal já vai fechar")
#     case _:
#         print("")
#         print("Cor inválida")
# print("")
#endregion 

# ==================================================================================
#region Exercicio 01
# print("")
# print("Peça dois números e imprima o maior deles.")
# print("")
# numEx1_1 = int(input("Digite dois números : "))

# print("Digite 2 numeros para comparar:")
# print("")
# numEx1_1 = int(input("Digite o primeiro número : "));
# print("")
# numEx1_2 = int(input("Digite o segundo número : "));
# if numEx1_1>numEx1_2:
#     print("")
#     print("Numero 1 Maior")
# elif numEx1_1<numEx1_2:
#     print("")
#     print("Numero 2 Maior")
# else:
#         print("Numeros iguais")
# print("")
#endregion 

# ==================================================================================
#region Exercicio 02
# print("")
# print("Peça um valor e mostre na tela se o valor é positivo ou negativo.")
# print("")
# numEx2 = float(input("Digite um números : "))
# print("")
# if numEx2>0:
#     print(numEx2, " é positivo")
#     print("")
# elif numEx2<0:
#     print(numEx2, " é negativo")
#     print("")
# else:
#     print("O numero é zero")
#     print("")
#endregion 

# ==================================================================================
#region Exercicio 03
# print("")
# print("Verifique se uma letra digitada é 'F' ou 'M' Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.")
# print("")
# letraEx3 = str(input("Digite o sexo (F-Feminino ou M-Masculino) ")).upper().strip()
# print("")
# if letraEx3 == "M":
#     print(letraEx3, " - Masculino")
#     print("")
# elif letraEx3 == "F":
#     print(letraEx3, " - Feminino")
#     print("")
# else:
#     print("Sexo Inválido")
#     print("")

# print("-------------------------")

# if letraEx3 == "f" or letraEx3 == "F":
#     print("F - Femenino")
#     print("")
# elif letraEx3 == "m" or letraEx3 == "M":
#     print("M - Masculino")
#     print("")
# else: 
#     print("Sexo inválido")
#     print("")
#endregion 

# ==================================================================================
#region Exercicio 04
print("")
print("Verifique se Faça um Programa que verifique se uma letra digitada é vogal ou consoante.")
print("")
letraEx4 = str(input("Digite uma letra : ")).lower().strip()
print("")

if len(letraEx4)==1: 
    if letraEx4 in "aeiou":
        print("Vogal")
        print("")
    else:
        print("Consoante")
        print("")

    print("======================================")
    if letraEx4 == "a" or letraEx4 == "e" or letraEx4 == "i" or letraEx4 == "o" or letraEx4 == "u":
        print("Vogal")
        print("")
    else:
        print("Consoante")
        print("")
else:
    print("Digite apenas 1 letra")
    print("")
#endregion 

# ==================================================================================
#region Exercicio 05
# print("")
# print("Faça a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar: ○ A mensagem 'Aprovado', se a média alcançada for maior ou igual a sete; ○ A mensagem 'Reprovado', se a média for menor do que sete;○ A mensagem 'Aprovado com Distinção', se a média for igual a dez.")
# print("")
# print("Digite 2 notas :")
# print("")
# nota1Ex5 = float(input("Digite a primeira nota : "));
# print("")
# nota2Ex5 = float(input("Digite a segunda nota : "));
# mediaEx5 = (nota1Ex5+nota2Ex5)/2;
# print("")
# print("Média : ", mediaEx5)
# print("")

# if mediaEx5<7:
#     print("")
#     print("Reprovado")
# elif mediaEx5==10:
#     print("")
#     print("Aprovado com Distinção")
# else:
#     print("")
#     print("Aprovado")
# print("")
#endregion 



# ==================================================================================
#region Exercicio 06
print("")
print("Faça a leia três números e mostre o maior deles.")
print("")
num1Ex6 = float(input("Digite o primeiro número: "));
print("")
num2Ex6 = float(input("Digite o segundo número: "));
print("")
num3Ex6 = float(input("Digite o terceiro número: "));
print("")


#endregion 


# ==================================================================================
#region QUESTÃO 4 MODO HARD:
letra = str(input("Digite uma letra: ")).lower()

if len(letra) == 1:
    if letra in "aeiou":
        print("É vogal")
    elif letra in "bcdfghjklmnpqrstvxywz":
        print("É consoante")
    else:
        print("Meu fi, digite uma LETRA, sabe o que é letra?")
else:
    print("Digite só UMAAAAAA letra")

#endregion 


# ==================================================================================
#region 

#endregion 


# ==================================================================================
#region 

#endregion 



