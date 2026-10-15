from finsight.processor import calcular_total, validar_valor
transacoes = [
    {"tipo": "deposito", "valor": 1500},
    {"tipo": "saque", "valor": 200},
    {"tipo": "deposito", "valor": 750}
]

total_depositos = calcular_total(transacoes, "deposito")
total_saques = calcular_total(transacoes, "saque")
valor_valido = validar_valor(100)

print(total_depositos)
print(total_saques)
print(valor_valido)
