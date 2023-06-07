a = 17
b = 20

def encrypt_message(msg):
    cipher = ""
    for char in msg:
        if char != ' ':
            cipher += chr((((a * (ord(char) - 65)) + b) % 26) + 65)
        else:
            cipher += char
    return cipher

def decrypt_cipher(cipher):
    msg = ""
    a_inv = 0
    flag = 0

    for i in range(26):
        flag = (a * i) % 26

        if flag == 1:
            a_inv = i

    for char in cipher:
        if char != ' ':
            msg += chr(((a_inv * ((ord(char) - 65 - b)) % 26)) + 65)
        else:
            msg += char

    return msg

msg = "AFFINE CIPHER"

print("message:", msg)

cipher_text = encrypt_message(msg)
print("Encrypted Message is:", cipher_text)

print("Decrypted Message is:", decrypt_cipher(cipher_text))