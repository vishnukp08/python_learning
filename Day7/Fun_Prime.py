def is_prime(n):
    if n < 2:
        print("Not prime")
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
                break 

        return True

print(is_prime(6))