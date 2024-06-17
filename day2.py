allowance={"HRA" : 0.4, "IA":0.30, "TA":0.15}
deduction={"PF":0.12,"Insurance":5000}

print("-"*25,"Salary calculator: ","-"*25)
basic= int(input("Enter the basic salary"))

def calculator_allowance(basic):
    total_allowance=0
    for i in allowance:
        total_allowance+=allowance[i]*basic
    return total_allowance

def calculator_deduction(basic):
    total_deduction=0
    for i in deduction:
        if type(deduction[i]) is not int:
            total_deduction+=deduction[i]*basic
        else:
            total_deductions+=deductions[i]
        return total_deduction
    
def professional_tax(sal):
    prof_tax=0
    if sal>=8500 and sal<=10000:
        prof_tax=200
    elif sal>10000 and sal<=30000:
        prof_tax=300
    elif sal>30000:
        prof_tax=500
    return prof_tax

def calculatesalary():
    gsalary=basic+calculator_allowance(basic)
    ptax=professional_tax(gsalary)
    nsalary=gsalary-ptax-calculator_deduction(basic)
    print("basic salary",basic)
    print("Allowance", calculator_allowance(basic))
    print("Deduction", calculator_deduction(basic))
    print("Professional Tax", ptax)
    print("Gross salary", gsalary)
    print("Net salary",nsalary)

calculatesalary()
    
    



























    
    
    
