def multiply(x, y):
    if x < 10 or y < 10:
        print(f"Base case: {x} * {y} = {x * y}")
        return x * y

    # Calculate the size of the numbers
    n = max(len(str(x)), len(str(y)))
    n2 = n // 2

    # Split the numbers into halves
    a, b = divmod(x, 10**n2)
    c, d = divmod(y, 10**n2)

    # Recursive steps
    print(f"Recursive a c call: multiply({a}, {c})")
    ac = multiply(a, c)
    print(f"Recursive b d call: multiply({b}, {d})")
    bd = multiply(b, d)
    print(f"Recursive ab cd call: multiply({a + b}, {c + d})")
    ad_bc = multiply((a + b), (c + d)) - ac - bd

    # Combine the results  Karatsuba algorithm
    result = ac * 10**(2*n2) + ad_bc * 10**n2 + bd

    print(f"Combine results: {ac} * 10^{2*n2} + {ad_bc} * 10^{n2} + {bd} = {result}")
    return result

# Example usage
num1 = 12345678901234567890
num2 = 98765432109876543210

result = multiply(num1, num2)
print(f"Final Result: {result}") 