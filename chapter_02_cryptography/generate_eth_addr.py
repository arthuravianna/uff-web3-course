from ecdsa import SigningKey, SECP256k1
from Crypto.Hash import keccak

# Generate private key
private_key = SigningKey.generate(curve=SECP256k1)
public_key = private_key.get_verifying_key()

# Raw bytes (64 bytes: X || Y)
public_key_bytes = public_key.to_string()

# Compute Keccak-256 hash
keccak256 = keccak.new(digest_bits=256)
keccak256.update(public_key_bytes)
public_key_hash = keccak256.digest()

# Ethereum address = last 20 bytes of the hash
address = "0x" + public_key_hash[-20:].hex()

print("Private Key:", private_key.to_string().hex())
print("Public Key:", public_key_bytes.hex())
print("Ethereum Address:", address)
