nome = "Franco" ;
idade = 18;
altura = 1.79;
matriculado = True;

print("helo word")
print()
print("nome: ",nome)
print("nome tipo: ",type (nome))
print("nome tipo: ",type (nome))
print()
print("idade: ",idade)
print("idade tipo: ",type (idade))
print()
print("altura: ",altura)
print("altura tipo: ",type (altura))
print()
print("matriculado: ",matriculado)
print("matriculado tipo:",type (matriculado))

print()
nome = str(input("Altere o nome: "));
print("Novo nome:  ",nome)
print("nome tipo: ",type (nome))
print()
print(f"nome tipo: {type (nome)}")
print()
print(f"O nome é: {(nome)}, tipo: {type (nome)}")
print(f"""O nome é: {(nome)}
       tipo: {type (nome)}""")
print()

num1 = float(input("Digite um numero: "));
num2 = float(input("Digite outro numero: "));
print(f"{(num1)} + {(num2)} = {(num1+num2)}")
print(f"{(num1)} + {(num2)} = {(num1+num2)}")
print()

print("Truncando")
print("%.3f"%(num1/num2))
print(f"{(num1)} / {(num2)} = {(num1/num2):.5f}")
# print(f"oi "%.4f"%(num1/num2)")
print()
print("Arredondando")
print("%.4f"%round((num1/num2),2))
print("%.4f"%round((num1/num2),4))
print()

print(f"{(num1):.2f} - {(num2)} = {num1-num2}")
print(f"{(num1)} * {(num2)} = {num1*num2}")
print(f"{(num1)} / {(num2)} = {num1/num2}")
print()


