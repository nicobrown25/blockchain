# MontyCoin: A Basic Cryptocurrency

MontyCoin is a simple implementation of a blockchain and cryptocurrency.

## Running the Project

1. navigate to scripts directory
2. run the servers (nodes) with ```./run.sh```
3. stop the nodes with  ```./stop.sh```

## Project Improvements

1. Transaction Validation:  Implement a system to validate transactions before they are added to the blockchain. This could include checking if the sender has enough balance to perform the transaction.
2. Wallets: Create a Wallet class that generates private and public keys for users. The private key can be used to sign transactions and the public key can be used as the user's address.
3. Transaction Signing and Verification: Implement a system where transactions are signed using the sender's private key and can be verified by others using the sender's public key. This ensures that only the owner of a wallet can make transactions from it.
4. Improved Mining Process: Modify the mining process. For example, you could implement a difficulty adjustment algorithm that adjusts the difficulty of the mining process based on the total computational power of the network.
5. Custom Hashing Algorithm: Implement a custom hashing algorithm for the blockchain. This could be a great way to learn about cryptographic hash functions.
6. Peer-to-Peer Network: Instead of manually adding nodes, implement a peer-to-peer network where nodes can discover each other.
7. GUI: Create a graphical user interface (GUI) for easier interaction with the blockchain.
8. Error Handling: Improve error handling and return appropriate HTTP status codes and messages when errors occur.
9. Data Persistence: Implement a system to store the blockchain data persistently.
10. Reward System: Implement a reward system for miners.