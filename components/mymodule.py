import re

# Validez les données saisies

def validate_username(username):
    return len(username) >= 3 and not re.search(r"[@#$%^&*()<>/|}{~:]", username)

def validate_email(email):
    return re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-z]{2,}$", email)

def validate_password_length(password):
    return len(password) >= 8

def validate_password(password):
    return validate_password_length(password) and re.search(r"[a-z]", password) and re.search(r"[A-Z]", password) and re.search(r"\d", password) and re.search(r"[@#$%^&*()<>/|}{~:]", password)