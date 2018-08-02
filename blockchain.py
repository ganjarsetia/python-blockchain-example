class Blockhain(object):
    def __init__(self):
        self.chain = []
        self.current_transaction = []

    def new_block(self):
        # Creates a new Block and adds it to the chain
        pass

    def new_transaction(self):
        # Adds a new transaction to the list of transactions
        return 'hi'

    @staticmethod
    def hash(block):
        # Hashses a block
        pass

    @property
    def last_block(self):
        # Returns the last Block in the chain
        pass
