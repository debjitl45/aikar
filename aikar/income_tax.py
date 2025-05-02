# taxmistri/income_tax.py

class IncomeTaxCalculator:
    def __init__(self, income, age=30, regime='new', deductions={}):
        self.income = income
        self.age = age
        self.regime = regime
        self.deductions = deductions

    def _apply_deductions(self, income):
        total_deduction = 0
        if self.regime == 'new':
            if '80CCD2' in self.deductions.keys():  #new regime considers only 80CCD2
                total_deduction = self.deductions['80CCD2']
        else:
            total_deduction = sum(self.deductions.values())  #old regime considers all deductions
        return max(0, self.income - total_deduction)

    def _calculate_old_regime_tax(self, income):
        gross_income = self.income
        taxable_income = self._apply_deductions(gross_income)-50000 #standard deduction of 50k
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

    def _calculate_new_regime_tax(self, income):
        gross_income = self.income
        taxable_income = self._apply_deductions(gross_income) - 75000  #std deduction of 75k
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

        for limit, rate in slabs:
            if taxable_income > limit:
                tax += (limit - prev_limit) * rate
                prev_limit = limit
            else:
                tax += (taxable_income - prev_limit) * rate
                break

        # Apply marginal relief if applicable
        if 1200000 < taxable_income <= 1275000:
            excess_income = taxable_income - 1200000
            if tax > excess_income:
                tax = excess_income

        # Health & Education Cess at 4%
        cess = tax * 0.04
        total_tax = tax + cess

        return {
            "Gross Income": gross_income,
            "Taxable Income": taxable_income,
            "Base Tax": round(tax),
            "Cess (4%)": round(cess),
            "Total Tax Payable": round(total_tax)
        }

    def calculate(self):
        # New regime now has ₹75,000 standard deduction
        if self.regime == 'new':
            taxable_income = max(0, self._apply_deductions(self.income))
        else:
            taxable_income = self._apply_deductions(self.income)

        # Rebate under 87A for income up to ₹7L (new regime)
        if self.regime == 'new' and taxable_income <= 700000:
            return 0

        if self.regime == 'old' and taxable_income <= 500000:
            return 0  # 87A rebate under old regime

        if self.regime == 'old':
            gross_tax = self._calculate_old_regime_tax(taxable_income)
        else:
            gross_tax = self._calculate_new_regime_tax(taxable_income)
        return gross_tax
