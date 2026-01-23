# 🚀 Instalasi & Persiapan Flask

Sebelum memproses data Instagram, pastikan **Python** dan **Flask** sudah terpasang di komputer kamu.

---

## 🐍 1. Pastikan Python Terinstal
Cek versi Python:
```bash
python --version
```
atau:
```bash
python3 --version
```

## 2. Buat Virtual Environment

```bash
python -m venv venv
```

## 3. Aktifkan virtual environment:

### Linux / MacOS:
```bash
source venv/bin/activate

```
### Windows:
```bash
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
venv\Scripts\activate
```

## 4. install flask:
```bash
pip install flask
```
## 5. play project
```bash
python app.py
```
**buka live server http://127.0.0.1:5000**
---

# 📦 Cara Mendapatkan Data Instagram (Followers dan Following)

Panduan ini menjelaskan langkah-langkah untuk mengekspor data **followers** dan **following** dari Instagram menggunakan perangkat **HP**.

---

## 📱 Langkah-langkah di HP:

1. Buka aplikasi **Instagram**.
2. Masuk ke halaman **Profil**.
3. Ketuk ikon **garis tiga (≡)** di pojok kanan atas.
4. Pilih **Account Center**.
5. Masuk ke menu:  
   **Your Information and Permissions** ➝ **Download Your Information**.
6. Tekan **Create Export**.

---

## ⚙️ Konfigurasi Ekspor:

- Pilih akun Instagram yang ingin diekspor.
- Pilih **Export to Device**.
- Pada bagian **Customize Your Information**:
  - **Centang hanya:** `followers_and_following`
- Atur:
  - **Date Range**: `All time`
  - **Format**: `JSON`
- Tekan **Start Export**.

---

## ⏳ Tunggu Proses

- Tunggu beberapa saat hingga tombol **Download** muncul.
- Setelah selesai, unduh file yang tersedia.

---

## 🗂️ Ekstrak File

- Setelah file terunduh (dalam format ZIP), ekstrak file tersebut.
- Buka folder hasil ekstraksi hingga kamu menemukan folder bernama:  
  `followers_and_following`

---

✅ **Data siap digunakan!**  
Kamu sekarang dapat memproses data tersebut dengan script Python atau tools lain untuk menganalisis siapa yang tidak follow balik, mutuals, dan lainnya.

