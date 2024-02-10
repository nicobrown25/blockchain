from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import tkinter as tk
import requests
import hashlib


class Wallet:
    def __init__(self):
        self.private_key = RSA.generate(2048)
        self.public_key = self.private_key.publickey()

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
        receiver = 'receiver_address_placeholder'
        amount = 100
        response = requests.post('http://localhost:5000/add_transaction', json={
            'sender': sender,
            'receiver': receiver,
            'amount': amount
        })
        return response.json()

    def get_chain(self):
        response = requests.get('http://localhost:5000/get_chain')
        return response.json()


def run_test():
    wallet = Wallet()

    message = "This is a test message"
    signature = wallet.sign_message(message)
    verification_result = wallet.verify_signature(
        message, signature, wallet.public_key)
    print("Verification result with correct public key: ", verification_result)

    another_wallet = Wallet()

    verification_result = wallet.verify_signature(
        message, signature, another_wallet.public_key)
    print("Verification result with different public key: ", verification_result)

# run_test()


wallet = Wallet()


def on_button_public_key_clicked():
    print(wallet.public_key.export_key().decode())


def on_button_private_key_clicked():
    print(wallet.private_key.export_key().decode())


def on_button_add_transaction_clicked():
    response = wallet.add_transaction()
    print(response)


def on_button_get_chain_clicked():
    response = wallet.get_chain()
    print(response)


root = tk.Tk()

button_public_key = tk.Button(
    root, text="Show Public Key", command=on_button_public_key_clicked)
button_public_key.pack()

button_private_key = tk.Button(
    root, text="Show Private Key", command=on_button_private_key_clicked)
button_private_key.pack()

button_add_transaction = tk.Button(
    root, text="Add Transaction", command=on_button_add_transaction_clicked)
button_add_transaction.pack()

on_button_get_chain_clicked = tk.Button(
    root, text="Get Chain", command=on_button_get_chain_clicked)
on_button_get_chain_clicked.pack()

root.mainloop()

run_test()
