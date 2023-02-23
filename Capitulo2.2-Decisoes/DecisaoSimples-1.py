nome = input("Digite o nome: ")
idade = int(input("Digite sua idade: "))
prioridade = "Não"
if idade >=65:
    prioridade = "Sim"
print("O paciente " + nome + " possui atendimento prioritário? " + prioridade)