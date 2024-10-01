import base64
import hashlib

def encode_payload(payload, salt_key, salt_index):
    salted_payload = salt_key[:salt_index] + payload + salt_key[salt_index:]
    encoded = base64.b64encode(salted_payload.encode()).decode()
    return encoded

def decode_payload(encoded_payload, salt_key, salt_index):
    decoded = base64.b64decode(encoded_payload.encode()).decode()
    expected_salt = salt_key[:salt_index] + salt_key[salt_index:]
    if decoded.startswith(expected_salt[:salt_index]) and decoded.endswith(expected_salt[salt_index:]):
        return decoded[len(salt_key[:salt_index]):-len(salt_key[salt_index:])]
    return None

# Example usage
payload = "example_payload"
salt_key = "somesaltkey"
salt_index = 5

encoded = encode_payload(payload, salt_key, salt_index)
print("Encoded:", encoded)

decoded = decode_payload(encoded, salt_key, salt_index)
print("Decoded:", decoded)
