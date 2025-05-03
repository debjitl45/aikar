# taxmistri/capital_gains.py
from datetime import datetime

from aikar.exceptions import AikarException


class CapitalGainsCalculator:
    def __init__(self, asset_type, gain_amount, bought_on_date, sold_on_date):
        self.asset_type = asset_type.strip().lower()
        self.gain_amount = gain_amount
        self.holding_period_days = (
                    datetime.strptime(sold_on_date, "%d/%m/%Y").date() - datetime.strptime(bought_on_date,
                                                                                           "%d/%m/%Y").date()).days
        self.validation()
    def validation(self):
        if self.asset_type not in ['equity', 'debt', 'gold', 'gold etf', 'real estate']:
            raise AikarException("Invalid asset type. Please choose from 'equity', 'debt', 'gold', 'gold etf', or 'real estate'.")
        if self.gain_amount < 0:
            raise AikarException("Capital Loss is not taxable.")
        if self.holding_period_days < 0:
            raise AikarException("Holding period cannot be negative.")
    def _is_long_term(self):
        if self.asset_type == 'equity' or self.asset_type == 'gold etf':
            return self.holding_period_days > 365
        elif self.asset_type == 'debt' or self.asset_type == 'gold' or self.asset_type == 'real estate':
            return self.holding_period_days > 730
        else:
            return False

    def calculate(self):
        self.validation()
        is_long_term = self._is_long_term()

        if self.asset_type == 'equity' or self.asset_type == 'gold etf':
            if is_long_term:
                exempt = 125000
                taxable = max(0, self.gain_amount - exempt)
                return {
                        "Asset Type": self.asset_type,
                        "Gain Amount": self.gain_amount,
                        "Exempt Amount": exempt,
                        "Taxable Amount": taxable,
                        "Tax Rate": 0.125,
                        "Tax Payable": taxable * 0.125
                    }
            else:
                return {
                        "Asset Type": self.asset_type,
                        "Gain Amount": self.gain_amount,
                        "Exempt Amount": None,
                        "Taxable Amount": self.gain_amount,
                        "Tax Rate": 0.20,
                        "Tax Payable": self.gain_amount * 0.20
                    }
        else:
            if is_long_term:
                return {
                    "Asset Type": self.asset_type,
                    "Gain Amount": self.gain_amount,
                    "Indexation Benefit": None,
                    "Taxable Amount": self.gain_amount,
                    "Tax Rate": 0.125,
                    "Tax Payable": self.gain_amount * 0.125
                }
            else:
                return {
                    "Asset Type": self.asset_type,
                    "Gain Amount": self.gain_amount,
                    "Indexation Benefit": None,
                    "Taxable Amount": self.gain_amount,
                    "Tax Rate": 0.20,
                    "Tax Payable": self.gain_amount * 0.20
                }
