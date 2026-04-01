def login(username, password):
    if username == "admin" and password == "admin123":
        return "Login successful"
    return "Invalid credentials"