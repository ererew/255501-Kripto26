Muhammad Reyhan Fachrurozi
140810255501

# Vigenère Cipher & Autokey Cipher
---

## 🛠️ Penjelasan Alur Program

1. **Pemetaan Karakter ke Angka (`char_to_num` & `num_to_char`)**
   * Mengubah huruf alfabet menjadi indeks angka berbasis $A=0, B=1, \dots, Z=25$.
   * Fungsi sebaliknya mengubah nilai numerik modulo 26 kembali ke bentuk karakter alfabet.

2. **Pembentukan Kunci (*Key Generation*)**
   * **Vigenère Cipher (`vigenere_encrypt`):** Kunci diulang secara periodik menggunakan teknik pemotongan string (`[:len(plaintext)]`) agar panjangnya sama persis dengan panjang *plaintext*.
   * **Autokey Cipher (`autokey_encrypt`):** Kunci awal digabungkan dengan karakter *plaintext* asli di belakangnya untuk membentuk rantai kunci (*autokey*) sepanjang *plaintext*.

3. **Proses Enkripsi**
   * Melakukan iterasi berpasangan antara *plaintext* dan *key* menggunakan fungsi `zip()`.
   * Menghitung nilai *ciphertext* menggunakan rumus aritmatika modular:
     $$C_i = (P_i + K_i) \bmod 26$$
   * Menggabungkan karakter hasil kalkulasi ke dalam variabel string *ciphertext*.

![Screenshot Running Program](./Tugas%203/screenshot.png)
