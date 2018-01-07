class Blockchain(object):
    def __init__(self):
      self.chain=[] #empty list to store our blockchain
      self.current_transactions = [] #store transactions

    def new_block(self):
      #Creates a new block and adds it to the chain
      pass #do nothing

    def new_transaction(self):
      #Add a new transaction to the list of transactions
      pass

    @staticmethod
    def hash(block): #hashes are immutable blocks
      # Hashes a block
      pass

    @property
    def last_block(self):
      #Returns the last Block in the chain
      pass
  