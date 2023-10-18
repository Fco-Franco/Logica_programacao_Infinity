#region Tarefa encontrar letra
print("Tarefa encontrar letra");
pular = input("Deseja pular? Digite c para continuar, ou qualquer coisa para pular.\n").lower().strip();

if pular == "c":
    palavra3 = str(input("Digite uma palavra: ")).lower();
    caracter3 = str(input("Digite a caracter: ")).lower();
    numCaracter =0
    acumPos = ""

    print(f"\nDeve ser encontrado o caracter '{caracter3}' na palavra {palavra3}.")


    for pos, i in enumerate(palavra3): 
        # enumerate obtem a posição (índice) e o caractere correspondente em cada iteração do loop for. Você pode adaptar esse conceito para outras linguagens de programação, ajustando a sintaxe.
        if i == caracter3:
            numCaracter +=1
            acumPos+=(str(pos+1)+" , ")

    palavra3SemEspacos = palavra3.replace(" ", "")
    
    printVar=f"\nA palavra/frase '{palavra3}' tem {len(palavra3)} caracteres, ou {len(palavra3SemEspacos)} desconsiderando os espaços, e contém {numCaracter} caracteres '{caracter3}', na(s) posicão(ões): {acumPos}."

    #if acumPos:  # Verifica se acumPos está vazio
    #    acumPos = acumPos[:-2]  # Remove os dois últimos caracteres (espaço e vírgula)
    #    print(f"\nAcumulo de posicao = {acumPos}")

    if numCaracter==0:  # Verifica se acumPos não está vazio antes de imprimir
        printVar = printVar[:-22]  # Remove os dois últimos caracteres (espaço e vírgula)
        print(printVar)
    else:
        printVar = printVar[:-4]
        print(f"{printVar}.")

else:
    print("Pulou tarefa\n")
#endregion 

#region NUMEROS
print("\n==================================================================================\n")
print("Dddd");
pular = input("Deseja pular? Digite c para continuar, ou qualquer coisa para pular.\n").lower().strip();

if pular == "c":
    print("IF \n")  



else:
    print("Pulou tarefa\n")
#endregion 