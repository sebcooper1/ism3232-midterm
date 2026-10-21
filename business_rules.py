# Constants
LONG_RENTAL_DAYS = 7
SHORT_RENTAL_DAYS = 3
MID_RENTAL_DAYS = 6
NO_DISCOUNT = 0.0
STANDARD_DISCOUNT = 0.10
LONG_DISCOUNT = 0.20




def calculate_rental_cost(daily_rate: float, days: int) -> float:
    """Calculates the total rental cost based on the daily rate and number of days."""
    return daily_rate * days 


def get_rental_discount(days: int, contractor: bool = False) -> float:
    """Calculate the discount based on rental days and contractor status."""
    
    if days >= LONG_RENTAL_DAYS:
        return 0.2

    elif days >= SHORT_RENTAL_DAYS or contractor:
        return 0.1

    else:
        return 0.0


calculate_quote(daily_rate: float, days: int, contractor: bool = False) -> float:
   

requires_deposit(quote: float) -> bool

needs_inspection(days: int, quote: float) -> bool

total_quoted(rentals: list) -> float

largest_rental(rentals: list) -> str

format_rental_line(customer: str, quote: float, deposit: bool, inspection: bool) -> str

