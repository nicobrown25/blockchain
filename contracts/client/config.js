const config = {
    contractAddress: "0x32D2Ee30e633022440eca6d0FDA0131FE13bBf6e",
    abi: [
        {
            "inputs": [],
            "stateMutability": "nonpayable",
            "type": "constructor"
        },
        {
            "inputs": [],
            "name": "message",
            "outputs": [
                {
                    "internalType": "string",
                    "name": "",
                    "type": "string"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "string",
                    "name": "newMessage",
                    "type": "string"
                }
            ],
            "name": "updateMessage",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        }
    ]
};