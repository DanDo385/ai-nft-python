from solcx import compile_standard, install_solc
import json
import os

# Install Solidity compiler
install_solc('0.8.0')

# Load the Solidity contract
contract_source_code = '''
pragma solidity ^0.8.0;

contract MyContract {
    string public greet = "Hello, World!";
}
'''

# Compile the contract
compiled_sol = compile_standard({
    "language": "Solidity",
    "sources": {
        "MyContract.sol": {
            "content": contract_source_code
        }
    },
    "settings": {
        "outputSelection": {
            "*": {
                "*": ["abi", "evm.bytecode"]
            }
        }
    }
})

# Extract ABI and bytecode
abi = compiled_sol['contracts']['MyContract.sol']['MyContract']['abi']
bytecode = compiled_sol['contracts']['MyContract.sol']['MyContract']['evm']['bytecode']['object']

# Ensure the artifacts directory exists
artifacts_dir = os.path.join('backend', 'artifacts')
os.makedirs(artifacts_dir, exist_ok=True)

# Save ABI
with open(os.path.join(artifacts_dir, 'MyContract.abi'), 'w') as abi_file:
    json.dump(abi, abi_file, indent=4)

# Save bytecode
with open(os.path.join(artifacts_dir, 'MyContract.bytecode'), 'w') as bytecode_file:
    bytecode_file.write(bytecode)

print("Compilation successful. ABI and bytecode saved in the artifacts directory.")
