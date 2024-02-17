# 3- vairant
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def not_prime_generator(n):
    count = 0
    number = 2
    while count < n:
        if not is_prime(number):
            count += 1
            yield number
        number += 1

n = int(input("n sonini kiriting: "))
not_prime_gen = not_prime_generator(n)

print(f"Dastlabki {n} ta tub bo'lmagan sonlar: ", end="")
for not_prime in not_prime_gen:
    print(not_prime, end=" ")
