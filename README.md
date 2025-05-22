

# BNBChainTestnet

Automating Chainlink Faucet for BNB Chain Testnet using Python.

## Overview

**BNBChainTestnet** is a Python script designed to automate the process of requesting testnet BNB tokens from the [Chainlink Faucet](https://faucets.chain.link/). This is useful for developers and testers who need a streamlined way to obtain testnet tokens for development and QA purposes.

## Features

- Automates the process of requesting BNB testnet tokens
- Uses browser automation for interacting with the faucet site
- Simple and easy-to-use Python script

## Prerequisites

- Python 3.7+
- [pip](https://pip.pypa.io/en/stable/)
- [pyppeteer](https://github.com/pyppeteer/pyppeteer) (for browser automation)

## Installation

Clone this repository:

```bash
git clone https://github.com/borilliano/BNBChainTestnet.git
cd BNBChainTestnet
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not present, install `pyppeteer` manually:

```bash
pip install pyppeteer
```

## Usage

1. Edit `bnb.py` and set your BNB Chain testnet wallet address.
2. Run the script:

```bash
python bnb.py
```

The script will open a browser window, navigate to the Chainlink Faucet, and attempt to request BNB testnet tokens for your address.

## Notes

- **Wallet Connection:** Full automation of wallet connection (e.g., MetaMask) is not included due to security and complexity concerns.
- **Selectors:** If the faucet website changes its layout, you may need to update the selectors in `bnb.py`.
- **Responsible Use:** Please use this tool responsibly and do not abuse public faucet resources.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


---
