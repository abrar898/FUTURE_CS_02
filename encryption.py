from Crypto.Cipher import AES
import os

# AES requires 16, 24, or 32 byte keys (128, 192, 256-bit)
key = b'ThisIsASecretKey'  # 16-byte static key (use env in production)

def pad(data):
    # Pad with spaces to make data a multiple of 16 bytes
    return data + b' ' * (16 - len(data) % 16)

def unpad(data):
    return data.rstrip(b' ')

def encrypt_file(input_path, output_path):
    cipher = AES.new(key, AES.MODE_ECB)
    with open(input_path, 'rb') as f:
        data = f.read()
    padded_data = pad(data)
    encrypted_data = cipher.encrypt(padded_data)
    with open(output_path, 'wb') as f:
        f.write(encrypted_data)

def decrypt_file(input_path, output_path):
    cipher = AES.new(key, AES.MODE_ECB)
    with open(input_path, 'rb') as f:
        encrypted_data = f.read()
    decrypted_data = unpad(cipher.decrypt(encrypted_data))
    with open(output_path, 'wb') as f:
        f.write(decrypted_data)
