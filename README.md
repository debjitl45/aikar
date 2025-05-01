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
calc = IncomeTaxCalculator(
    income=1400000,
    age=29,
    regime='new',
    deductions={'80C': 0, 'HRA': 0, '80CCD2': 100000, 'Home Loan': 0}
)
