km = int(input("Quantos Km foi percorrido com o veiculo? \n "))
dias = int(input("Quantos dias foi alugado ? \n"))

total_dia = dias * 60
total_km = km * 0.15

total = total_dia + total_km

print(f"O valor total do aluguel é de: {total}")