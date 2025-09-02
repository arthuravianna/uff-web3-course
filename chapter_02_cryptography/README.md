# Cryptography

Lorem Ipsum

To run the examples and do the practical exercises in this chapter, you will need to install two Python packages. We advise using a virtual environment as follows:

``` shell
cd chapter_02_cryptography/
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

## Symmetric Cryptography - Cipher


## Asymmetric Cryptography - Digital Signature

## Cryptography and Blockchain

## Practical Exercises
This section presents practical exercises that complement the reading.

### Symmetric Cryptography
Build an HTTP server that receives an encrypted message and utilizes Symmetric Cryptography to decrypt it.
Modify the ``./exercises/symmetric_cryptography/symmetric_cryptography.py ``file to act as the HTTP client and send the encrypted message to the server.

Hint: The HTTP server can have an endpoint `POST /message` that expects the payload below.

``` json
{ "message": <encrypted message> }
```

### Asymmetric Cryptography
Build an HTTP server that receives a message and a signature and utilizes Asymmetric Cryptography to verify if the signature belongs to a specific public key.
Modify the ``./exercises/symmetric_cryptography/symmetric_cryptography.py ``file to act as the HTTP client and send the encrypted message to the server.

**Hint 1**: A common practice is to sign the hash of the message. So, the client should first calculate the hash of the message and then sign it.

**Hint 2**: The HTTP server can have an endpoint `POST /message` that expects the payload below. Considering that you are following **Hint 1**, the server should calculate the hash of the message and then verify the signature.

``` json
{
    "message": <message>,
    "signature": <signature>
}
```

## References
1. Narayanan, Arvind, et al. Bitcoin and cryptocurrency technologies: a comprehensive introduction. Princeton University Press, 2016
1. https://www.pycryptodome.org/