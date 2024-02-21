### Create a Blockchain ###

# Import Libraries

import datetime
import hashlib
import json
from flask import Flask, jsonify

### Build Blockchain

class Blockchain: 
    
    def __init__(self): 
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0', time_elapsed = '0')
        self.difficulty = 6;
        
    def create_block(self, proof, previous_hash, time_elapsed): 
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'time_elapsed': time_elapsed,
                 'previous_hash': previous_hash}
        self.chain.append(block)
        return block
    
    def get_previous_block(self): 
        return self.chain[-1]
    
    def proof_of_work(self, previous_proof): 
        start_time = datetime.datetime.now()
        new_proof = 1
        hash_operation = ''
        time_elapsed = ''
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
           
            if hash_operation[:self.difficulty] == '0' * self.difficulty:
                check_proof = True
            else: 
                new_proof += 1
        end_time = datetime.datetime.now()
        time_elapsed = str(end_time - start_time)
        return new_proof, hash_operation, time_elapsed # return new time 
    
    def hash(self, block): 
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:self.difficulty] != '0' * self.difficulty:
                return False
            previous_block = block
            block_index += 1
        return True

### Mine Blockchain

# Create Web App
app = Flask(__name__)

# Create Blockchain
blockchain = Blockchain()

# Mine a new block
@app.route('/mine_block', methods = ['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof, hash_operation, time_elapsed = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash, time_elapsed)
    response = {'message': 'Congratulations, you just mined a block!',
                'hash': hash_operation,
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'time_elapsed': block['time_elapsed'] + ' seconds',
                'previous_hash': block['previous_hash']}
    return jsonify(response), 200

# Get a full blockchain
@app.route('/get_chain', methods = ['GET'])
def get_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200

# Confirm chain is valid
@app.route('/confirm_chain', methods = ['GET'])
def confirm_chain():
    response = {'valid': blockchain.is_chain_valid(blockchain.chain)}
    return jsonify(response), 200

# Run app
app.run(host = '0.0.0.0', port = 5001)
    







