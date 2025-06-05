valor_inicial = int(input("Valor inicial: "))
taxa = float(input("Taxa de juros: "))
time = int(input("Período(anos): "))

total = valor_inicial * (1 + taxa / 100) ** time

print(f"Total após {time} anos: R$ {total:.2f}")
