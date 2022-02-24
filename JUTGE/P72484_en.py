def rombo(valor):
   result1 = [" " * (valor - i) + "*" * (i + i - 1) for i in range(1, valor + 1)]
   return "\n".join(result1 + list(reversed(result1[:-1])))
entrada_numero = int(input(""))
print(rombo(entrada_numero))