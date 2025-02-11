# Exercício 1 - Fatorial com Recursão
# Desenvolva uma função recursiva para calcular o fatorial de um número inteiro.
# Lembre-se de que fat(n) = n * fat(n-1) e fat(0) = 1.
# Chame a função dentro do código principal e peça para o usuário fornecer o número.
def fac(n: float):
    # se o número for igual 1 retorne número
    if n == 1:
        return n
    # return 5 * 4 * 3 * 2 * 1
    return n * fac(n - 1)
# print(fac(5))

# Exercício 2 - Fibonacci com Recursão
# Crie uma função recursiva para calcular o enésimo termo da série de Fibonacci.
# A sequência de Fibonacci é: fib(1) = 1, fib(2) = 1, e fib(n) = fib(n-1) + fib(n-2) para n > 2.
# Peça ao usuário para inserir o valor de n e imprima o valor correspondente da sequência de Fibonacci.
# F(n) = F(n−1) + F(n−2)
def fib(n: float):
    if n == 0:
        return n
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)
# for i in range(10):
#     print(fib(i), end=',')
# print("...", end='')

# Exercício 3 - Soma Recursiva de Números Inteiros
# Crie uma função recursiva que some todos os números inteiros de 1 até 100.
# A função deve receber dois parâmetros: o número atual (nro) e a soma acumulada até o momento.
# A função deve parar quando o número for igual a 100.
def sum_spectrum(i: float, f: float):
    if i > f:
        return 0
    return i + sum_spectrum(i + 1, f)
# print(sum_spectrum(1, 100)) # 5050
# print(sum_spectrum(0, 50)) # 1275
# print(sum_spectrum(1, 12)) # 78

# Exercício 4 - Contagem Regressiva com Recursão
# Implemente uma função recursiva que faça uma contagem regressiva de um número fornecido pelo usuário.
# A contagem deve parar quando o número atingir 0, e a função deve imprimir cada valor na contagem.
def regressive_counter(n):
    print(n, end=' ')
    if n > 0:
        regressive_counter(n - 1)
# regressive_counter(100)

# Exercício 5 - Potência de um Número com Recursão
# Crie uma função recursiva que calcule a potência de um número (base^expoente).
# O usuário deve fornecer a base e o expoente como entrada.
# Lembre-se que base^0 = 1, para qualquer base.
def pow(b: float, e: int):
    if e == 1:
        return b
    return b * pow(b, e - 1)
# print(pow(2,3))

# Exercício 6 - Recursão para Soma dos Dígitos de um Número
# Implemente uma função recursiva que calcule a soma dos dígitos de um número inteiro fornecido pelo usuário.
# Exemplo: para o número 123, a função deve retornar 1 + 2 + 3 = 6.
def sum_digits(n: int):
    if n == 0:
        return n
    return (n % 10) + sum_digits(n//10)

# Exercício 7 - Palíndromo com Recursão
# Crie uma função recursiva que verifique se uma palavra ou número é um palíndromo.
# A função deve retornar True se a palavra ou número for um palíndromo e False caso contrário.
def is_pal(s: str):
    if len(s) <= 1:
        return True
    return s[-1] == s[0] and is_pal(s[1: -1])
# print(is_pal("radar"))  # True
# print(is_pal("ovo"))  # True
# print(is_pal("teste"))  # False
# print(is_pal("1221"))  # True
# print(is_pal("12321"))  # True
# print(is_pal("hello"))  # False

# Exercício 8 - Recursão para Calcular o Máximo Divisor Comum (MDC)
# Implemente a função recursiva para calcular o máximo divisor comum (MDC) de dois números.
# A fórmula do MDC de dois números a e b é: mdc(a, b) = mdc(b, a % b), até que b seja igual a 0.
def mdc(a: float, b: float):
    if b == 0:
        return a
    return mdc(b, a % b)
# Testes
# print(mdc(48, 18))  # 6
# print(mdc(56, 98))  # 14
# print(mdc(101, 103))  # 1

# Exercício 9 - Recursão para Inverter uma String
# Crie uma função recursiva que inverta uma string fornecida pelo usuário.
# A função deve retornar a string invertida sem usar métodos nativos de inversão de strings.
def reverse(s: str):
    if len(s) <= 1:
        return s
    return s[-1] + reverse(s[:-1])
# print(reverse('teste'))

# Exercício 10 - Produto de Dois Números Usando Soma Recursiva
# Implemente uma função recursiva que multiplique dois números inteiros usando apenas somas.
def multiplicacao(a, b):
    pass