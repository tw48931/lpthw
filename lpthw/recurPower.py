def recurPower(base, exp):
    if exp == 0:
        return 1
    elif exp > 0:
        return base * recurPower(base, exp - 1)
    else:
        raise ValueError("exp should >0")
      
x = int(input("Please enter base:"))
y = int(input("Please enter exp:"))
print(recurPower(x, y))
