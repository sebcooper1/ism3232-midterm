# Constants
LONG_RENTAL_DAYS = 7
SHORT_RENTAL_DAYS = 3

NO_DISCOUNT = 0.0
STANDARD_DISCOUNT = 0.10
LONG_DISCOUNT = 0.20

DAMAGE_WAIVER_LIMIT = 150.00
DAMAGE_WAIVER_FEE = 25.00

REQUIRE_DEPOSIT_THRESHOLD = 1000.00

NEED_INSPECTION_THRESHOLD = 800.00
INSPECTION_DAYS = 5


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


def calculate_quote(daily_rate: float, days: int, contractor: bool = False) -> float:
   """Calculates the final quote after applying any applicable discounts."""
   original_cost = calculate_rental_cost(daily_rate, days)
   discount = get_rental_discount(days, contractor)
   discounted_cost = original_cost * (1 - discount)
   if discounted_cost < DAMAGE_WAIVER_LIMIT:
         discounted_cost += DAMAGE_WAIVER_FEE  # Add damage waiver fee if below limit
   return discounted_cost

def requires_deposit(quote: float) -> bool:
    """Determines if a deposit is required based on the quote amount."""
    return quote >= REQUIRE_DEPOSIT_THRESHOLD

def needs_inspection(days: int, quote: float) -> bool:
    """Determines if an inspection is required based on the rental days and quote amount."""
    return days >= INSPECTION_DAYS and quote > NEED_INSPECTION_THRESHOLD

def total_quoted(rentals: list) -> float:
    """Calculates the total quoted amount for a list of rentals."""
    total = 0
    
    for rental in rentals:
        quote = calculate_quote(rental['daily_rate'], rental['days'], rental['contractor'])
        total += quote
    
    return total

def largest_rental(rentals: list) -> str:
    """Finds the customer with the largest rental quote."""
    largest_quote = 0.0
    largest_customer = ""   

    for rental in rentals:
        quote = calculate_quote(rental['daily_rate'], rental['days'], rental['contractor'])
        if quote > largest_quote:
            largest_quote = quote
            largest_customer = rental['customer']
    
    return largest_customer


def format_rental_line(customer: str, quote: float, deposit: bool, inspection: bool) -> str:
    """Returns one line of formatted rental information for display."""
    if deposit:
        deposit_str = "yes"
    else:
        deposit_str = "no"  

    if inspection:
        inspection_str = "yes"
    else:
        inspection_str = "no"

    return f"{customer}: ${quote:.2f} | deposit: {deposit_str} | inspection: {inspection_str}"
    

