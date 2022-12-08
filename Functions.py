def privet_func(name):
    """Print Privetstvie"""
    print("Hello. \n  _________ \n All best \n _________ \n  With Love" + " to " + name )
def summa(x, z):
     return x + z

def factorial(o):
    """Calculate Factorial of o"""
    otvet = 1
    for i in range (1, o + 1):
        otvet = otvet * i
    return otvet

for i in range(1, 10):
    print(str(i) + "!\t = " + str(factorial(i)))
