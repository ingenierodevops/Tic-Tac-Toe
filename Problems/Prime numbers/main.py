prime_numbers = []
prime_numbers.append(2)

for number in range(3, 1000, 2):
    if all(number % numeros for numeros in prime_numbers):
        prime_numbers.append(number)
