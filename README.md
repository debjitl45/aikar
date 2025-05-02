# TaxMistri

TaxMistri simplifies Indian Tax calculations using Python.

## Features

- Calculation of Income Tax (Old and New Regimes)
- Calculation of Capital Gains Tax (Equity, Debt, Gold)

## Installation

```bash
pip install taxmistri
```
## Usage
```python
#import the library 
from taxmistri import IncomeTaxCalculator
#enter your income,age,regime and deductions under 80C,80CCD2,HRA,Interest paid for Home Loan
income_tax = IncomeTaxCalculator(
    income=1400000,
    age=29,
    regime='new',
    deductions={'80C': 0, 'HRA': 0, '80CCD2': 100000, 'Home Loan': 0}
)
#enter your asset type, profits, buy & sell date for whatever investments you have done eg:- equity, gold, gold etfs, debt, real estate
capital_gains_tax = CapitalGainsCalculator('gold', 125000, '3/1/2023', '3/2/2029')

