from hypothesis import given, strategies as st
from phone_repair_quote_parser import mask_imei, parse_parts_order, parse_model

@given(st.text() | st.none())
def test_mask_imei_no_crash(s):
    try:
        mask_imei(s)
    except Exception as e:
        assert False, f"mask_imei crashed with: {e!r} for input {s!r}"

@given(st.text() | st.none())
def test_parse_parts_order_no_crash(s):
    try:
        parse_parts_order(s)
    except Exception as e:
        assert False, f"parse_parts_order crashed with: {e!r} for input {s!r}"

@given(st.text() | st.none())
def test_parse_model_no_crash(s):
    try:
        parse_model(s)
    except Exception as e:
        assert False, f"parse_model crashed with: {e!r} for input {s!r}"

# Extra property checks (optional): the output must also be correct, not just crash-free
@given(st.text())
def test_mask_imei_never_reveals_more_than_four(s):
    result = mask_imei(s)
    assert sum(1 for c in result if c != '*') <= 4

@given(st.text())
def test_parse_parts_order_returns_positive_ints(s):
    for part, qty in parse_parts_order(s).items():
        assert part.strip() == part and part != ""
        assert isinstance(qty, int) and qty > 0

@given(st.text())
def test_parse_model_returns_two_strings(s):
    brand, model = parse_model(s)
    assert isinstance(brand, str) and isinstance(model, str)