import hashlib
import secrets

rest_token = secrets.token_hex(20)
hash_value = hashlib.sha256(rest_token.encode()).hexdigest()

print(hash_value)

verification_token = hashlib.sha256(rest_token.encode()).hexdigest()

print(verification_token)

if verification_token != hash_value:
    print('Token is not valid')
else:
    print('Token is valid')

hash_value2 = hash_value.replace(hash_value[0], '1')

print(hash_value2)

verification_token2 = hashlib.sha256(rest_token.encode()).hexdigest()

print(verification_token2)

if verification_token2 != hash_value2:
    print('Token is not valid')
else:
    print('Token is valid')