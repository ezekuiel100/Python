valor_inicial = int(input("Valor inicial: "))
taxa = float(input("Taxa de juros: "))
tempo = int(input("Período(anos): "))

total = valor_inicial * (1 + taxa / 100) ** tempo

print(f"Total após {tempo} anos: R$ {total:.2f}")
