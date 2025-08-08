#######################################
#              PART 1                 #
#######################################

from hashlib import sha256

def h(string):
    return sha256(string.encode()).hexdigest()

def merkleize(sentence: str) -> str:
	merkle = list(map(h, sentence.split(" ")))
	#padding da árvore
	while(len(merkle) != 1):
		if(len(merkle) % 2 != 0):
			merkle.append("\x00")
		for i in range(len(merkle)//2):
			merkle.append(h(merkle.pop(0) + merkle.pop(0)))

	return merkle[0]

#######################################
#              PART 2                 #
#######################################

from enum import Enum
class Side(Enum):
  LEFT = 0
  RIGHT = 1

def validate_proof(root: str, data: str, proof: [(str, Side)]) -> bool:
	aux = h(data)
	while(len(proof) > 0):
		sibiling = proof.pop(0)
		if(sibiling[1] == Side.RIGHT):
			aux = h(aux + sibiling[0])
		else:
			aux = h(sibiling[0] + aux)
	if(aux == root):
		return True
	else:
		return False

def main():
	s = input("Input to calculate Merkle Root Hash\n")
	print(merkleize(s))

if __name__ == '__main__':
	main()

