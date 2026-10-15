def calcular_total(transacoes, tipo):
    total = 0

    for transacao in transacoes:
        if transacao["tipo"] == tipo:
            total += transacao["valor"]   

    return total


def validar_valor(valor):
   return valor > 0
