a, b = 0, 1
fibonacci = []
while a <= 50:
    fibonacci.append(a)
    a, b = b, a + b

print("Serie de Fibonacci entre 0 y 50:", fibonacci)
