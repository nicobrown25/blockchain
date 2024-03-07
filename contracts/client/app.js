window.addEventListener('load', async () => {
    if (window.ethereum) {
        window.web3 = new Web3(window.ethereum);
        try {
            await window.ethereum.request({ method: 'eth_requestAccounts' });
        } catch (error) {
            console.error("User denied account access");
            return;
        }
    } else {
        console.error("Please install MetaMask!");
        return;
    }

    const simpleStorage = new web3.eth.Contract(config.abi, config.contractAddress);

    window.setMessage = async () => {
        const messageInput = document.getElementById('messageInput');
        const message = messageInput.value;
        console.log(message)
        const accounts = await web3.eth.getAccounts();
        if (accounts.length === 0) {
            console.error("No accounts found. Make sure MetaMask is connected.");
            return;
        }
        try {
            await simpleStorage.methods.updateMessage(message).send({ from: accounts[0] });
        } catch (error) {
            console.error("Error sending transaction:", error);
        }
    };

    window.getMessage = async () => {
        try {
            const value = await simpleStorage.methods.message().call();
            document.getElementById('message').innerText = `Message: ${value}`;
        } catch (error) {
            console.log("HI AGAIN")
            console.error("Error fetching value:", error);
        }
    };
});
