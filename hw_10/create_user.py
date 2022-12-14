from faker import Faker

fake = Faker()


def create_user(name: str, password: str):
    if len(name) > 0 and len(password) > 0:
        return "New user created"
    elif len(name) < 1 and len(password) > 0:
        return f"{fake.name()} - fake name, {password} - your password"
    elif len(name) > 0 and len(password) < 1:
        return f"{name} - your name, {fake.password()} - fake password"
    elif len(name) < 1 and len(password) < 1:
        return f"{fake.name()} - fake name, {fake.password()} - fake password"
