import unittest
from blockchain import Blockhain


class BlockTestCase(unittest.TestCase):
    def test_new_transaction(self):
        blockchain = Blockhain()
        self.assertEqual(blockchain.new_transaction(), 'hi')


if __name__ == '__main__':
    unittest.main()

""" blockchain = Blockhain()
blockchain.new_block() """
