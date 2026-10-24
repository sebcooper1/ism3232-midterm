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


def test_calculate_quote_as_149():
    assert round(calculate_quote(149.99, 1, False), 2) == 174.99


def test_calculate_quote_as_150():
    assert round(calculate_quote(150.00, 1, False), 2) == 150.00


def test_calculate_rental_cost_at_70():
    assert round(calculate_rental_cost(70.00, 2), 2) == 140.00


def test_calculate_rental_cost_at_60():
    assert round(calculate_rental_cost(60.00, 2), 2) == 120.00


def test_calculate_rental_cost_at_85():
    assert round(calculate_rental_cost(85.00, 4), 2) == 340.00


def test_get_rental_discount_as_false1():
    assert get_rental_discount(2, False) == 0.00


def test_get_rental_discount_as_false7():
    assert get_rental_discount(7, False) == 0.20


def test_get_rental_discount_as_false3():
    assert get_rental_discount(3, False) == 0.10


def test_get_rental_discount_as_false6():
    assert get_rental_discount(6, False) == 0.10


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
    assert needs_inspection(4, 900.00) is False


def test_needs_inspection_as_true():
    assert needs_inspection(5, 900.00) is True


def test_needs_inspection_under_boundary():
    assert needs_inspection(5, 800.00) is False


def test_needs_inspection_over_boundary():
    assert needs_inspection(5, 800.01) is True


def test_requires_deposit_as_false():
    assert requires_deposit(120.00) is False


def test_requires_deposit_below_threshold():
    assert requires_deposit(999.99) is False


def test_requires_deposit_at_threshold():
    assert requires_deposit(1000.00) is True


def test_total_quoted():
    rentals = [
        {"customer": "Alvarez", "daily_rate": 60.00, "days": 2, "contractor": False},
        {"customer": "Brennan", "daily_rate": 60.00, "days": 2, "contractor": True},
        {"customer": "Chowdhury", "daily_rate": 85.00, "days": 4, "contractor": False},
    ]
    assert round(total_quoted(rentals), 2) == 584.00


def test_largest_rental_empty_list():
    assert largest_rental([]) == ""


def test_largest_rental_tie():
    rentals = [
        {"customer": "Alvarez", "daily_rate": 100.00, "days": 4, "contractor": False},
        {"customer": "Brennan", "daily_rate": 100.00, "days": 4, "contractor": False},
    ]
    assert largest_rental(rentals) == "Alvarez"
