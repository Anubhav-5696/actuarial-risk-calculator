from app import calculate_expected_loss, calculate_premium


def test_calculate_expected_loss():
    assert calculate_expected_loss(0.02, 100000) == 2000


def test_calculate_premium():
    expected_loss = 2000
    expense_loading = 0.10
    profit_margin = 0.15

    assert calculate_premium(expected_loss, expense_loading, profit_margin) == 2500