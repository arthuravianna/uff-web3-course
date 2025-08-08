import sys

HASH_OUTPUT_SIZE = 13

def h(s):
    # Step 1: Convert string to number (base 128)
    # value = ord(s[n]) * 128ⁿ + ord(s[n-1]) * 128ⁿ⁻¹+...+ord(s[0]) * 128⁰
    value = 0
    for char in s:
        value = value*128 + ord(char)
    
    # Step 2: Division–remainder
    return value % HASH_OUTPUT_SIZE


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: Expected one parameter")
        print("Usage: python3 simple_hash.py '<input>'")
        sys.exit(1)

    s = sys.argv[1]
    print(f"s: {s}\nH(s): {h(s)}")

    