# Blockchain Application

This application demonstrates a basic implementation of a blockchain. It includes functionalities to create a new block, mine blocks, display the entire chain, and verify the chain's integrity.

## Setup Instructions

Before running the application, ensure you have the following prerequisites:

1. Download and install Python, Anaconda, Flask, and Postman.
2. Open Anaconda Navigator.
3. Launch Spyder (or your preferred Python IDE).
4. Set up your project directory structure.
5. Save your blockchain implementation in a file named `blockchain.py`.

## Running the Application

To start the blockchain application:

1. Navigate to your project directory in the terminal.
2. Run the command `python blockchain.py` to start the Flask server.
3. The server will start on `localhost` at port `5000`.

## Using Postman to Interact with the Blockchain

Postman can be used to interact with the blockchain via HTTP requests. Here are the available endpoints and how to use them:

### Mine a New Block

- **Endpoint:** `GET /mine_block`
- **Purpose:** This endpoint mines a new block.
- **Usage:** Send a GET request to `http://localhost:5000/mine_block`. The response includes details of the mined block.

### Get the Full Blockchain

- **Endpoint:** `GET /get_chain`
- **Purpose:** Retrieves the entire blockchain.
- **Usage:** Send a GET request to `http://localhost:5000/get_chain`. This will return the current blockchain and its length.

### Confirm Blockchain Validity

- **Endpoint:** `GET /confirm_chain`
- **Purpose:** Checks if the blockchain is valid.
- **Usage:** Send a GET request to `http://localhost:5000/confirm_chain`. The response will indicate whether the blockchain is valid.

## Interacting with the Blockchain

After sending requests via Postman, you will receive JSON responses that include blockchain data and confirmation messages. This allows you to visually verify the operations performed on the blockchain.
