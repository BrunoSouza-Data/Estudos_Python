inventario = []
resposta = "S"
while resposta == "S":
    inventario.append(input("Equipamento: "))
    inventario.append(float(input("Valor: ")))
    inventario.append(int(input("Número Serial: ")))
    inventario.append(input("Departamento: "))
    # a barra invertida é o caracter de escape. Que serve para colocar aspas dentro de aspas.
    resposta = input("Digite \"S\" para continuar: ").upper()

for elemento in inventario:
    print(elemento)
