# Agoric SDK

A Python implementation of the Agoric SDK.

## Features

- ERTP (Electronic Rights Transfer Protocol)
- Zoe Smart Contract Framework
- Object Capability (Ocap) Model
- Notifiers and Updaters
- Wallet Management
- Treasury and Fund Management
- Virtual Machines (Vat)
- Cross-Chain Token Transfers (Pegasus)

## Installation

```bash
pip install agoric_sdk
```

## Usage

```python
from agoric_sdk import Mint, Zoe, Wallet

# Example usage of the Mint module
token_mint = Mint('Token')
token1 = token_mint.mint(100)
print(token1)
print(token_mint.get_supply())
```

## License

MIT License
