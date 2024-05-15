from web3 import Web3
import json
import os

# Connect to local Ethereum node
ganache_url = 'http://127.0.0.1:8545'
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Check if connected to the node
if not web3.isConnected():
    raise Exception("Failed to connect to Ethereum node")

# Set default account
web3.eth.default_account = web3.eth.accounts[0]

# Load ABI and bytecode
artifacts_dir = os.path.join('/Users/dandoe/Desktop/Code/ai-nft-python/backend', 'artifacts')
with open(os.path.join(artifacts_dir, 'NFT.abi'), 'r') as abi_file:
    abi = json.load(abi_file)

with open(os.path.join(artifacts_dir, 'NFT.bytecode'), 'r') as bytecode_file:
    bytecode = bytecode_file.read()

# Deploy contract
NFT = web3.eth.contract(abi=abi, bytecode=bytecode)
tx_hash = NFT.constructor("MyNFT", "NFT").transact()
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

# Save contract address
contract_address = tx_receipt.contractAddress
deployment_info = {'contract_address': contract_address}
with open(os.path.join(artifacts_dir, 'deployed_contract_address.json'), 'w') as address_file:
    json.dump(deployment_info, address_file, indent=4)

print(f"Contract deployed at address: {contract_address}")
print("Deployment information saved in the artifacts directory.")
