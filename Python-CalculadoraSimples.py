
#region  Calculadora simples============================================
def obter_numero(mensagem):
    while True:
        entrada = input(mensagem)
        if entrada.replace(".", "").lstrip('-').isdigit():  # Verifica se a entrada contém apenas dígitos ou ponto decimal
        #replace(".", ""): Remove todos os pontos (caso existam) da string entrada. Isso é útil ao verificar números decimais, pois permite que o ponto decimal seja único e esteja no lugar correto.

        # .lstrip('-'): Remove todos os caracteres de espaço em branco e o sinal de menos ("-") do início da string entrada. Isso é feito para permitir números negativos, pois o sinal de menos é permitido no início.

        # .isdigit(): Retorna True se todos os caracteres na string forem dígitos (0 a 9) e a string não estiver vazia. Caso contrário, retorna False. Isso é utilizado para verificar se a string entrada contém apenas dígitos, o que é um indicativo de que pode ser convertida para um número.

            return float(entrada)
        else:
            print("Entrada inválida. Digite um número válido.")

def operacaoMatematica(num1, num2, operacao):
    # Bloco condicional para chamar a função apropriada
    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 - num2
    elif operacao == "*":
        resultado = num1 * num2
    elif operacao == "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Erro: Divisão por zero.")
            return None
    else:
        print("Operação inválida.")
        return None

    # Exibe o resultado
    print(f"\nResultado: {num1} {operacao} {num2} = {resultado:.2f}.")
    return resultado

# Programa principal
while True:
    # Solicitação de entrada do usuário
    num1 = obter_numero("Entre com o número 1: ")
    num2 = obter_numero("Entre com o número 2: ")
    operacao = input("Entre com a operação (+, -, *, /): ")

    # Chama a função operacaoMatematica
    resultado = operacaoMatematica(num1, num2, operacao)

    # Verifica se o usuário deseja continuar calculando
    continuar = input("\nDeseja continuar calculando? Digite 's' para sim: ")
    if continuar.lower() != 's':
        num1=""
        num2=""
        operacao=""
        break  # Interrompe o loop se o usuário não deseja continuar

# Fim do programa
print("\nPrograma encerrado.\n")

#endregion