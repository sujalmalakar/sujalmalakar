mass1 = float(input("Enter the mass in talents :"))
mass2 = float(input("Enter the mass in pounds :"))
mass3 = float(input("Enter the mass in lots :"))

w = (mass1 * 20 * 32 * 13.3) + (mass2 * 32 * 13.3) + (mass3 * 13.3)
print(w)

w2 = w/1000
print(w2)