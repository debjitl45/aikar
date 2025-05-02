from aikar import IncomeTaxCalculator

from aikar import CapitalGainsCalculator

capital_gains_tax = CapitalGainsCalculator('gold', 125000, '3/1/2023', '3/2/2029')

print(capital_gains_tax.calculate())


income_tax = IncomeTaxCalculator(
    income=1200000,
    age=29,
    regime='old',
    deductions={'80C': 150000, 'HRA': 180000, '80CCD2': 0, 'Home Loan': 0}
)

print(income_tax.calculate())
