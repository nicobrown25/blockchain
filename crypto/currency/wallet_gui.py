import tkinter as tk
from wallet import Wallet

wallet = Wallet()


def on_button_public_key_clicked():
    print("Public Key", wallet.public_key.export_key().decode())


def on_button_private_key_clicked():
    print("Private Key", wallet.private_key.export_key().decode())


def on_button_add_transaction_clicked():
    response = wallet.add_transaction()
    print("Transaction", response)


def on_button_get_chain_clicked():
    response = wallet.get_chain()
    print("Blockchain", response)


def on_button_connect_node_clicked():
    response = wallet.connect_node()
    print("Node", response)


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

button_get_chain = tk.Button(
    root, text="Get Chain", command=on_button_get_chain_clicked)
button_get_chain.pack()

button_connect_node = tk.Button(
    root, text="Connect Node", command=on_button_connect_node_clicked)
button_connect_node.pack()

root.mainloop()
