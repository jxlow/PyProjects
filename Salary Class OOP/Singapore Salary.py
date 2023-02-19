class salary :

    def __init__(self) :
        self.monthly = "monthly"
    

    def annual_salary(monthly) :
        '''
        Annual Salary
        '''
        x = float(monthly) * 12
        return x
    
    def monthly_th(monthly) :
        '''
        Take Home Pay
        '''
        x = float(monthly) * 0.8
        return x
    
    def annual_th(monthly) :
        x = salary.monthly_th(monthly) * 12
        return x
    
    def cpf_employer(monthly) :
        '''
        CPF EMPLOYER 17%
        '''
        x = float(monthly) * 0.17
        return x
    
    def cpf_employee(monthly) :
        '''
        CPF EMPLOYEE 20%'''
        x = float(monthly) * 0.2
        return x

monthly_salary = float(input("Enter monthly salary before CPF: "))

print("")
print("---PAY BEFORE DEDUCTION---")

print(f"Monthly Salary before CPF is: ${monthly_salary:,.2f}")
annual = salary.annual_salary(monthly_salary)
print(f"Annual Salary is: ${annual:,.2f}")

print("")
print("--- TAKE HOME PAY---")
monthly_takehome = salary.monthly_th(monthly_salary)
print(f"Monthly take home pay after CPF deduction is: ${monthly_takehome:,.2f}")
annual_takehome = salary.annual_th(monthly_salary)
print(f"Annual take home pay after CPF deduction is: ${annual_takehome:,.2f}")

print("")
print("--- CPF CONTRIBUTION---")
employer_contribution = salary.cpf_employer(monthly_salary)
print(f"Employer contribution per month is: ${employer_contribution:,.2f}")
employee_contribution = salary.cpf_employee(monthly_salary)
print(f"Employee CPF contribution is: ${employee_contribution:,.2f}")