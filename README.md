# Aikar

"Aikar" the name is derived from hindi word "आयकर" which translates to income tax.
Aikar is a Python library provides functions helps in Tax calculations using Python. 

### Income Tax Slabs for FY 2024-25 (AY 2025-26)

#### 🔹 New Regime (Post Budget 2025)

| Income Range                  | Tax Rate  |
|------------------------------|-----------|
| Up to ₹4,00,000              | Nil       |
| ₹4,00,001 – ₹8,00,000        | 5%        |
| ₹8,00,001 – ₹12,00,000       | 10%       |
| ₹12,00,001 – ₹16,00,000      | 15%       |
| ₹16,00,001 – ₹20,00,000      | 20%       |
| Above ₹20,00,000             | 30%       |

>  **Standard deduction of ₹50,000** available  
>  **No exemptions/deductions** (except NPS 80CCD(2), EPF, etc.)  
>  **Marginal relief** applies beyond ₹12.75L

---

#### 🔹 Old Regime

| Income Range                  | Tax Rate  |
|------------------------------|-----------|
| Up to ₹2,50,000              | Nil       |
| ₹2,50,001 – ₹5,00,000        | 5%        |
| ₹5,00,001 – ₹10,00,000       | 20%       |
| Above ₹10,00,000             | 30%       |

> Multiple deductions allowed (80C, 80D, HRA, LTA, etc.)  
> **Rebate under 87A** for income up to ₹5L  
> **Surcharge & marginal relief** applies beyond ₹50L


## Features

- Calculation of Income Tax (Old and New Regimes)
- Calculation of Capital Gains Tax (Equity, Debt, Gold)

## Installation

```bash
pip install aikar
```
## Usage
```python
#import the library 
from aikar import IncomeTaxCalculator
#enter your income,age,regime and deductions under 80C,80CCD2,HRA,Interest paid for Home Loan
income_tax = IncomeTaxCalculator(
    income=1400000,
    age=29,
    regime='new',
    deductions={'80C': 0, 'HRA': 0, '80CCD2': 100000, 'Home Loan': 0}
)
#enter your asset type, profits, buy & sell date for whatever investments you have done eg:- equity, gold, gold etfs, debt, real estate
capital_gains_tax = CapitalGainsCalculator('gold', 125000, '3/1/2023', '3/2/2029')

