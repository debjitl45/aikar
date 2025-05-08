from aikar import IncomeTaxCalculator

from aikar import CapitalGainsCalculator

user_input_example = {
    "PPF": 50000,
    "LIC": 30000,
    "elss": 100000,
    "employer nps": 80000,
    "80CCD(1B)": 60000,
    "medical insurance": 40000,
    "80D parents": 60000,
    "donation": 20000
}

try:
    capital_gains_tax = CapitalGainsCalculator('equity', 125010, '3/1/2023', '3/2/2029')
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
    income_tax = IncomeTaxCalculator(income=1279000, age=30,
                                     deductions={"PPF": 50000, "LIC": 5000, "elss": 30000, "tax saving fd": 5000,
                                                 "beauty rebate": 5000,
                                                 "80D": 500000, "corporate nps": 50000, "tuition fees": 50000},
                                     regime="old")
    print(income_tax.calculate())
except Exception as e:
    print("Validation failed:", e)
