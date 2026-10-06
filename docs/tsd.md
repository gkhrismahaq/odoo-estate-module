# Odoo Estate Booking — System Specification Document (TSD)

| Field              | Value                                         |
|--------------------|-----------------------------------------------|
| **Document ID**    | ODOO-ESTATE-TSD-01                            |
| **Version**        | 1.0                                           |
| **Status**         | Active                                        |
| **Effective Date** | 2026-10-06                                    |
| **Authors**        | Gilang Khrismahaq                             |

**Tujuan Dokumen:**
Dokumen ini merupakan Single Source of Truth (SSOT) yang merincikan spesifikasi teknis dan fungsional dari modul `estate_booking` dalam ekosistem Odoo 17. Dokumen ini menjadi rujukan utama bagi penyusunan roadmap dan pelaksanaan metode *Spec-Driven Development*.

---

## Bagian 1: Kebutuhan Bisnis

### 1.1 Ringkasan Eksekutif
Proyek ini mengembangkan modul manajemen properti internal menjadi portal publik. Sistem ini memfasilitasi klien untuk melihat katalog properti, membayar tanda jadi melalui sistem pembayaran terintegrasi, dan mengelola jadwal tagihan pembiayaan.

### 1.2 Tujuan Bisnis
- Mengotomatisasi proses penerimaan pembayaran tanda jadi.
- Membuat sistem penagihan pembiayaan yang terintegrasi secara otomatis dengan modul akuntansi.
- Menyediakan portal klien untuk transparansi riwayat transaksi.

### 1.3 Ruang Lingkup
- Integrasi katalog properti dengan modul website.
- Integrasi sistem pembayaran Odoo.
- Manajemen jadwal pembiayaan properti.
- Pembuatan tagihan otomatis pada modul akuntansi.
- Antarmuka portal klien.

---

## Bagian 2: Spesifikasi Fungsional

### 2.1 Profil Pengguna
- Pengunjung situs: Mengakses katalog properti dan mendaftarkan akun.
- Klien: Melakukan pembayaran awal dan melunasi tagihan pembiayaan rutin.
- Agen properti: Mengelola data properti dan status reservasi.
- Staf keuangan: Memverifikasi tagihan dan jurnal keuangan.

### 2.2 Alur Proses Bisnis
1. Klien mengakses halaman katalog properti.
2. Klien memilih properti dan melanjutkan ke proses pemesanan.
3. Klien melakukan pembayaran awal melalui layanan pembayaran digital.
4. Sistem menerima konfirmasi pembayaran dan secara otomatis memperbarui status properti, serta membuat jadwal pembiayaan.
5. Klien mengakses portal akun secara berkala untuk menyelesaikan tagihan lanjutan.

---

## Bagian 3: Spesifikasi Teknis

### 3.1 Ketergantungan Modul
Modul ini dibangun di atas kerangka kerja modul berikut:
- estate
- website
- payment
- account

### 3.2 Model Data

#### Perluasan model estate.property
- booking_fee (Monetary): Nilai tanda jadi.
- booking_ids (One2many): Relasi ke data reservasi.
- status (Selection): Penambahan opsi dipesan.

#### Model baru estate.booking
- name (Char): Nomor referensi dokumen.
- property_id (Many2one): Relasi properti.
- customer_id (Many2one): Relasi pembeli.
- booking_date (Date): Tanggal transaksi.
- booking_fee_paid (Monetary): Nilai pembayaran awal.
- payment_transaction_id (Many2one): Relasi riwayat transaksi pembayaran.
- installment_ids (One2many): Relasi jadwal pembiayaan.
- state (Selection): draft, waiting_payment, confirmed, canceled.

#### Model baru estate.installment
- booking_id (Many2one): Relasi dokumen reservasi.
- name (Char): Keterangan jadwal pembiayaan.
- due_date (Date): Tanggal jatuh tempo.
- amount (Monetary): Nilai tagihan.
- invoice_id (Many2one): Relasi tagihan akuntansi.
- state (Selection): unpaid, paid, late.

### 3.3 Transisi Status 
Siklus status pada dokumen reservasi meliputi:
- Draft ke Waiting Payment: Terjadi saat klien menginisiasi pembayaran.
- Waiting Payment ke Confirmed: Tereksekusi melalui validasi dari sistem pembayaran pihak ketiga.
- Confirmed ke Canceled: Dikelola oleh agen properti jika terjadi pembatalan sepihak.

### 3.4 Hak Akses
- Agen properti memiliki hak penuh membaca, membuat, mengubah, dan menghapus dokumen reservasi.
- Klien hanya memiliki hak membaca dokumen reservasi yang terhubung dengan akun portal mereka.
- Pengunjung publik diizinkan melihat katalog properti namun tidak memiliki akses ke antarmuka internal.
