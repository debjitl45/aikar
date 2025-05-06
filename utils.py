from aikar import IncomeTaxCalculator

from aikar import CapitalGainsCalculator

try:
    capital_gains_tax = CapitalGainsCalculator('equity mutual fund', 125000, '3/1/2023', '3/2/2029')
    print(capital_gains_tax.calculate())
except Exception as e:
    print("Validation failed:", e)


# income_tax = IncomeTaxCalculator(
#     income=1200000,
#     age=29,
#     regime='oldnew',
#     deductions={'80C': 150000, 'HRA': 180000, '80CCD2': 0, 'Home Loan': 0}
# )

try:
    income_tax = IncomeTaxCalculator(income=1275001, age=30, deductions={"80CCD2": 0}, regime="new")
    print(income_tax.calculate())
except Exception as e:
    print("Validation failed:", e)

