import sys
from Crypto.Hash import SHA256
from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
import requests
import base64


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: Expected one parameter")
        print("Usage: python3 ds.py '<input>'")
        sys.exit(1)
    message = sys.argv[1]

    priv_key = ECC.import_key(open('private_key.pem', "rb").read())
    # TODO: calculate the message hash
    # TODO: sign the message hash using the private key
    # TODO: Send the signature with the message to server

    payload = {
        "message": message,
        "signature": ""
    }
    print(f"Request...\n{payload}\n\n")

    print("Response...")
    response = requests.post("http://localhost:8000/message", json=payload)
    print(response.json())
