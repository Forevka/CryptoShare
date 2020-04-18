from dataclasses import dataclass
from decimal import Decimal

@dataclass
class ResultModel:
    site_name: str
    commission: Decimal
    price: Decimal

    def price_comission(self,) -> Decimal:
        return Decimal(self.price - (self.price * (self.commission / 100)))
    
    def price_difference(self,) -> Decimal:
        return Decimal(abs(self.price_comission() - self.price) / self.price) * Decimal(100.0)


if __name__ == "__main__":
    r = ResultModel("test", Decimal(2.5), Decimal(1691))
    print(r.price_comission())