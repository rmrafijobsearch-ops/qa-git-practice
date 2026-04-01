from app import login

def test_valid_login():
    assert login("admin", "admin123") == "Login successful"

def test_invalid_login():
    assert login("wrong", "wrong") == "Invalid credentials"

def test_empty_login():
    assert login("", "") == "Invalid credentials"