# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(s):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {s}')  # Press Ctrl+F8 to toggle the breakpoint.

def add(x, y, z):
    return x + y + z

def multiplication(x, y):
    return x * y

def square(x):
    return x ** 2

def cube(x):
    return x ** 3
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    sum = add(2,5,7)
    print(sum)

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



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
