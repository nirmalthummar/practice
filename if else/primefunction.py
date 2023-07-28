def find_prime(numbers):
    prime_numbers = []
    no_prime = []
    
    for num in numbers:
        if num == 1:
            no_prime.append(num)
        elif num == 2:
            no_prime.append(num)
        else:
            prime = True
            for j in range(2,num):
                if num % j == 0:
                    prime = False
                    break
            if prime:
                prime_numbers.append(num)
            else:
                no_prime.append(num)

    return prime_numbers, no_prime

abc = (3,4,5,6,7,8,9,10,11,12,13,200,181,192)
print(find_prime(abc))