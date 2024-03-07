# Blockchain Spring 2024

### Setup

1. Create python virtual environment: `python -m venv venv`
2. Switch to virtual environment: `source venv/bin/activate`
3. Install packages `pip install -r requirements.txt`

## Blockchain

### Endpoint Collections

- [Basic Blockchain](https://nobles-blockchain.postman.co/workspace/New-Team-Workspace~6ee04c91-09b2-4066-a420-2d5e83667e0d/collection/24854847-a4059b9c-1111-4056-82e7-6c845caf1603?action=share&creator=24854847)
- [Basic Blockchain Expanded](https://nobles-blockchain.postman.co/workspace/New-Team-Workspace~6ee04c91-09b2-4066-a420-2d5e83667e0d/collection/24854847-852421c2-4abb-4502-a0cf-e8117949fb49?action=share&creator=24854847)

### Running the Project

1. To run the application, use the following command: `python basic_blockchain_expanded.py`. The application will start a Flask server on http://127.0.0.1:5000.

## Cryptocurrency

MontyCoin is a simple implementation of a blockchain and cryptocurrency.

### Endpoint Collections

- [Cryptocurrency](https://nobles-blockchain.postman.co/workspace/New-Team-Workspace~6ee04c91-09b2-4066-a420-2d5e83667e0d/collection/24854847-5aaeccc5-c743-4bf6-a1a2-5f3ec30ad654?action=share&creator=24854847) ([export](./endpoint_collections/basic_crypto.json))
- [Transaction Picker](https://nobles-blockchain.postman.co/workspace/Blockchain~6ee04c91-09b2-4066-a420-2d5e83667e0d/collection/31591599-4b3fe1aa-9f86-41a1-9705-ac6bd2beabe5?action=share&creator=24854847) ([export](endpoint_collections/transaction_picker.json))

### Running the Project

1. Run `chmod +x run.sh` and `chmod +x stop.sh` from scripts directory to make scripts executable
2. Run `start.py` from currency directory to start node controller and wallet GUIs. The servers (nodes) with `./run.sh`. This will start 4 nodes on http://127.0.0.1:5000 - http://127.0.0.1:5003

## Smart Contracts

### Setup
1. Install [MetaMask](https://metamask.io/) browser extension
2. Get Sepolia testnet ETH from a [faucet](https://faucet.quicknode.com/ethereum/sepolia/).

### Deploy Contract
1. Copy HelloWorld.sol into [Remix](https://remix.ethereum.org/). Compile. Deploy to MetaMask.
2. Copy ABI and deployed contract address into config.js

### Run Client
1. Use http-server to run index.html/app.js frontend client
2. Use [Sepolia etherscan](https://sepolia.etherscan.io/) to view contract transactions
