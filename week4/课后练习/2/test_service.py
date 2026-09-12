from service import calculate

def test_add_case():
    assert calculate(1, 2, "add") == 3

def test_sub_case():
    assert calculate(10, 2, "sub") == 8

def test_mul_case():
    assert calculate(3, 4, "mul") == 12

def test_unknown_op_returns_none():
    assert calculate(1, 2, "div") is None

def test_unknown_op_empty_string():
    assert calculate(5, 5, "") is None
