def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

x = int(input("First Number: "))
y = int(input("Second Number: "))

if x <= 0 or y <= 0:
    print("Value must be positibo. ")

else:
    print(f"The LCM of {x} and {y} is = {lcm(x, y)}")