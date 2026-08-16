def register(username, password):
    print("Registering user:", username)
    return {"username": username, "password": password}


def validate_email(email):
    return "@" in email and "." in email
