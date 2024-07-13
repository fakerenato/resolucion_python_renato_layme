numero_payaso=float(input("Numero de payasos vendidos"))
numero_muñeca=float(input("Numero de muñecas vendidas"))
peso_payaso=0.112*numero_payaso
peso_muñeca=0.075*numero_muñeca
peso_total=peso_muñeca + peso_payaso
print(f"El peso total es {peso_total} kilos")
