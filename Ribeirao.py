1) 
def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    return False

num = int(input("Informe o número que deseja verificar: "))

if fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} NÃO pertence à sequência de Fibonacci.")
2)
def contar_a(string):
    contagem = 0
    for letra in string:
        if letra.lower() == 'a':
            contagem += 1
    return contagem


texto = input("Informe uma string: ")


quantidade = contar_a(texto)
print(f"A letra 'a' aparece {quantidade} vezes na string.")
3) INDICE = 12
SOMA = 0
K = 1

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)
4)a-9
b-128
c-49
d-100
e-13
f-20




