class Salary :

    def __init__(self, x: float) :
        self.monthly = x

    def __str__(self) :
        return f"{self.monthly:,.2f}"
    
    def getM(self):
        return self.monthly

    def annual_salary(self) :
        '''
        Annual Salary
        '''
        x = self.monthly * 12
        return x
    
    def monthly_th(self) :
        '''
        Take Home Pay
        '''
        x = self.monthly * 0.8
        return x
    
    def annual_th(self) :
        x = self.monthly_th() * 12
        return x

    
    def cpf_employer(self) :
        '''
        CPF EMPLOYER 17%
        '''
        x = self.monthly * 0.17
        return x
    
    def cpf_employee(self) :
        '''
        CPF EMPLOYEE 20%'''
        x = self.monthly * 0.2
        return x


user_salary_input = float(input("Enter monthly salary before CPF deduction: "))
user_salary = Salary(user_salary_input)
print(type(user_salary))
print(f">>> You've entered ${user_salary} before CPF deduction.")

print("")
print("---PAY BEFORE DEDUCTION---")

print(f"Monthly Salary before CPF is: ${user_salary}")
annual = user_salary.annual_salary()
print(f"Annual Salary is: ${annual:,.2f}")

print("")
print("--- TAKE HOME PAY---")
monthly_takehome = user_salary.monthly_th()
print(f"Monthly take home pay after CPF deduction is: ${monthly_takehome:,.2f}")
annual_takehome = user_salary.annual_th()
print(f"Annual take home pay after CPF deduction is: ${annual_takehome:,.2f}")

print("")
print("---CPF CONTRIBUTION---")
employer_contribution = user_salary.cpf_employer()
print(f"Employer contribution per month is: ${employer_contribution:,.2f}")
employee_contribution = user_salary.cpf_employee()
print(f"Employee CPF contribution is: ${employee_contribution:,.2f}")

# ASK FOR BONUS INPUT
print("")
bonus_received = float(input("Enter bonus amount (0 to exit): "))
if bonus_received == 0 :
    exit()

print("")
print("---BONUS CALCULATION---")
bonus_months = (bonus_received / annual) * 12
print(f"Your bonus amount in months is: {bonus_months:.2f}")
bonus_months_percentage = (bonus_received / annual) * 100
print(f"Your bonus amount in % is: {bonus_months_percentage:.2f}%")

# ASK FOR INCREMENT INPUT
print("")
increment_received = float(input("Enter increment amount (0 to exit): "))
if increment_received == 0 :
    exit()

print("")
print("---INCREMENT CALCULATION---")
increment_months_percentage = (increment_received / user_salary.getM()) * 100
print(f"Your bonus amount in % is: {increment_months_percentage:.2f}%")

print('')

