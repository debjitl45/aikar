# taxmistri/income_tax.py
from aikar.deduction_validation_and_clubbing import classify_and_sanitize_deductions
from aikar.exceptions import AikarException


class IncomeTaxCalculator:
    def __init__(self, income, age, regime, deductions):
        self.income = income
        self.age = age
        self.regime = regime.lower()
        self.deductions = classify_and_sanitize_deductions(deductions)
        self.validation()

    def validation(self):
        if self.regime not in ['new', 'old']:
            raise AikarException("Invalid regime. Please choose 'new' or 'old'.")
        if self.age < 0 or self.age > 100:
            raise AikarException("Invalid age. Age should be between 0 and 100.")
        if self.income < 0:
            raise AikarException("Income cannot be negative.")
        for key, value in self.deductions.items():
            if not isinstance(key, str):
                raise AikarException(f"Deduction key '{key}' must be a string.")
            if not isinstance(value, (int, float)) or value < 0:
                raise AikarException(f"Deduction value for '{key}' must be a positive number.")

    def _apply_deductions(self):
        self.validation()
        total_deduction = 0
        if self.regime == 'new':
            if "80CCD(2)" in self.deductions.keys():  #new regime considers only 80CCD2/corporate NPS
                total_deduction = self.deductions["80CCD(2)"]
        else:
            total_deduction = sum(self.deductions.values())  #old regime considers all deductions
        return max(0, self.income - total_deduction)

    def _calculate_old_regime_tax(self):
        gross_income = self.income
        taxable_income = self._apply_deductions() - 50000  #standard deduction of 50k
        tax = 0
        slabs = [
            (250000, 0.0),
            (500000, 0.05),
            (1000000, 0.2),
            (float('inf'), 0.3)
        ]
        previous_limit = 0
        for limit, rate in slabs:
            if taxable_income > limit:
                tax += (limit - previous_limit) * rate
                previous_limit = limit
            else:
                tax += (taxable_income - previous_limit) * rate
                break
        cess = tax * 0.04
        total_tax = tax + cess
        return {
            "Gross Income": gross_income,
            "Taxable Income": taxable_income,
            "Base Tax": round(tax),
            "Cess (4%)": round(cess),
            "Total Tax Payable": round(total_tax)
        }

    def _calculate_new_regime_tax(self):
        gross_income = self.income
        taxable_income = self._apply_deductions() - 75000  #std deduction of 75k
        slabs = [
            (400000, 0.00),
            (800000, 0.05),
            (1200000, 0.10),
            (1600000, 0.15),
            (2000000, 0.20),
            (2400000, 0.25),
            (float('inf'), 0.30)
        ]

        tax = 0
        prev_limit = 0
        rebate_flag = False
        rebate = 0

        for limit, rate in slabs:
            if taxable_income > limit:
                tax += (limit - prev_limit) * rate
                prev_limit = limit
            else:
                tax += (taxable_income - prev_limit) * rate
                break
        # Apply rebate if net taxable income is less than or equal to 1200000 and tax is less than or equal to 60000
        if taxable_income <= 1200000 and tax <= 60000:
            tax = 0
            rebate_flag = True

        # Apply marginal relief if net taxable income is between 1200000 and 1275000 which compensates the marginally excess income from the tax-free slab
        if 1200000 < taxable_income <= 1275000 and rebate_flag == False:
            excess_income = taxable_income - 1200000
            if tax > excess_income:
                tax = excess_income

        # Health & Education Cess at 4%
        cess = tax * 0.04
        total_tax = tax + cess

        return {
            "Gross Income": gross_income,
            "Taxable Income": taxable_income,
            "Tax Before Rebate": round(tax),
            "Tax Rebate under 87A": round(rebate) if rebate_flag == True else 0,
            "Tax After Rebate": 0 if rebate_flag == True else round(tax),
            "Cess (4%)": 0 if rebate_flag == True else round(cess),
            "Total Tax Payable": 0 if rebate_flag == True else round(total_tax)
        }

    def calculate(self):
        # New regime now has ₹75,000 standard deduction
        print("Total Deductions: ", self.deductions)
        # Calculate tax based on regime
        if self.regime == 'old':
            gross_tax = self._calculate_old_regime_tax()
        else:
            gross_tax = self._calculate_new_regime_tax()
        return gross_tax
