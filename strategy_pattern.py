
from abc import ABC, abstractmethod
class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, total: float) -> float:
        pass


# Concrete Strategies
class RegularPrice(DiscountStrategy):
    def apply_discount(self, total: float) -> float:
        return total


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent: float):
        self.percent = percent

    def apply_discount(self, total: float) -> float:
        return total - (total * (self.percent / 100))


class FixedCouponDiscount(DiscountStrategy):
    def __init__(self, coupon_value: float):
        self.coupon_value = coupon_value

    def apply_discount(self, total: float) -> float:
        return max(0.0, total - self.coupon_value)

class CheckoutOrder:
    def __init__(self, strategy: DiscountStrategy):
        self.strategy = strategy

    def set_discount_strategy(self, strategy: DiscountStrategy):
        self.strategy = strategy

    def calculate_total(self, bill_amount: float):
        final_bill = self.strategy.apply_discount(bill_amount)
        print(f"Original Bill: ${bill_amount:.2f} -> Final Total: ${final_bill:.2f}")

if __name__ == "__main__":
    bill = 150.0

    order = CheckoutOrder(RegularPrice())
    print("[1. Standard Checkout]")
    order.calculate_total(bill)

    print("\n[2. Black Friday 20% Off]")
    order.set_discount_strategy(PercentageDiscount(percent=20.0))
    order.calculate_total(bill)

    print("\n[3. Applying $30 Coupon]")
    order.set_discount_strategy(FixedCouponDiscount(coupon_value=30.0))
    order.calculate_total(bill)