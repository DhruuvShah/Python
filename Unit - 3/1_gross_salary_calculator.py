"""Calculate an employee's gross salary using HRA and DA salary slabs."""

basic = float(input("Enter basic salary: "))

if basic <= 10000:
    hra_rate = 0.20
    da_rate = 0.80
elif basic <= 20000:
    hra_rate = 0.25
    da_rate = 0.90
else:
    hra_rate = 0.30
    da_rate = 0.95

hra = basic * hra_rate
da = basic * da_rate
gross = basic + hra + da

print("Basic Salary:",basic)
print("HRA:",hra)
print("DA",da)
print("Gross Salary", gross)
