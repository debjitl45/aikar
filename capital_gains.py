# taxmistri/capital_gains.py

class CapitalGainsCalculator:
    def __init__(self, asset_type, gain_amount, holding_period_days):
        self.asset_type = asset_type.lower()
        self.gain_amount = gain_amount
        self.holding_period_days = holding_period_days

    def _is_long_term(self):
        if self.asset_type == 'equity':
            return self.holding_period_days > 365
        elif self.asset_type == 'debt' or self.asset_type == 'gold':
            return self.holding_period_days > 1095
        else:
            return False

    def calculate(self):
        is_long_term = self._is_long_term()

        if self.asset_type == 'equity':
            if is_long_term:
                exempt = 100000
                taxable = max(0, self.gain_amount - exempt)
                return taxable * 0.10
            else:
                return self.gain_amount * 0.15
        else:
            if is_long_term:
                return self.gain_amount * 0.20
            else:
                return self.gain_amount * 0.30
