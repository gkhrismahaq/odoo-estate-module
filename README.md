# Odoo 17 Custom ERP Development
**Property Management & E-Commerce Integration System**

Repositori ini berisi serangkaian modul kustom yang dikembangkan untuk Odoo 17, dirancang menggunakan arsitektur terisolasi (Docker & Docker Compose). Proyek ini berfokus pada pengembangan sistem manajemen properti terpadu, mencakup pencatatan inventaris internal (back-office) hingga integrasi e-commerce dan sistem pembiayaan.

---

## Struktur Modul

Proyek ini mengadopsi arsitektur modular berstandar industri untuk memastikan skalabilitas dan isolasi fungsionalitas.

### 1. Modul Inti: estate
Modul fundamental untuk operasional dan manajemen data master properti.
- Manajemen inventaris properti, hierarki tipe, dan pelabelan.
- Pencatatan dan pengelolaan siklus penawaran harga.
- Implementasi validasi integritas data (Python & SQL Constraints).

### 2. Modul Ekstensi: estate_booking
Modul lanjutan yang menghubungkan data operasional dengan ekosistem finansial dan interaksi klien.
- Web Portal: Antarmuka publik bagi klien untuk menelusuri katalog dan melakukan reservasi.
- Payment Integration: Integrasi mesin pembayaran Odoo untuk otorisasi pembayaran uang muka (Booking Fee).
- Installment System: Otomatisasi pembentukan jadwal pembiayaan yang terhubung langsung dengan modul akuntansi untuk penerbitan tagihan berkala.

---

## Infrastruktur Teknologi
- Sistem ERP: Odoo 17.0
- Basis Data: PostgreSQL 15
- Deployment: Docker & Docker Compose
- Utilitas Build: Makefile