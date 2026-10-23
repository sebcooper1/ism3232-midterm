from business_rules import (
    calculate_quote,
    calculate_rental_cost,
    format_rental_line,
    get_rental_discount,
    largest_rental,
    needs_inspection,
    requires_deposit,
    total_quoted,
)


def test_calculate_quote_as_false():
    assert calculate_quote(60.00, 2, False) == 145.00


def test_calculate_quote_as_true():
    assert calculate_quote(60.00, 2, True) == 133.00


def test_calculate_rental_cost_at_70():
    assert calculate_rental_cost(70.00, 2) == 140.00


def test_calculate_rental_cost_at_60():
    assert calculate_rental_cost(60.00, 2) == 120.00


def test_calculate_rental_cost_at_85():
    assert calculate_rental_cost(85.00, 4) == 340.00


def test_get_rental_discount_as_false1():
    assert get_rental_discount(1, False) == 0.00


def test_get_rental_discount_as_true2():
    assert get_rental_discount(2, True) == 0.10


def test_get_rental_discount_as_false8():
    assert get_rental_discount(8, False) == 0.20


def test_get_rental_discount_as_true6():
    assert get_rental_discount(6, True) == 0.10


def test_format_rental_line_Alvarez():
    assert (
        format_rental_line("Alvarez", 120.00, False, False)
        == "Alvarez: $120.00 | deposit: no | inspection: no"
    )


def test_format_rental_line_Brennan():
    assert (
        format_rental_line("Brennan", 120.00, True, False)
        == "Brennan: $120.00 | deposit: yes | inspection: no"
    )


def test_format_rental_line_Chowdhury():
    assert (
        format_rental_line("Chowdhury", 340.00, False, True)
        == "Chowdhury: $340.00 | deposit: no | inspection: yes"
    )


def test_largest_rental():
    rentals = [
        {"customer": "Alvarez", "daily_rate": 60.00, "days": 2, "contractor": False},
        {"customer": "Brennan", "daily_rate": 60.00, "days": 2, "contractor": True},
        {"customer": "Chowdhury", "daily_rate": 85.00, "days": 4, "contractor": False},
    ]
    assert largest_rental(rentals) == "Chowdhury"


def test_needs_inspection_as_false():
    assert needs_inspection(2, 120.00) == False


def test_needs_inspection_as_true():
    assert needs_inspection(15, 900.00) == True


def test_requires_deposit_as_false():
    assert requires_deposit(120.00) == False


def test_requires_deposit_below_threshold():
    assert requires_deposit(999.99) == False


def test_requires_deposit_at_threshold():
    assert requires_deposit(1000.00) == True


def test_total_quoted():
    rentals = [
        {"customer": "Alvarez", "daily_rate": 60.00, "days": 2, "contractor": False},
        {"customer": "Brennan", "daily_rate": 60.00, "days": 2, "contractor": True},
        {"customer": "Chowdhury", "daily_rate": 85.00, "days": 4, "contractor": False},
    ]
    assert total_quoted(rentals) == 584.00


def test_largest_rental_empty_list():
    assert largest_rental([]) == ""
