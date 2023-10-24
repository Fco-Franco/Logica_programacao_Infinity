
#region 1 Senha ======================================================================================
print("Tarefa gravar senha");
pular = input("Deseja pular? Digite c para continuar, ou qualquer coisa para pular.\n").lower().strip();

if pular == "c":
    senhaValida = False

    while senhaValida==False:
        senha = str(input("Digite sua senha de 6 digitos, sendo: 1 letra minuscula, 1 maiuscula, 1 caracter especial, 1 numero. "));
        minuscula = False
        maiuscula = False
        especial = False
        numero = False

        for caracter in senha:
            if len(senha)!=6:
                print("\nA senha deve ter 6 digitos.\n")
                break
            else:
                match caracter:
                    case " ":
                        print("\nA senha não pode ter espaço.")
                        break
                    case c if caracter.islower():
                        minuscula = True                   
                    case c if caracter.islower():
                        minuscula = True
                    case c if caracter.isupper():
                        maiuscula = True                   
                    case c if caracter in "@#$!&":
                        especial = True
                    case c if caracter.isdigit():
                        numero = True

        if minuscula or maiuscula or especial or numero:
            if not minuscula:
                print("Nao tem minuscula.")
            if not maiuscula:
                print("Nao tem maiuscula.")
            if not especial:
                print("Nao tem especial.")
            if not numero:
                print("Nao tem numero.")
            
        if minuscula and maiuscula and especial and numero:
            print("\nA senha gerada com sucesso.\n");
            senhaValida = False
            break
else:
    print("Pulou tarefa\n")
#endregion

#region 1 Senha ======================================================================================
print("\n==================================================================================\n")
print("Tarefa gravar senha 2");
pular = input("Deseja pular? Digite c para continuar, ou qualquer coisa para pular.\n").lower().strip();

if pular == "c":
    import re

    senha = input("Digite sua senha de no máximo 8 dígitos, sendo: 1 letra minúscula, 1 maiúscula, 1 caracter especial, 1 número: ")

    # Use expressões regulares para verificar a senha
    if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$!])[A-Za-z\d@#$!]{1,8}$", senha):
        print("A senha atende aos critérios especificados.")
    else:
        print("A senha não atende aos critérios especificados.")
else:
    print("Pulou tarefa\n")
#endregion


#region 2 Senha ======================================================================================
print("\n==================================================================================\n")
print("Tarefa gravar senha 3");
pular = input("Deseja pular? Digite c para continuar, ou qualquer coisa para pular.\n").lower().strip();

if pular == "c":
    senhaValida = False

    while senhaValida==False: # Só deixa sair do loop quando a senha for gerada
        senha = str(input("Digite sua senha de 6 digitos, sendo: 1 letra minuscula, 1 maiuscula, 1 caracter especial, 1 numero. "));
        minuscula = False
        maiuscula = False
        especial = False
        numero = False
        space = False

        for caracter in senha: # percorre a senha
            if len(senha)!=6:
                print("\nA senha deve ter 6 digitos.\n")
                break

            elif caracter == " ":
                space = True
            
            elif caracter.islower():
                minuscula = True

            elif caracter.isupper():
                maiuscula = True

            elif caracter in "@#$!&":
                especial = True

            elif caracter.isdigit():
                numero = True

        if len(senha)==4: # Gera as menssagens de erro
            if space:
                print("Nao deve ter espaço.")
            if not minuscula:
                print("Deve ter caracter minuscula.")
            if not maiuscula:
                print("Deve ter caracter maiuscula.")
            if not especial:
                print("Deve ter caracter especial.")
            if not numero:
                print("Deve ter caracter numero.")

        if minuscula and maiuscula and especial and numero : # senha ok
            print("\nA senha gerada com sucesso.\n");
            senhaValida = False
            break
else:
    print("Pulou tarefa\n")
#endregion

#region Tarefa encontrar letra ======================================================================================
print("\n==================================================================================\n")
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

#region NUMEROS ======================================================================================
print("\n==================================================================================\n")
print("Dddd");
pular = input("Deseja pular? Digite c para continuar, ou qualquer coisa para pular.\n").lower().strip();

if pular == "c":
    print("IF \n")  



else:
    print("Pulou tarefa\n")
#endregion 