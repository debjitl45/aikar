from taxmistri import IncomeTaxCalculator

from taxmistri import CapitalGainsCalculator

calc = CapitalGainsCalculator('gold', 125000, '3/1/2023', '3/2/2029')

print(calc.calculate())


calc = IncomeTaxCalculator(
    income=1400000,
    age=29,
    regime='new',
    deductions={'80C': 0, 'HRA': 0, '80CCD2': 100000, 'Home Loan': 0}
)

print(calc.calculate())
