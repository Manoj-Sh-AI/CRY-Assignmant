import bcrypt
import random

# Generate a random salt
def generate_salt():
    return bcrypt.gensalt(10).decode()

# Generate a hashed password using bcrypt
def generate_hashed_password(password, salt):
    hashed_password = bcrypt.hashpw(password.encode(), salt.encode())
    return hashed_password.decode()

# Verify a password against a hashed password using bcrypt
def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode(), hashed_password.encode())

# Generate a password file with 10 passwords
def generate_password_file():
    passwords = []
    for i in range(10):
        password = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(8))
        passwords.append(password)

    with open('passwords.txt', 'w') as file:
        file.write('\n'.join(passwords))

# Store the hashed values of passwords in a file
def store_hashed_passwords():
    with open('passwords.txt', 'r') as file:
        passwords = file.read().split('\n')
    
    hashed_passwords = []
    for password in passwords:
        salt = generate_salt()
        hashed_password = generate_hashed_password(password, salt)
        hashed_passwords.append(hashed_password)
    
    with open('hashed_passwords.txt', 'w') as file:
        file.write('\n'.join(hashed_passwords))

# Generate a salt file
def generate_salt_file():
    salts = []
    for _ in range(10):
        salt = generate_salt()
        salts.append(salt)
    
    with open('salts.txt', 'w') as file:
        file.write('\n'.join(salts))

# Store salted and hashed passwords in a file
def store_salted_hashed_passwords():
    with open('passwords.txt', 'r') as file:
        passwords = file.read().split('\n')

    with open('salts.txt', 'r') as file:
        salts = file.read().split('\n')

    salted_hashed_passwords = []
    for password, salt in zip(passwords, salts):
        salted_password = password + salt
        hashed_password = generate_hashed_password(salted_password, salt)
        salted_hashed_passwords.append(hashed_password)

    with open('salted_hashed_passwords.txt', 'w') as file:
        file.write('\n'.join(salted_hashed_passwords))

# Verify a password against the hashed passwords in the file
def verify_password_from_file(password):
    with open('hashed_passwords.txt', 'r') as file:
        hashed_passwords = file.read().split('\n')

    for hashed_password in hashed_passwords:
        if verify_password(password, hashed_password):
            return True
    
    return False

# Verify a password against the salted and hashed passwords in the file
def verify_salted_hashed_password_from_file(password):
    with open('salted_hashed_passwords.txt', 'r') as file:
        salted_hashed_passwords = file.read().split('\n')

    with open('salts.txt', 'r') as file:
        salts = file.read().split('\n')

    for salted_hashed_password, salt in zip(salted_hashed_passwords, salts):
        salted_password = password + salt
        hashed_password = generate_hashed_password(salted_password, salt)
        if verify_password(salted_password, salted_hashed_password):
            return True
    
    return False

# Task 4a: Generate a password file of 10 passwords
generate_password_file()

# Task 4b: Store the hashed values of passwords in a file
store_hashed_passwords()

# Task 4c: Generate a salt file and store salted and hashed passwords in a file
generate_salt_file()
store_salted_hashed_passwords()

password_to_verify = 'password123'
is_password_valid = verify_password_from_file(password_to_verify)
print('Is password valid (hashed passwords):', is_password_valid)

# Verify a password against the salted and hashed passwords in the file
is_salted_hashed_password_valid = verify_salted_hashed_password_from_file(password_to_verify)
print('Is password valid (salted and hashed passwords):', is_salted_hashed_password_valid)
