# Facebook 2FA TOTP Generator

This Python script fetches the Time-based One-Time Password (TOTP) for applying 2FA on a Facebook account. Provide the secret key, and the script will retrieve the corresponding code from a dedicated website.

Created for fun and learning purposes.

## Highlight Features

- Simple and easy to use
- Efficient TOTP generation
- Error handling for request and response issues

## Installation

1. Download the `2fa_code.py` file from this repository.

2. Install the required dependencies:

```bash
pip install requests 
```

## Usage

```bash
from 2fa_code import GetCode 

key = "12345"
code = GetCode(key).apply()

print(f"The 2FA TOTP code is: {code}")
```
