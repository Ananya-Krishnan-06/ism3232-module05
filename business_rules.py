# business_rules.py
# Author: Ananya Krishnan

SPENDING_LIMIT = 1000


def calculate_total(price: float, quantity: int) -> float:
    """Return total club expense including 7% tax."""
    return price * quantity * 1.07


def requires_review(amount: float) -> bool:
    """Return True if club expense exceeds the spending limit."""
    return amount > SPENDING_LIMIT


def get_approval_tier(amount: float) -> str:
    """Return the student council approval routing tier."""
    if amount <= 500:
        return "auto"
    elif amount <= 2000:
        return "treasurer"
    else:
        return "advisor"


def apply_discount(price: float, pct: float) -> float:
    """Return price after club discount. pct is 0-100."""
    return price * (1 - pct / 100)
