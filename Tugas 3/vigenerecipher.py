def char_to_num(c):
    """Mengubah karakter A-Z menjadi 0-25."""
    return ord(c.upper()) - ord('A')

def num_to_char(n):
    """Mengubah angka 0-25 menjadi karakter A-Z."""
    return chr((n % 26) + ord('A'))

def vigenere_encrypt(plaintext, key):
    """Enkripsi Vigenere Cipher: Kunci diulang sepanjang Plaintext."""
    plaintext = plaintext.upper().replace(" ", "")
    key = key.upper().replace(" ", "")
    
    # Pengulangan kunci secara periodik
    full_key = (key * ((len(plaintext) // len(key)) + 1))[:len(plaintext)]
    
    ciphertext = []
    print("--- PROCESS VIGENERE CIPHER ---")
    print(f"PT  : {list(plaintext)}")
    print(f"n(PT): {[char_to_num(p) for p in plaintext]}")
    print(f"K   : {list(full_key)}")
    print(f"n(K) : {[char_to_num(k) for k in full_key]}")
    
    for p, k in zip(plaintext, full_key):
        c_num = (char_to_num(p) + char_to_num(k)) % 26
        ciphertext.append(num_to_char(c_num))
        
    res = "".join(ciphertext)
    print(f"CT  : {list(res)}\n")
    return res

def autokey_encrypt(plaintext, key):
    """Enkripsi Autokey Cipher: Kunci diawali key awal lalu disambung Plaintext."""
    plaintext = plaintext.upper().replace(" ", "")
    key = key.upper().replace(" ", "")
    
    # Pembentukan Autokey (Key awal + sisa dari Plaintext)
    auto_key = (key + plaintext)[:len(plaintext)]
    
    ciphertext = []
    print("--- PROCESS AUTOKEY CIPHER ---")
    print(f"PT  : {list(plaintext)}")
    print(f"n(PT): {[char_to_num(p) for p in plaintext]}")
    print(f"K   : {list(auto_key)}")
    print(f"n(K) : {[char_to_num(k) for k in auto_key]}")
    
    for p, k in zip(plaintext, auto_key):
        c_num = (char_to_num(p) + char_to_num(k)) % 26
        ciphertext.append(num_to_char(c_num))
        
    res = "".join(ciphertext)
    print(f"CT  : {list(res)}\n")
    return res

# --- EKSEKUSI TUGAS 1 ---
plaintext = "ASPRAKGANTENG"
key = "REYHANFACHRUROZI"

print("========================================")
print(f"PLAINTEXT : {plaintext}")
print(f"KEY       : {key}")
print("========================================\n")

vigenere_result = vigenere_encrypt(plaintext, key)
autokey_result = autokey_encrypt(plaintext, key)

print(f"Hasil Vigenere Cipher : {vigenere_result}")
print(f"Hasil Autokey Cipher  : {autokey_result}")