To start, I added a self.difficulty feature that makes it much easier to change the mining 
difficulty of the blockchain. Instead of having to alter multiple lines of code to change
the mining difficulty, now I just have to change one number near the top, and it will alter 
all of the lines it needs to. Also, I made a new feature that measures the time it takes to 
mine a block. It does this by first creating a variable equal to the datetime.datetime.now()
at the beginning of the proof of work function, and when it reaches the end of the loop, signifying
the completion of the mining, it creates another variable equal to the datetime.datetime.now().
It then subtracts the initial variable from the final one 