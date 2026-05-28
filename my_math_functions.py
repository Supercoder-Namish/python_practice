def print_hi(s):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {s}')

def add(x, y, z):       # Adds 3 parameters and returns the sum
    return x + y + z

def multiplication(x, y):
    return x * y

def square(x):
    return x ** 2

def cube(x):
    return x ** 3
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    sum = add(2,5,7)
    print(sum)

    concatenate = add('Hello', 'World', 'Python')
    print(concatenate)

    repeat = multiplication('Hello', 3)
    print(repeat)

    product = multiplication(3,4)
    print(product)

    sum1 = add(sum,product,1)
    print(sum1)

    product1 = multiplication(sum,product)
    print(product1)

    power2 = square(3)
    print(power2)

    power3 = cube(3)
    print(power3)