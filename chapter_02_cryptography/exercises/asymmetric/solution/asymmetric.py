import sys
from Crypto.Hash import SHA256
from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
import requests
import base64


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: Expected one parameter")
        print("Usage: python3 symmetric.py '<input>'")
        sys.exit(1)
    message = sys.argv[1]

    priv_key = DSA.import_key(open('private_key.pem', "rb").read())
    message_hash = SHA256.new(message.encode())
    signer = DSS.new(priv_key, 'fips-186-3')
    signature = signer.sign(message_hash)

    payload = {
        "message": message,
        "signature": base64.b64encode(signature).decode()
    }
    print(f"Request...\n{payload}\n\n")

    print("Response...")
    response = requests.post("http://localhost:8000/message", json=payload)
    print(response.json())
