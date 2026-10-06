# Odoo Estate Booking — OpenSpec Changes Plan

| Field              | Value                                         |
|--------------------|-----------------------------------------------|
| **Document ID**    | ODOO-ESTATE-OPENSPEC-01                       |
| **Version**        | 1.0                                           |
| **Status**         | Active                                        |
| **Effective Date** | 2026-10-06                                    |
| **Authors**        | Gilang Khrismahaq                             |

**Tujuan Dokumen:**
Dokumen ini memecah kebutuhan sistem Estate Booking (Spesifikasi: `tsd.md`) secara menyeluruh (A–Z) ke dalam unit *capabilities* dan *changes* yang dapat dieksekusi secara independen menggunakan kerangka OpenSpec. Setiap *change* merujuk langsung ke Spesifikasi Sistem (SSOT).

---

## Fase 1: Perluasan Model Data (Backend)

### 1.1 Capability: `property-booking-models`
Pembuatan model data inti untuk mencatat reservasi dan jadwal pembiayaan.

| Nama Change | Domain | Deskripsi | Referensi SSOT |
|---|---|---|---|
| `extend-property-model` | Backend | Modifikasi model `estate.property` dengan penambahan field `booking_fee`, `booking_ids`, dan status `reserved`. | [tsd.md](tsd.md) (Bagian 3.2) |
| `create-booking-model` | Backend | Pembuatan model baru `estate.booking` beserta fields, states, dan relasinya (`draft`, `waiting_payment`, `confirmed`, `canceled`). | [tsd.md](tsd.md) (Bagian 3.2) |
| `create-installment-model` | Backend | Pembuatan model baru `estate.installment` untuk mencatat jadwal cicilan pelanggan per bulan. | [tsd.md](tsd.md) (Bagian 3.2) |
| `setup-booking-security` | Security | Konfigurasi `ir.model.access.csv` dan `security.xml` untuk model *booking* dan *installment* (Portal User = Read Own, Internal = Full Access). | [tsd.md](tsd.md) (Bagian 3.4) |

---

## Fase 2: Antarmuka Publik (Web Portal)

### 2.1 Capability: `portal-property-catalog`
Pembuatan antarmuka publik bagi klien untuk menelusuri katalog properti.

| Nama Change | Domain | Deskripsi | Referensi SSOT |
|---|---|---|---|
| `ui-property-catalog` | Frontend | Pembuatan Odoo Controller `/properties` dan template QWeb untuk menampilkan daftar properti yang berstatus *New*. | [tsd.md](tsd.md) (Bagian 3.5) |
| `ui-property-detail` | Frontend | Pembuatan Odoo Controller `/property/<id>` untuk menampilkan foto, spesifikasi, harga, dan tombol "Book Now". | [tsd.md](tsd.md) (Bagian 2.2) |
| `ui-booking-checkout` | Frontend | Pembuatan alur *checkout* untuk inisiasi registrasi dan konfirmasi pemesanan sebelum diarahkan ke *Payment Gateway*. | [tsd.md](tsd.md) (Bagian 2.2) |

---

## Fase 3: Integrasi Sistem Pembayaran

### 3.1 Capability: `payment-gateway-integration`
Menghubungkan proses pemesanan dengan *Payment Engine* bawaan Odoo.

| Nama Change | Domain | Deskripsi | Referensi SSOT |
|---|---|---|---|
| `integrate-payment-transaction` | Integrasi | Menghasilkan referensi `payment.transaction` ketika tombol "Book Now" diklik dan mengarahkan pengguna ke *Test Provider* Odoo. | [tsd.md](tsd.md) (Bagian 3.5) |
| `webhook-payment-callback` | Backend | Menangkap notifikasi dari Gateway (via metode `_process_notification_data()`) untuk memvalidasi pembayaran "SUKSES". | [tsd.md](tsd.md) (Bagian 3.3) |
| `automate-state-transitions` | Backend | Secara otomatis mengubah status `estate.property` menjadi `reserved` dan `estate.booking` menjadi `confirmed` setelah menerima sinyal *webhook* pembayaran. | [tsd.md](tsd.md) (Bagian 3.3) |

---

## Fase 4: Otomatisasi Akuntansi dan Portal Klien

### 4.1 Capability: `installment-invoicing`
Pembuatan tagihan cicilan berkala secara otomatis.

| Nama Change | Domain | Deskripsi | Referensi SSOT |
|---|---|---|---|
| `automate-installment-drafts` | Backend | Meng-*generate* deretan baris `estate.installment` secara otomatis berdasarkan jumlah termin sesaat setelah pembayaran uang muka (*DP/Booking Fee*) terkonfirmasi lunas. | [tsd.md](tsd.md) (Bagian 2.2) |
| `integrate-customer-invoices` | Integrasi | Memicu Odoo untuk menerbitkan draf *Customer Invoice* (`account.move`) untuk setiap entitas `estate.installment` yang jatuh tempo. | [tsd.md](tsd.md) (Bagian 3.2) |
| `ui-customer-portal-invoices` | Frontend | Mengekspos tagihan cicilan ke dalam portal pelanggan Odoo bawaan (`/my/invoices`) agar klien dapat meninjaunya secara independen. | [tsd.md](tsd.md) (Bagian 2.2) |
