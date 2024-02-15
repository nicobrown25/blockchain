from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from dotenv import load_dotenv
import os
import requests
import hashlib

load_dotenv()

# TODO: connect wallet to random node


class Wallet:
    def __init__(self):
        self.private_key = RSA.generate(2048)
        self.public_key = self.private_key.publickey()
        self.node = os.getenv('NODE_SERVER_URL')

    def sign_message(self, message):
        message = message.encode('utf-8')
        hashed_message = SHA256.new(message)
        signature = pkcs1_15.new(self.private_key).sign(hashed_message)
        return signature

    def verify_signature(self, message, signature, public_key):
        message = message.encode('utf-8')
        hashed_message = SHA256.new(message)
        try:
            pkcs1_15.new(public_key).verify(hashed_message, signature)
            return True
        except (ValueError, TypeError):
            return False

    def add_transaction(self):
        public_key_string = self.public_key.export_key().decode('utf-8')
        sender = hashlib.sha256(public_key_string.encode('utf-8')).hexdigest()
        receiver = 'receiver'
        amount = 100

        print(
            f'Message -> Sender: {sender} Receiver {receiver} Amount: {amount}')

        response = requests.post(f'{self.node}/add_transaction', json={
            'sender': sender,
            'receiver': receiver,
            'amount': amount
        })
        return response.json()

    def get_chain(self):
        response = requests.get(f'{self.node}/get_chain')
        return response.json()

    def connect_node(self):
        return self.node
