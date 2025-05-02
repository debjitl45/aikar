from aikar import IncomeTaxCalculator

from aikar import CapitalGainsCalculator

capital_gains_tax = CapitalGainsCalculator('gold', 125000, '3/1/2023', '3/2/2029')

print(capital_gains_tax.calculate())


income_tax = IncomeTaxCalculator(
    income=1400000,
    age=29,
    regime='new',
    deductions={'80C': 0, 'HRA': 0, '80CCD2': 100000, 'Home Loan': 0}
)

print(income_tax.calculate())
