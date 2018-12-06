#generate timestamps
import datetime
#import hashing algorithm
import hashlib
#define the 'block' data structure
class Block:
  #Each block contains 7 attributes
  #1st number of blocks
  #2nd what data is stored in this block?
  #3rd Pointer to the next block
  #4th The hash of this block
  #5th A nonce is a number only used once
  #6th store the hash (ID) of the previous block in the chain
  #7th timestamp
  block_no = 0
  data = None
  next = None
  hash = None
  nonce = 0
  previous_hash = 0x0
  timestamp = datetime.datetime.now()

  #we initialize a block by storing some data in it
  def __init__(self, data):
    self.data = data

  #Function to compute 'hash' of block
  def hash(self):
    h = hashlib.sha256()
    h.update(
    str(self.nonce).encode('utf-8') +
    str(self.data).encode('utf-8') +
    str(self.previous_hash).encode('utf-8') +
    str(self.timestamp).encode('utf-8') +
    str(self.block_no).encode('utf-8')
    )
    return h.hexdigest()

  def __str__(self):
    #print out the value of block
    return "Block Hash " + str(self.hash()) + "\nBlock No: " + str(self.block_no)
#defne the blockchain datastructure
#consist of 'blocks' linked togther
class Blockchain:

  max_nonce = 2**32
  diff = 10
  target = 2 ** (256-diff)
  #generate the first block in the blockchain
  block = Block("Genesis")
  #set it as the head of our blockchain
  head = block

  #adds a given blcok to the chain of the blocks
  def add(self, block):
    block.previous_hash = self.block.hash()
    block.block_no = self.block.block_no + 1

    self.block.next = block
    self.block = self.block.next

  #determines whether or not we can add a given block to the blockchain
  def mine(self, block):
    for i in range(self.max_nonce):
      if int(block.hash(), 16) <= self.target:
          self.add(block)
          print(block)
          break
      else:
        block.nonce += 1

#initialize Blockchain
blockchain = Blockchain();

#mine 10 blocks
for i in range(10):
  blockchain.mine(Block("Block " + str(i+1)))
#print out the Block in the Blockchain
while blockchain.head != None:
  print(blockchain.head)
  blockchain.head = blockchain.head.next
