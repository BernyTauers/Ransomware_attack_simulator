# Ransomware Simulator (Educational)

This project is a **simulator** of ransomware using AES encryption, designed for **educational purposes only**. It mimics how a real ransomware attack works by encrypting files and changing their extensions to `.locked`.

##  What This Project Does
- **Encrypts** files in a specified directory.
- Changes their extensions to `.locked` to mark them as encrypted.
- Saves encryption keys, nonce, and tag in a `keys.txt` file for educational purposes.

##  Technologies Used
- **Python**: Main language used for encryption.
- **AES (Advanced Encryption Standard)**: Symmetric encryption for securing files.
- **Cryptodome**: Used for cryptography and AES implementation.
- **shutil**: To copy files before encryption (creating backups).
- **os**: File system manipulation and directory handling.

##  How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ransomware-simulator.git
   cd ransomware-simulator
