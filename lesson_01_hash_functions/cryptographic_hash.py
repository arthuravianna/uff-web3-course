import sys
from hashlib import sha256


# sha256's output has 256 bits.
# So, the hexdigest will have 64 characters
# because each hex character represents 4 bits,
# therefore, 64 * 4 = 256.
def h(s):
    return sha256(s.encode()).hexdigest()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: Expected one parameter")
        print("Usage: python3 criptographic_hash.py '<input>'")
        sys.exit(1)

    s = sys.argv[1]
    print(f"s: {s}\nH(s): {h(s)}")

    