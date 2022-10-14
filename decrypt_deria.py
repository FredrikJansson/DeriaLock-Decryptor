import sys
import hashlib
from Crypto.Cipher import AES

PWD = "b3f6c3r6vctb9c3n789um83zn8c3tb7c3brc3b5c77327tbrv6b123rv6c3rb6c7tc3n7tb6tb6c3t6b35nt723472357t1423tb231br6c3v4"

def calculate_key_n_iv(pwd = PWD):
    b = bytearray()
    b.extend(map(ord, pwd))
    hash = hashlib.sha512(b)
    dig = hash.digest()
    key = dig[0:32]
    iv = dig[32:48]
    return key, iv


def decrypt_file(enc_file, new_file):
    key, iv = calculate_key_n_iv()
    bs = AES.block_size
    cipher = AES.new(key, AES.MODE_CBC, iv)
    nb = ""
    eof = False
    with open(enc_file, "rb") as inf:
        with open(new_file, "wb") as outf:
            while eof is False:
                next_r = inf.read(1024 * bs)
                b = nb
                nb = cipher.decrypt(next_r)
                if len(nb) == 0:
                    pl = b[-1]
                    b = b[:-pl]
                    eof = True
                if b:
                    outf.write(b)
    print(f"Decrypted {enc_file} to {new_file}.")



def main():
    if len(sys.argv) != 3:
        print("Args need to be: python3 decrypt_deria.py encrypted_file new_decrypted_file")
        exit(1)
    
    decrypt_file(sys.argv[1], sys.argv[2])
    
    
if __name__ == "__main__":
    main()