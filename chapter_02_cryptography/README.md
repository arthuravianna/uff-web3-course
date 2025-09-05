# Cryptography

Cryptography is a complex academic field that employs several advanced and intricate mathematical techniques. Hash functions, which we presented in the previous chapter, are part of this field. In this chapter, we present Ciphers and Digital Signatures. Ciphers can utilize symmetric or asymmetric cryptography. Digital Signatures use asymmetric cryptography.

A cipher is a class of algorithms used to encrypt or decrypt information. Digital Signatures are a class of algorithms used to sign a message and validate signatures. Symmetric cryptography utilizes a single key, hence its name. Asymmetric cryptography uses a key pair, consisting of a public key that is meant to be shared and a private key that is kept secret, hence its name. 

In the following subsections, we discuss Ciphers and Digital Signatures in more detail, along with the application of Digital Signatures in Blockchain. To run the examples and do the practical exercises in this chapter, you will need to install some Python packages. We advise using a virtual environment and the requirements file as follows:

``` shell
cd chapter_02_cryptography/
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

## Ciphers
As introduced, ciphers are a class of algorithms used to encrypt and decrypt data, aiming to protect its confidentiality. A typical scenario involves one party encrypting the message and sending it to the receiver. Therefore, even if someone is eavesdropping on the communication, they won't know the content of the message. Cipher algorithms can be symmetric or asymmetric.

### Symmetric Cipher
Symmetric Ciphers utilize the same key for both encryption and decryption of data. In this case, the sender and receiver share the same key. Symmetric ciphers are typically very fast and can process a large amount of data. Execute the code snippet below to observe how a message is encrypted and decrypted using a symmetric cipher algorithm.

> [!IMPORTANT]
> Make sure to install the requirements as mentioned at the beginning of the chapter before running the snippet.

``` python
>>> from Crypto.Cipher import Salsa20
>>> key = b'0123456789012345'
>>> nonce = b'2\x8e\xbb\x83\n\xf1\xefh'
>>> sender_cipher = Salsa20.new(key, nonce)
>>> ciphertext = sender_cipher.encrypt(b'You shall not pass!')
>>> ciphertext
b'\xf8F\x94J\xad\xdc\x8d\xb7l\x19m\xc8[<\xdb_^\xf0#'
>>> receiver_cipher = Salsa20.new(key, nonce)
>>> receiver_cipher.decrypt(ciphertext).decode()
'You shall not pass!'
```

### Asymmetric Cipher
Asymmetric Ciphers utilize a key pair, consisting of a public key for encryption and a private key for decryption. In this case, the sender encrypts the message using the public key, and the receiver decrypts it using the private key. Consider a scenario with three people, Alice, Bob, and Charlie. If Alice wants to send a message to Bob, she encrypts it using Bob's public key. However, if she wants to send a message to Charlie, she encrypts it using Charlie's public key. With this, Alice can guarantee that only the desired recipient will understand the message.

Therefore, asymmetric ciphers are useful when you have different recipients and want to make sure they can't understand messages addressed to each other. However, Asymmetric ciphers are typically very slow and can process only very small payloads. Execute the code snippet below to observe how a message is encrypted and decrypted using an asymmetric cipher algorithm, called PKCS#1 OAEP.

> [!IMPORTANT]
> Make sure to install the requirements as mentioned at the beginning of the chapter before running the snippet.

``` python
>>> from Crypto.Cipher import PKCS1_OAEP
>>> from Crypto.PublicKey import RSA
>>> message = b'You shall not pass!'
>>> key = RSA.importKey(open('rsa_public_key.pem').read())
>>> cipher = PKCS1_OAEP.new(key)
>>> ciphertext = cipher.encrypt(message)
>>> ciphertext
b'b\x84\xc2\x8f\xafb\x80Bb\xa74\xc2-\xe6\x05T\x99\x0b\x0b}\xe0l\xc5zM\xe8\\\x80\x0b\x8b\xcc\x12\xe5\xb2\xdb\xf7\xc2\x00T\xc2\xeb\xa2\x1d\x9e;<\xca@\xcc\x8d\x8e\xf6\x85\x9ag"r3\xf2\x9d \x10\xbcm\x1c\xa5\x07\x93\x1a\xa2\xb0.:+\xf9&\xc90\xe9~\xe6\xc2\x10\xa5L\xdd\xa7\xc82\x9a\x16\xba\xfb\x01$0\x95\xa9dJ!6\xe3t=Y \xfbd\xf9\x91^\xba]\xa4\xc8\xaaQN\xfb@*\xaaGr\xc8\xdf\x9a\xe70\xdd;;\xca\xa6\xff\nt\xad\xcb \xd8\xf4\xd3\x05\xaa[5\xea\xdc\xe2\x95\xd3\xcd\xc7\xbc\xb7\xaaNZ\xe7\x8eJ/\x08\xdcy\xb1\x9cwO\xc8mXPhes{\xad\x06\x8f\xe1(Yc\x9e\xab\xe5\xd7\xf0X\xce\xba\xe5\x9b\x82o\x00\xe9\xc9<K3\xd7\x95rq\xa6\xe5\xa7P\xd3\xd4\x1c\xed\xda\x10^\xd4*J\r\x05Ed\x93\xe9\xb7\xb7D\xe4c\xa1\x12\x16\xbe\xce\x80V\xe4\xdamg\xe7\x92B&QE\x19\xb2\xd1 `o'
>>> key = RSA.importKey(open('rsa_private_key.pem').read())
>>> cipher = PKCS1_OAEP.new(key)
>>> message = cipher.decrypt(ciphertext)
>>> message
b'You shall not pass!'
```

## Digital Signatures
A digital signature is a digital analog to a handwritten signature on paper. The objective is to replicate two properties present in handwritten signatures. The first, only you can make your signature, but anyone can verify it. Second, we want the signature to be tied to a specific document, so that somebody cannot use it to endorse a different document.

To reproduce these properties on digital signatures, we utilize asymmetric cryptography. The signature is generated using a private key. Therefore, the first property is guaranteed because only you know the private key. To achieve the second property, the signature is generated based on the message with a function that receives the message as a parameter, such as `sign(priv_key, msg)`.

Bitcoin and Ethereum utilize the Elliptic Curve Digital Signature Algorithm (ECDSA). ECDSA is a U.S.A. government standard, which is an update of the DSA algorithm adapted to use elliptic curves. A limitation of ECDSA is that it can only sign messages of 256 bits. However, this is not a significant issue, as you can sign the message hash. Therefore, you can use a cryptographic hash function, such as SHA256, to calculate the hash and then sign it. Execute the code snippet below to observe how you can sign the hash of a message and then verify its signature.

> [!IMPORTANT]
> Make sure to install the requirements as mentioned at the beginning of the chapter before running the snippet.

``` python
>>> from Crypto.Hash import SHA256
>>> from Crypto.PublicKey import ECC
>>> from Crypto.Signature import DSS
>>> private_key = ECC.import_key(open('ecdsa_private_key.pem', "rb").read())
>>> message = b'You shall not pass!'
>>> message_hash = SHA256.new(message)
>>> signer = DSS.new(private_key, 'fips-186-3')
>>> signature = signer.sign(message_hash)
>>> signature
b"\xd2\xd4\xfeaG\x9a\xb9\xa3\xb8\xbc\x94\xec)Q|\x1f\x19\xf0\x96\n$e\x07\x05C\xf5\x9c\xbf|9%\x13\x8d:Y}]\x08\x1fT\x9a\x06\xa4\x02)'(u\\%nI\x1a\x1b\xf6E\xd4\xde\x90\xd4Z)\x8b\xb6"
>>> public_key = ECC.import_key(open('ecdsa_public_key.pem', "rb").read())
>>> verifier = DSS.new(public_key, 'fips-186-3')
>>> verifier.verify(message_hash, signature) # Raises: ValueError – if the signature is not authentic
```

## Digital Signatures and Blockchain



## Practical Exercises
This section presents practical exercises that complement the reading.

### Ciphers
Build a client-server HTTP communication system that utilizes a symmetric cipher to exchange messages. The HTTP server should receive an encrypted message from a client and use a Symmetric Cipher to decrypt it.

- Modify the template file ``./exercises/cipher/cipher.py`` to encrypt and send the message to the server.
- Modify the template server file ``./exercises/cipher/cipher_server.py`` to decrypted the message.

**Hint 1**: The HTTP server can have an endpoint `POST /message` that expects the payload below.
**Hint 2**: To run the FastAPI server, execute the following command: `fastapi dev cipher_server.py`

``` json
{ "message": <encrypted message> }
```

### Digital Signatures
Build a client-server HTTP communication system that utilizes digital signatures to verify the messages exchanged. The HTTP server should receive a message and a signature and use the public key to verify the signature.

- Modify the template file ``./exercises/digital_signature/ds.py `` to sign the message and then send the message and the signature to the server.
- Modify the template server file ``./exercises/digital_signature/ds_server.py`` to verify the signature.

**Hint 1**: A common practice is to sign the hash of the message. So, the client should first calculate the hash of the message and then sign it. Consider using SHA256, a cryptographic hash function, to calculate the hash.

**Hint 2**: The HTTP server can have an endpoint `POST /message` that expects the payload below. Considering that you are following **Hint 1**, the server should calculate the hash of the message and then verify the signature.

**Hint 3**: To run the FastAPI server, execute the following command: `fastapi dev ds_server.py`

``` json
{
    "message": <message>,
    "signature": <signature>
}
```

## References
1. Narayanan, Arvind, et al. Bitcoin and cryptocurrency technologies: a comprehensive introduction. Princeton University Press, 2016
1. https://www.pycryptodome.org/