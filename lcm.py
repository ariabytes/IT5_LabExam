# LCM
print("\nThis is an LCM Calculator that uses GCD")

def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b % a, a)

def lcm(a, b):
    if a <= 0:
        print("Value is not accepted!")
    else:
        return a * b // gcd(a, b)


# Main
while True:
    x = int(input("\nEnter a value for x: "))
    y = int(input("Enter a value for y: "))
    print(f"\nThe LCM of {x} and {y} is {lcm(x,y)}.")

