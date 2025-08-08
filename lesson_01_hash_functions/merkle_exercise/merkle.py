#######################################
#              PART 1                 #
#######################################

from hashlib import sha256

def h(string):
    return sha256(string.encode()).hexdigest()

def merkleize(sentence: str) -> str:
	pass
#######################################
#              PART 2                 #
#######################################

from enum import Enum
class Side(Enum):
  LEFT = 0
  RIGHT = 1

def validate_proof(root: str, data: str, proof: [(str, Side)]) -> bool:
	pass


def main():
	s = input("Input to calculate Merkle Root Hash\n")
	print(merkleize(s))

if __name__ == '__main__':
	main()

