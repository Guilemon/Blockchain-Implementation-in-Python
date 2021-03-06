import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
      self.chain=[] #empty list to store our blockchain
      self.current_transactions = [] #store transactions

      #create the genesis block - a block with no predecessors
      self.new_block(previous_hash=1,proof=100)

    def new_block(self,proof,previous_hash=None):
      """
      Creates a new block and adds it to the chain

      :param proof:<int> The proof given by the Proof of Work algorithm
      :param previous_hash: (Optional) <str> Hash of previous Block
      :return: <dict> New Block
      """
      block = {
      'index': len(self.chain)+1,
      'timestamp': time(),
      'transactions': self.current_transactions,
      'proof': proof,
      'previous_hash': previous_hash or self.hash(self.chain[-1]),
      }
      #Reset the current list of transactions
      self.current_transactions = []
      self.chain.append(block)
      return block

    def new_transaction(self,sender,recipient,amount):
      """
      Creates a new transaction to go into the next mined Block
      :param sender:<str> Address of the Sender
      :param recipient:<str> Address of the recipient
      :param amount:<int> Amount
      :return: <int> The index of the Block that will hole this transaction
      """
      self.current_transaction.append({
          'sender':sender,
          'recipient':recipient,
          'amount':amount,
      })
      return self.last_block['index'] + 1

    @staticmethod
    def hash(block): #hashes are immutable blocks
      """
      Creates a SHA-256 hash of a Block
      :param block: <dict> Block
      :return: <str>
      """
      #Dictionary should be ordered or else we will have inconsistent hashes

      block_string = json.dumps(block,sort_keys=True).encode()
      return hashlib.sha256(block_string).hexdigest();


    @property
    def last_block(self):
      #Returns the last Block in the chain
      return self.chain[-1]

