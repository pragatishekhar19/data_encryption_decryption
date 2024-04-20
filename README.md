# AES Encryption with Python

This Python script provides a simple yet secure method for AES encryption and decryption using the `Crypto` library. It allows users to encrypt sensitive messages with a password and decrypt them when needed. Additionally, it provides an option to save the encrypted data to a file for future retrieval.

## Features

- **Secure Encryption**: Utilizes the AES encryption algorithm with Cipher Block Chaining (CBC) mode for secure message encryption.
- **Password Protection**: Prompts the user to input a password securely using the `getpass` module, ensuring the password remains hidden.
- **User-Friendly Interface**: Guides the user through the encryption and decryption process with clear prompts and instructions.
- **Option to Save Data**: Allows users to optionally save the encrypted data to a binary file for later use.

## Usage

1. **Installation**: Ensure you have Python 3.x installed on your system. Install the required libraries using pip:
   ```bash
   pip install pycryptodome
   ```

2. **Running the Script**: Execute the script `aes_encryption.py` in your preferred Python environment.

3. **Encryption**:
   - Enter a strong password when prompted.
   - Input the message you wish to encrypt.
   - Choose whether you want to see the encrypted message.

4. **Decryption**:
   - If you choose to see the encrypted message, enter the password again to decrypt and view the message.
   - If you choose not to see the encrypted message, decide whether to save the encrypted data to a file.

5. **Saving Encrypted Data**: Optionally save the encrypted data to a file by choosing 'Yes' when prompted.

## Notes

- Ensure you have the `Crypto` library installed (`pip install pycryptodome`) before running the script.
- It's crucial to use a strong and memorable password for encryption to maintain the security of your data.
- Keep your password secure and do not share it with others.
- For additional security, consider storing the encrypted data in a secure location.
