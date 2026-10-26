# Employee Module – Gross and Net Salary 

import employee

basic = float(input("Enter basic salary: ")) 
da = employee.DA(basic) 
hra = employee.HRA(basic) 
gross = basic + da + hra 
pf = employee.PF(basic) 
itax = employee.ITAX(gross) 
net = gross - pf - itax 

print("DA =", da) 
print("HRA =", hra) 
print("Gross Salary =", gross) 
print("PF =", pf) 
print("Income Tax =", itax) 
print("Net Salary =", net) 
