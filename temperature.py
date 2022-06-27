temperature  = input()
unit = temperature[-1].upper()
value=float(temperature[:-1])
print(value)

if (unit=="C"):
    print(str(round(value,2))+unit)
    print(str(round((value*(9/5)+32),2))+"F")
    print(str(round(value+273,2))+"K")
