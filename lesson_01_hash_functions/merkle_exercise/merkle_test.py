import unittest
from hashlib import sha256
import merkle

def h(string):
    return sha256(string.encode()).hexdigest()

#Globals
ROOTS = []
#Blocks necessary to prove
PROOF = {"test0": [], "test1": [], "test2": [], "test3": [], "test4": [], "test5": []}
DIGEST0 = "\x00"

class MerkleTreeTest(unittest.TestCase):

	#######################################
	#       TESTES ÁRVORE DE MERKLE       #
	#######################################

	def test_merkleize_0(self):
		digest1 = h("Unbelievable...")
		root = digest1
		ROOTS.append(root)
		self.assertEqual(merkle.merkleize("Unbelievable..."), root)

	def test_merkleize_1(self):

		digest1 = h("In")
		digest2 = h("our")
		digest3 = h("village,")
		digest4 = h("folks")
		digest5 = h("say")
		digest6 = h("God")
		digest7 = h("crumbles")
		digest8 = h("up")
		digest9 = h("the")
		digest10 = h("old")
		digest11 = h("moon")
		digest12 = h("into")
		digest13 = h("stars.")

		PROOF["test1"].append((digest3, merkle.Side.LEFT))

		digest1 = h(digest1+digest2)
		digest2 = h(digest3+digest4)
		digest3 = h(digest5+digest6)
		digest4 = h(digest7+digest8)
		digest5 = h(digest9+digest10)
		digest6 = h(digest11+digest12)
		digest7 = h(digest13+DIGEST0)

		PROOF["test1"].append((digest1, merkle.Side.LEFT))

		digest1 = h(digest1+digest2)
		digest2 = h(digest3+digest4)
		digest3 = h(digest5+digest6)
		digest4 = h(digest7+DIGEST0)

		PROOF["test1"].append((digest2, merkle.Side.RIGHT))

		digest1 = h(digest1+digest2)
		digest2 = h(digest3+digest4)

		PROOF["test1"].append((digest2, merkle.Side.RIGHT))

		root = h(digest1+digest2)
		ROOTS.append(root)
		self.assertEqual(merkle.merkleize("In our village, folks say God crumbles up the old moon into stars."), root)

	def test_merkleize_2(self):

		digest1 = h("I")
		digest2 = h("love")
		digest3 = h("chicken!")

		PROOF["test2"].append((digest1, merkle.Side.LEFT))

		digest1 = h(digest1+digest2)
		digest2 = h(digest3+DIGEST0)

		PROOF["test2"].append((digest2, merkle.Side.RIGHT))

		root = h(digest1+digest2)
		ROOTS.append(root)
		self.assertEqual(merkle.merkleize("I love chicken!"), root)

	def test_merkleize_3(self):

		digest1 = h("Eu")
		digest2 = h("adoraria")
		digest3 = h("aprender")
		digest4 = h("mais")
		digest5 = h("sobre")
		digest6 = h("Blockchain!")

		PROOF["test3"].append((digest5, merkle.Side.LEFT))

		digest1 = h(digest1+digest2)
		digest2 = h(digest3+digest4)
		digest3 = h(digest5+digest6)

		PROOF["test3"].append((DIGEST0, merkle.Side.RIGHT))

		digest1 = h(digest1+digest2)
		digest2 = h(digest3+DIGEST0)

		PROOF["test3"].append((digest1, merkle.Side.LEFT))

		root = h(digest1+digest2)
		ROOTS.append(root)
		self.assertEqual(merkle.merkleize("Eu adoraria aprender mais sobre Blockchain!"), root)

	def test_merkleize_4(self):

		digest1 = h("Os")
		digest2 = h("fins")
		digest3 = h("justificam")
		digest4 = h("os")
		digest5 = h("meios.")

		PROOF["test4"].append((digest3, merkle.Side.LEFT))

		digest1 = h(digest1+digest2)
		digest2 = h(digest3+digest4)
		digest3 = h(digest5+DIGEST0)

		PROOF["test4"].append((digest1, merkle.Side.LEFT))

		digest1 = h(digest1+digest2)
		digest2 = h(digest3+DIGEST0)

		PROOF["test4"].append((digest2, merkle.Side.RIGHT))

		root = h(digest1+digest2)
		ROOTS.append(root)
		self.assertEqual(merkle.merkleize("Os fins justificam os meios."), root)

	def test_merkleize_5(self):
		digest1 = h("I")
		digest2 = h("must")
		digest3 = h("uphold")
		digest4 = h("my")
		digest5 = h("ideals,")
		digest6 = h("for")
		digest7 = h("perhaps")
		digest8 = h("the")
		digest9 = h("time")
		digest10 = h("will")
		digest11 = h("come")
		digest12 = h("when")
		digest13 = h("I")
		digest14 = h("shall")
		digest15 = h("be")
		digest16 = h("able")
		digest17 = h("to")
		digest18 = h("carry")
		digest19 = h("them")
		digest20 = h("out.")

		PROOF["test5"].append((digest6, merkle.Side.RIGHT))

		digest1 = h(digest1+digest2)
		digest2 = h(digest3+digest4)
		digest3 = h(digest5+digest6)
		digest4 = h(digest7+digest8)
		digest5 = h(digest9+digest10)
		digest6 = h(digest11+digest12)
		digest7 = h(digest13+digest14)
		digest8 = h(digest15+digest16)
		digest9 = h(digest17+digest18)
		digest10 = h(digest19+digest20)

		PROOF["test5"].append((digest4, merkle.Side.RIGHT))

		digest1 = h(digest1+digest2)
		digest2 = h(digest3+digest4)
		digest3 = h(digest5+digest6)
		digest4 = h(digest7+digest8)
		digest5 = h(digest9+digest10)

		PROOF["test5"].append((digest1, merkle.Side.LEFT))

		digest1 = h(digest1+digest2)
		digest2 = h(digest3+digest4)
		digest3 = h(digest5+DIGEST0)

		PROOF["test5"].append((digest2, merkle.Side.RIGHT))

		digest1 = h(digest1+digest2)
		digest2 = h(digest3+DIGEST0)

		PROOF["test5"].append((digest2, merkle.Side.RIGHT))

		root = h(digest1+digest2)
		ROOTS.append(root)
		self.assertEqual(merkle.merkleize("I must uphold my ideals, for perhaps the time will come when I shall be able to carry them out."), root)

	#######################################
	#          MERKLE PATH TESTS          #
	#######################################

	def test_validate_proof_0(self):
		self.assertTrue(merkle.validate_proof(ROOTS[0], "Unbelievable...", PROOF["test0"]))

	def test_validade_proof_1(self):
		self.assertTrue(merkle.validate_proof(ROOTS[1], "folks", PROOF["test1"]))

	def test_validade_proof_2(self):
		self.assertTrue(merkle.validate_proof(ROOTS[2], "love", PROOF["test2"]))

	def test_validate_proof_3(self):
		self.assertTrue(merkle.validate_proof(ROOTS[3], "Blockchain!", PROOF["test3"]))

	def test_validate_proof_4(self):
		self.assertTrue(merkle.validate_proof(ROOTS[4], "os", PROOF["test4"]))

	def test_validade_proof_5(self):
		self.assertTrue(merkle.validate_proof(ROOTS[5], "ideals,", PROOF["test5"]))

if __name__ == '__main__':
    unittest.main()

