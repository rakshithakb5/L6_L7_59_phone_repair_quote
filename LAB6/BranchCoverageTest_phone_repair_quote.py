import pytest
from phone_repair_quote import repair_quote, repair_days, trade_in_value


# ---------- repair_quote ----------
def test_budget_screen():
    assert repair_quote("screen", "budget", False, False) == 4600

def test_unknown_part():
    with pytest.raises(ValueError):
        repair_quote("speaker", "budget", False, False)

def test_unknown_tier():
    with pytest.raises(ValueError):
        repair_quote("screen", "premium", False, False)

def test_flagship_camera():
    assert repair_quote("camera", "flagship", False, False) == 5300   # 5000 + 300

def test_warranty_battery_free_part():
    assert repair_quote("battery", "budget", True, False) == 300      # cost 0 + labour 300

def test_express_surcharge():
    assert repair_quote("screen", "budget", False, True) == 5100      # 4600 + 500


# ---------- repair_days ----------
def test_in_stock_quick():
    assert repair_days("battery", True, 2) == 1

def test_no_technicians_in_stock():
    assert repair_days("battery", True, 0) == 3

def test_screen_out_of_stock():
    assert repair_days("screen", False, 2) == 6                       # 1 + 5

def test_battery_out_of_stock():
    assert repair_days("battery", False, 2) == 3                      # 1 + 2


# ---------- trade_in_value ----------
def test_trade_in_new_phone():
    assert trade_in_value(1000, 6, False) == 600

def test_trade_in_mid_age():
    assert trade_in_value(1000, 18, False) == 400

def test_trade_in_old_phone():
    assert trade_in_value(1000, 36, False) == 200

def test_trade_in_cracked_screen():
    assert trade_in_value(1000, 6, True) == 300

def test_trade_in_too_old():
    assert trade_in_value(1000, 60, False) == 0

def test_trade_in_invalid_price():
    with pytest.raises(ValueError):
        trade_in_value(0, 5, False)

# ---------- extra tests for branch coverage ----------
def test_flagship_false_side_budget_battery():
    assert repair_quote("battery", "budget", False, False) == 1800    # 1500 + 300

def test_warranty_on_screen_still_charged():
    assert repair_quote("screen", "budget", True, False) == 4600      # warranty doesn't cover screen

def test_not_warranty_false_side_charging_port():
    assert repair_quote("charging_port", "budget", False, False) == 1100

def test_express_false_flagship_screen():
    assert repair_quote("screen", "flagship", False, False) == 8600   # 8000 + 600

def test_no_technicians_camera_out_of_stock():
    assert repair_days("camera", False, 0) == 8                       # 3 + 5

def test_charging_port_out_of_stock_no_tech():
    assert repair_days("charging_port", False, 0) == 5                # 3 + 2

def test_trade_in_boundary_12_months():
    assert trade_in_value(1000, 12, False) == 600

def test_trade_in_boundary_24_months():
    assert trade_in_value(1000, 24, False) == 400

def test_trade_in_boundary_48_months():
    assert trade_in_value(1000, 48, False) == 200

def test_trade_in_boundary_49_months():
    assert trade_in_value(1000, 49, False) == 0

def test_trade_in_negative_age():
    with pytest.raises(ValueError):
        trade_in_value(1000, -1, False)