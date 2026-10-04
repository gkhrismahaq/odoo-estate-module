# Odoo 17 Module Development

Repositori ini adalah proyek pengembangan modul kustom untuk **Odoo 17**, yang diatur agar mudah dijalankan menggunakan **Docker**.

Saat ini, proyek ini mencakup pengembangan modul:
- **Real Estate Management (`estate`)**: Modul kustom untuk mengelola properti real estate, termasuk bangunan, apartemen, dan penyewa.

---

## Teknologi yang Digunakan

- **Odoo 17.0**
- **PostgreSQL 15**
- **Docker & Docker Compose**
- **Makefile** (untuk penyederhanaan perintah operasional)

---

## Cara Menjalankan Proyek

Proyek ini menggunakan `Makefile` agar Anda tidak perlu mengetik perintah Docker Compose yang panjang. Berikut adalah daftar perintah yang tersedia:

| Perintah | Deskripsi |
| :--- | :--- |
| `make start` | Menjalankan container Odoo dan Database (berjalan di *background*). |
| `make stop` | Menghentikan semua container. |
| `make restart` | Melakukan *restart* pada container. |
| `make console` | Membuka *Odoo shell* interaktif di dalam container. |
| `make psql` | Membuka *PostgreSQL shell* untuk mengakses database secara langsung. |
| `make logs odoo` | Menampilkan dan memantau *log* dari container Odoo. |
| `make logs db` | Menampilkan dan memantau *log* dari container database. |