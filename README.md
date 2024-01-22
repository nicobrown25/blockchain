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