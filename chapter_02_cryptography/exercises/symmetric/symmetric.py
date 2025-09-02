import sys
from Crypto.Cipher import Salsa20
import requests
import base64


KEY = b'0123456789012345'


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: Expected one parameter")
        print("Usage: python3 symmetric.py '<input>'")
        sys.exit(1)

    message = sys.argv[1]
    # TODO: encrypt the message
    # TODO: send the encrypted message and the nonce to server
    
    # HINT: bytes are not JSON serializable, 
    # encode to base64 then decode to send as JSON payload.
    payload = {
        "message": "",
        "nonce": ""
    }
    print(f"Request...\n{payload}\n\n")

    print("Response...")
    response = requests.post("http://localhost:8000/message", json=payload)
    print(response.json())
