<<<<<<< HEAD
To start, I added a self.difficulty feature that makes it much easier to change the mining 
difficulty of the blockchain. Instead of having to alter multiple lines of code to change
the mining difficulty, now I just have to change one number near the top, and it will alter 
all of the lines it needs to. Also, I made a new feature that measures the time it takes to 
mine a block. It does this by first creating a variable equal to the datetime.datetime.now()
at the beginning of the proof of work function, and when it reaches the end of the loop, signifying
the completion of the mining, it creates another variable equal to the datetime.datetime.now().
It then subtracts the initial variable from the final one, and then saves it in a variable called
time_elapsed. When a block is mined, it adds another field to the output, and tells you how many 
seconds it took to mine the block.

A class is something in python that lets you tell the code what to do with an object. It is like a
blueprint for what to do when creating a blockchain. In this code, Blockchain is the name of the 
class, and it creates a blockchain object when it is run.

An endpoint is the way that you would access the code from a server. A server is a computer that 
provides some functionality to a different party; in this code it would run the /get_chain function
and the /confirm_chain and the /mine_block. Flask is a program that you can use to make an online
user interface where others can access your code. Postman is something that you can use to test
your code, and lets you run a command without needing to re-write the command to access the code
for each iteration.

When I started writing this code, I planned on making a time_elapsed variable that would tell you
how long it took to mine each block. Though it was not difficult to generate the actual time value,
it proved more difficult to make it so that it would output the time that it generated, as I had to
incorporate it into the mine.block() function.
=======
# Blockchain Spring 2024

## Blockchain 
### Endpoint Collections 
  - [Basic Blockchain](https://nobles-blockchain.postman.co/workspace/New-Team-Workspace~6ee04c91-09b2-4066-a420-2d5e83667e0d/collection/24854847-a4059b9c-1111-4056-82e7-6c845caf1603?action=share&creator=24854847)
  - [Basic Blockchain Expanded](https://nobles-blockchain.postman.co/workspace/New-Team-Workspace~6ee04c91-09b2-4066-a420-2d5e83667e0d/collection/24854847-852421c2-4abb-4502-a0cf-e8117949fb49?action=share&creator=24854847)

### Running the Project
1. To run the application, use the following command: ```python basic_blockchain_expanded.py```. The application will start a Flask server on http://127.0.0.1:5000.
## Cryptocurrency

MontyCoin is a simple implementation of a blockchain and cryptocurrency.

### Endpoint Collections
  - [Cryptocurrency](https://nobles-blockchain.postman.co/workspace/New-Team-Workspace~6ee04c91-09b2-4066-a420-2d5e83667e0d/collection/24854847-5aaeccc5-c743-4bf6-a1a2-5f3ec30ad654?action=share&creator=24854847)
  - [Transaction Picker](https://nobles-blockchain.postman.co/workspace/Blockchain~6ee04c91-09b2-4066-a420-2d5e83667e0d/collection/31591599-4b3fe1aa-9f86-41a1-9705-ac6bd2beabe5?action=share&creator=24854847)

### Running the Project
1. Navigate to scripts directory
2. Run ```chmod +x run.sh``` and ```chmod +x stop.sh``` to make scripts executable
3. Run the servers (nodes) with ```./run.sh```. This will start 4 nodes on http://127.0.0.1:5000 - http://127.0.0.1:5003
4. Stop the nodes with  ```./stop.sh```

### Project Improvements
1. **Transaction Validation**:  Implement a system to validate transactions before they are added to the blockchain. This could include checking if the sender has enough balance to perform the transaction.
2. **Wallets**: Create a Wallet class that generates private and public keys for users. The private key can be used to sign transactions and the public key can be used as the user's address.
3. **Transaction Signing and Verification**: Implement a system where transactions are signed using the sender's private key and can be verified by others using the sender's public key. This ensures that only the owner of a wallet can make transactions from it.
4. **Improved Mining Process**: Modify the mining process. For example, you could implement a difficulty adjustment algorithm that adjusts the difficulty of the mining process based on the total computational power of the network.
5. **Custom Hashing Algorithm**: Implement a custom hashing algorithm for the blockchain. This could be a great way to learn about cryptographic hash functions.
6. **Peer-to-Peer Network**: Instead of manually adding nodes, implement a peer-to-peer network where nodes can discover each other.
7. **GUI**: Create a graphical user interface (GUI) for easier interaction with the blockchain.
8. **Error Handling**: Improve error handling and return appropriate HTTP status codes and messages when errors occur.
9. **Data Persistence**: Implement a system to store the blockchain data persistently.
10.** Reward System**: Implement a reward system for miners.

### Smart Contracts
>>>>>>> 2496eef8fa6156ba57cc45c9ae1811629f0b6aca
