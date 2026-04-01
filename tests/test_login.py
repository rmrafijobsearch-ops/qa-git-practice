from app import login

def test_valid_login():
    assert login("admin", "admin123") == "Login successful"

def test_invalid_login():
    assert login("wrong", "wrong") == "Invalid credentials"

def test_empty_login():
    assert login("", "") == "Invalid credentials"
def login(username, password):
    if not username or not password:
        return "Invalid credentials"
    if username == "admin" and password == "admin123":
        return "Login successful"
    return "Invalid credentials"