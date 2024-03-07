import tkinter as tk
import tkinter.messagebox as messagebox
import subprocess
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
nodes = os.getenv('NODES').split(',')
node_base_url = os.getenv('NODE_BASE_URL')
nodes = [node_base_url + ':' + node for node in nodes]


def on_button_connect_nodes_clicked():
    for node in nodes:
        try:
            response = requests.post(
                f"{node}/connect_node", json={'nodes': nodes})
            if response.status_code == 201:
                print(f"Node {node} connected successfully.")
            else:
                print(f"Failed to connect node {node}.")
        except requests.exceptions.RequestException as err:
            print(f"Failed to connect node {node}. Error: {err}")


def on_button_mine_clicked():
    selected_node = node_var.get()
    try:
        response = requests.get(f"{selected_node}/mine_block")
        if response.status_code == 200:
            print(f"Block mined successfully on node {selected_node}.")
        else:
            print(f"Failed to mine block on node {selected_node}.")
    except requests.exceptions.RequestException as err:
        print(f"Failed to mine block on node {selected_node}. Error: {err}")


def on_button_get_chain_clicked():
    selected_node = node_var.get()
    try:
        response = requests.get(f"{selected_node}/get_chain")
        if response.status_code == 200:
            print(f"Blockchain: {response.json()}")
        else:
            print(f"Failed to get blockchain from node {selected_node}.")
    except requests.exceptions.RequestException as err:
        print(f"Failed to get blockchain from node {
              selected_node}. Error: {err}")


def on_button_replace_chain_clicked():
    selected_node = node_var.get()
    try:
        response = requests.get(f"{selected_node}/replace_chain")
        if response.status_code == 200:
            print(f"{response.json()['message']}")
        else:
            print(f"Failed to replace blockchain on node {selected_node}.")
    except requests.exceptions.RequestException as err:
        print(f"Failed to replace blockchain on node {
              selected_node}. Error: {err}")


def on_button_confirm_chain_clicked():
    selected_node = node_var.get()
    try:
        response = requests.get(f"{selected_node}/confirm_chain")
        if response.status_code == 200:
            print(f"{response.json()['message']}")
        else:
            print(f"Failed to confirm blockchain on node {selected_node}.")
    except requests.exceptions.RequestException as err:
        print(f"Failed to confirm blockchain on node {
              selected_node}. Error: {err}")


root = tk.Tk()


button_start_nodes = tk.Button(
    root, text="Start Nodes", command=lambda: subprocess.run(["bash", "./scripts/run.sh"]))
button_start_nodes.pack()

button_connect_nodes = tk.Button(
    root, text="Connect Nodes", command=on_button_connect_nodes_clicked)
button_connect_nodes.pack()

button_kill_nodes = tk.Button(
    root, text="Kill Nodes", command=lambda: subprocess.run(["bash", "./scripts/stop.sh"]))
button_kill_nodes.pack()

node_var = tk.StringVar(root)
node_var.set(nodes[0])  # default value
node_label = tk.Label(root, text="Node:")
node_label.pack()
node_dropdown = tk.OptionMenu(root, node_var, *nodes)
node_dropdown.pack()

button_mine = tk.Button(root, text="Mine", command=on_button_mine_clicked)
button_mine.pack()

button_get_chain = tk.Button(
    root, text="Get Chain", command=on_button_get_chain_clicked)
button_get_chain.pack()

button_replace_chain = tk.Button(
    root, text="Replace Chain", command=on_button_replace_chain_clicked)
button_replace_chain.pack()

button_confirm_chain = tk.Button(
    root, text="Confirm Chain", command=on_button_confirm_chain_clicked)
button_confirm_chain.pack()

root.mainloop()
