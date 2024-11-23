# ⚡ TagLis - Pengecekan Tagihan Listrik Sederhana & Cepat ⚡
![TagLis](https://github.com/user-attachments/assets/cb3e80c3-3915-46ee-8111-58fe18f7edb8)

**TagLis** adalah aplikasi berbasis web yang dirancang untuk memudahkan pengguna dalam mengecek tagihan listrik mereka secara cepat, aman, dan user-friendly. Dengan antarmuka yang bersih dan fitur canggih, Anda hanya memerlukan ID Pelanggan untuk melihat informasi tagihan terbaru.

## 🚀 Fitur Utama
- **Cek Tagihan Cepat**: Hanya dengan memasukkan ID Pelanggan, dapatkan informasi lengkap tagihan listrik Anda.
- **Antarmuka Responsif**: Menggunakan Tailwind CSS untuk pengalaman pengguna yang optimal di semua perangkat.
- **Keamanan Data**: Data pelanggan dijaga dengan baik dan tidak disimpan oleh aplikasi.
- **Notifikasi Dinamis**: Pemberitahuan instan saat input tidak valid atau saat data berhasil diproses.
- **Modal FAQ Interaktif**: Menyediakan jawaban atas pertanyaan umum untuk membantu pengguna memahami aplikasi.

## 📦 Instalasi
1. **Kloning Repository**:
    ```bash
    git clone https://github.com/RozhakXD/TagLis.git
    cd TagLis
    ```
2. **Instalasi Dependensi**:
    ```bash
    pip install -r requirements.txt
    ```
3. **Konfigurasi Django**:
   - Atur `settings.py` sesuai dengan kebutuhan Anda, termasuk konfigurasi database dan STATICFILES_DIRS.
5. **Migrasi Database**:
    ```bash
    python manage.py migrate
    ```
6. **Menjalankan Server**:
    ```bash
    python manage.py runserver
    ```
6. **Akses Aplikasi**: Buka [http://localhost:8000](http://localhost:8000) di browser Anda.

## 💡 Cara Menggunakan TagLis
- Buka halaman utama TagLis.
- Masukkan ID Pelanggan atau Bill Number Anda di kolom input.
- Klik tombol "Cek Tagihan".
- Informasi tagihan Anda akan ditampilkan secara instan.

## 🛠️ Teknologi yang Digunakan
- Frontend: Tailwind CSS
- Backend: Django (Python)
- API: Custom RESTful API untuk validasi tagihan
- Notifikasi: JavaScript dengan efek dinamis

## 🖼️ Tangkapan Layar
![FunPic_20241123_131615122](https://github.com/user-attachments/assets/3a7f095a-c161-48e6-8430-df34932ddafc)

## 🌟 Kontribusi
Kami terbuka untuk kontribusi dari siapa saja! Jika Anda menemukan bug atau memiliki ide fitur baru, silakan buat issue atau pull request di repository ini.

## ☕ Dukung Kami
Jika TagLis bermanfaat bagi Anda, pertimbangkan untuk mendukung pengembangan aplikasi ini: [Trakteer Kami](https://trakteer.id/rozhak_official/tip)

## 📄 Lisensi
Proyek ini dilisensikan di bawah MIT License. Lihat [LICENSE](https://github.com/RozhakXD/TagLis/blob/main/LICENSE) untuk informasi lebih lanjut.
