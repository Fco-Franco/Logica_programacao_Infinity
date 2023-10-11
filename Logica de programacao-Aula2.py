# O .upper() transforma em maiusculo, e o .lower() em minusculo.
# O .strip() retira os espaços antes e depois do texto digitado.

#region COMPARA NUMEROS
print("==================================================================================")
print("")
print("Digite 2 numeros para compara.");
pular = input("Deseja pular(digite p), ou qualquer coisa para continuar.").lower().strip();
print("")
if pular != "p":
    print("IF")
    print("")   
    num1 = int(input("Digite o primeiro número : "));
    num2 = int(input("Digite o segundo número : "));
    print("")

    if num1 == num2:
        print("Números iguais")
    else:
        print("Números diferentes")
else:
    print("Pulou tarefa")
    print("")
#endregion 

#region MAIOR DE IDADE
print("==================================================================================")
print ("Verificação de maioridade.");
pular = input("Deseja pular(digite p), ou qualquer coisa para continuar.").lower().strip();
print("")
if pular != "p":
    print("IF")
    print("")
    idade1 = int(input("Digite a idade: "));
    print("")

    if idade1 >= 18:
        print(idade1, " anos. Maior de idade")
    else:
        print(idade1, " anos. Menor de idade")
    print("")
else:
    print("Pulou tarefa")
    print("")
#endregion 

#region TESTE NUMERO POSITIVO
print("==================================================================================")
print("")
print ("Verificação se número é positivo.");
pular = input("Deseja pular(digite p), ou qualquer coisa para continuar.").lower().strip();
print("")
if pular != "p":
    print("elif")
    print("")
    num3 = int(input("Digite um número: "));
    print("")
    if num3 > 0:
        print(num3," é positivo")
    elif num3 < 0:
        print(num3," é negativo")
    else:
        print(num3," é nulo")
    print("")
else:
    print("Pulou tarefa")
    print("")
#endregion 

#region TESTE DE COR
print("==================================================================================")
print("")
print ("Verificação de cor.");
pular = input("Deseja pular(digite p), ou qualquer coisa para continuar.").lower().strip();
print("")
if pular != "p":
    print("")
    print("elif")
    print("")
    cor = input("Digite uma cor. Digite: VERMELHO, VERDE, AMARELO.").upper().strip();
    print("")
    # O .upper() transforma em maiusculo, e o .lower() em minusculo.
    # O .strip() retira os espaços antes e depois do texto digitado.
    if cor == "VERMELHO":
        print(cor, " - Pare")
    elif cor == "VERDE":
        print(cor.upper(), " - Acelera")
    elif cor == "AMARELO":
        print(cor.lower(), " - Atenção")
    else:
        print("Cor inválida")
    print("")
else:
    print("Pulou tarefa")
    print("")
#endregion 

#region Condicionais 1
print("==================================================================================")
print("")
print ("Verificação de número inteiro de 0 a 10.");
pular = input("Deseja pular(digite p), ou qualquer coisa para continuar.").lower().strip();
print("")
if pular != "p":
    print("")
    print("Condicionais")
    print("")
    num4 = int(input("Digite uma Numero inteiro: "));
    print("")
    if num4 >= 0 and num4 <= 10:
        print(num4, " Numero válido")
    else:
        print("Numero inválida - deve ser entre 0 e 10")
    print("")
else:
    print("Pulou tarefa")
    print("")
#endregion 

#region Condicionais 2
print("==================================================================================")
print("")
print ("Verificação de S/N.");
pular = input("Deseja pular(digite p), ou qualquer coisa para continuar.").lower().strip();
print("")
if pular != "p":
    print("Condicionais")
    print("")
    sair = str(input("Deseja sair? (S/N) ")).lower().strip();
    print("")
    if sair == "s" or sair == "n":
        print("Operação válida")
        print("")
        if sair == "s":
            print(f"Digitou {(sair)}. Tchau meu fi, vá com Deus")
        else: 
            print(f"Digitou {(sair)}. Continue usando o programa")
    else:
        print("Operação inválida")
        print("")
else:
    print("Pulou tarefa")
    print("")
#endregion 

#region Condicionais Match
print("==================================================================================")
print("")
print ("Verificação de cor com Match");
pular = input("Deseja pular(digite p), ou qualquer coisa para continuar.").lower().strip();
print("")
if pular != "p":
    print("Condicionais Match")
    print("")
    cor1 = str(input("Digite um cor [Amarelo | Verde | Vermelho] : ")).lower().strip()
    match cor1:
        case "vermelho":
            print("")
            print("Pare sinal ta fechado")
        case "verde":
            print("")
            print("Segue em frente que o sinal ta aberto, vá simbora")
        case "amarelo":
            print("")
            print("Preste atenção que o sinal já vai fechar")
        case _:
            print("")
            print("Cor inválida")
    print("")
else:
    print("Pulou tarefa")
    print("")
#endregion 

#region Exercicio 01
print("==================================================================================")
print ("Imprimir o maior Número.");
pular = input("Deseja pular(digite p), ou qualquer coisa para continuar.").lower().strip();
print("")
if pular != "p":  
    print("Digite dois números inteiros e imprima o maior deles.")
    print("")
    numEx1_1 = int(input("Digite dois números : "))

    print("Digite 2 numeros para comparar:")
    print("")
    numEx1_1 = int(input("Digite o primeiro número : "));
    print("")
    numEx1_2 = int(input("Digite o segundo número : "));
    if numEx1_1>numEx1_2:
        print("")
        print("Numero 1 Maior")
    elif numEx1_1<numEx1_2:
        print("")
        print("Numero 2 Maior")
    else:
        print("Numeros iguais")
        print("")
else:
    print("Pulou tarefa")
    print("")
#endregion 

#region Exercicio 02
print("==================================================================================")
print ("Verificação de valor positivo/negativo");
pular = input("Deseja pular(digite p), ou qualquer coisa para continuar.").lower().strip();
print("")
if pular != "p":  
    print("Peça um valor e mostre na tela se o valor é positivo ou negativo.")
    print("")
    numEx2 = float(input("Digite um números : "))
    print("")
    if numEx2>0:
        print(numEx2, " é positivo")
        print("")
    elif numEx2<0:
        print(numEx2, " é negativo")
        print("")
    else:
        print("O numero é zero")
        print("")
else:
    print("Pulou tarefa")
    print("")
#endregion 

#region Exercicio 03
print("==================================================================================")
print ("Verificação de masculino/feminino");
pular = input("Deseja pular(digite p), ou qualquer coisa para continuar.").lower().strip();
print("")
if pular != "p": 
    print("Verifique se uma letra digitada é 'F' ou 'M' Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.")
    print("")
    letraEx3 = str(input("Digite o sexo (F-Feminino ou M-Masculino) ")).upper().strip()
    print("")
    if letraEx3 == "M":
        print(letraEx3, " - Masculino")
        print("")
    elif letraEx3 == "F":
        print(letraEx3, " - Feminino")
        print("")
    else:
        print("Sexo Inválido")
        print("")
    print("-------------------------")
    if letraEx3 == "f" or letraEx3 == "F":
        print("F - Femenino")
        print("")
    elif letraEx3 == "m" or letraEx3 == "M":
        print("M - Masculino")
        print("")
    else: 
        print("Sexo inválido")
        print("")
else:
    print("Pulou tarefa")
    print("")
#endregion 

#region Exercicio 04
print("==================================================================================")
print ("Verificação de vogal/consoante");
pular = input("Deseja pular(digite p), ou qualquer coisa para continuar.").lower().strip();
print("")
if pular != "p": 
    print("Verifique se Faça um Programa que verifique se uma letra digitada é vogal ou consoante.")
    print("")
    letraEx4 = str(input("Digite uma letra : ")).lower().strip()
    print("")

    if len(letraEx4)==1: 
        print("======================================")
        if letraEx4 in "aeiou":
            print("É Vogal")
            print("")
        elif letraEx4 in "bcdfghjklmnpqrstvxywz":
            print("É Consoante")
            print("")
        else:
            print("Nem vobgal nem consoante")
            print("")

        print("======================================")
        print("Considera simbolo consoante")
        if letraEx4 == "a" or letraEx4 == "e" or letraEx4 == "i" or letraEx4 == "o" or letraEx4 == "u":
            print("Vogal")
            print("")
        else:
            print("Nãp é vogal")
            print("")
    else:
        print("Digite apenas 1 letra")
        print("")
else:
    print("Pulou tarefa")
    print("")
#endregion 

#region Exercicio 05
print("==================================================================================")
print ("Verificação de média de notas aluno");
pular = input("Deseja pular(digite p), ou qualquer coisa para continuar.").lower().strip();
print("")
if pular != "p": 
    print("")
    print("Faça a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar: ○ A mensagem 'Aprovado', se a média alcançada for maior ou igual a sete; ○ A mensagem 'Reprovado', se a média for menor do que sete;○ A mensagem 'Aprovado com Distinção', se a média for igual a dez.")
    print("")
    print("Digite 2 notas :")
    print("")
    nota1Ex5 = float(input("Digite a primeira nota : "));
    print("")
    nota2Ex5 = float(input("Digite a segunda nota : "));
    mediaEx5 = (nota1Ex5+nota2Ex5)/2;
    print("")
    print("Média : ", mediaEx5)
    print("")

    if mediaEx5<7:
        print("")
        print("Reprovado")
    elif mediaEx5==10:
        print("")
        print("Aprovado com Distinção")
    else:
        print("")
        print("Aprovado")
    print("")
else:
    print("Pulou tarefa")
    print("")
#endregion 



#region Exercicio 06
print("==================================================================================")
print ("Verificação maior número.");
pular = input("Deseja pular(digite p), ou qualquer coisa para continuar.").lower().strip();
if pular != "p": 
    print("")
    print("Faça a leia três números e mostre o maior deles.")
    print("")
    num1Ex6 = float(input("Digite o primeiro número: "));
    print("")
    num2Ex6 = float(input("Digite o segundo número: "));
    print("")
    num3Ex6 = float(input("Digite o terceiro número: "));
    print("")
else:
    print("Pulou tarefa")
    print("")
#endregion 


#region Exercicio 07
print("==================================================================================")
print ("Verificação menor e maior número.");
pular = input("Deseja pular(digite p), ou qualquer coisa para continuar.").lower().strip();
print("")
if pular != "p": 
    print("Em desenvolvimento")
    print("Faça a leia três números e mostre o maior e o menor deles.")
    print("")
    num1Ex7 = float(input("Digite o primeiro número: "));
    print("")
    num2Ex7 = float(input("Digite o segundo número: "));
    print("")
    num3Ex7 = float(input("Digite o terceiro número: "));
    print("")
else:
    print("Pulou tarefa")
    print("")
#endregion 


#region 
print("==================================================================================")

#endregion 


#region 
print("==================================================================================")

#endregion 



