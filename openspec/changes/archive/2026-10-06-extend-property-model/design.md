## Context
Saat ini, model `estate.property` yang ada di modul bawaan `estate` hanya mencakup data dasar properti dan status penjualan konvensional (New, Offer Received, Offer Accepted, Sold, Canceled). Untuk memfasilitasi integrasi web dan pembayaran, kita membutuhkan relasi pemesanan dan komponen biaya (lihat proposal.md).

## Goals / Non-Goals

**Goals:**
- Melakukan modifikasi pada model `estate.property` secara aman menggunakan fitur *inheritance* bawaan Odoo.
- Menambahkan field baru: `booking_fee` dan relasi balik `booking_ids` (sebagai persiapan untuk model `estate.booking` di change selanjutnya).
- Memperbarui `status` selection untuk menambahkan opsi `dipesan` / `reserved`.

**Non-Goals:**
- Membuat model `estate.booking` itu sendiri (akan dikerjakan di change terpisah `create-booking-model`).
- Membuat file view XML untuk menampilkan field ini (akan dikerjakan di `ui-backend-booking-views`).

## Decisions

### 1. Klasifikasi Inheritance `estate.property`
- **Rationale:** Kita akan menggunakan *in-place inheritance* (`_inherit = 'estate.property'`) daripada membuat tabel model turunan baru (`_name`). Ini bertujuan agar kita memodifikasi fungsionalitas asli modul `estate` di tempat tanpa harus bermigrasi data.
- **Alternatives Considered:** Menggunakan *delegation inheritance* (model baru dengan relasi many2one ke `estate.property`). Hal ini dihindari karena akan menambah kompleksitas query dan relasi untuk fitur yang sifatnya langsung melekat pada properti.

### 2. Modifikasi Selection Field Status
- **Rationale:** Odoo 17 menyediakan atribut `selection_add` pada definisi field untuk menambahkan opsi baru tanpa menimpa opsi aslinya. Kita akan menggunakan `selection_add=[('reserved', 'Dipesan')]` pada field `status` di model `estate.property`.
- **Alternatives Considered:** Menimpa ulang seluruh daftar opsi menggunakan `selection=...`. Pendekatan ini rentan menyebabkan *crash* apabila modul lain juga memodifikasi selection tersebut.

### 3. Tipe Data `booking_fee`
- **Rationale:** Sesuai standar e-commerce, field `booking_fee` bisa berupa Float (Monetary jika ada *currency_id*). Karena model dasar `estate.property` (asumsi modul dasar) umumnya menggunakan `Float` untuk `expected_price` dan `selling_price`, kita akan menggunakan `fields.Float` untuk konsistensi, atau menambah `currency_id` apabila belum ada. Untuk kesederhanaan modul awal, akan digunakan tipe `Float`.
- **Alternatives Considered:** Menggunakan tipe `Monetary`.

## Risks / Trade-offs

- **Risiko bentrokan dengan modul `estate`:** Jika nama field aslinya bukan `state` melainkan `status` atau sebaliknya, penggunaan `selection_add` akan gagal (KeyError).
  - **Mitigasi:** Kita perlu melihat definisi field aktual pada repositori `estate` sebelum mengimplementasikan `selection_add`.
- **Relasi fiktif sementara `booking_ids`:** Field `booking_ids` (One2many) memerlukan referensi ke `estate.booking`, yang belum diimplementasikan di kode.
  - **Mitigasi:** Mengingat `estate.booking` akan dibuat di *change* berikutnya, kita mungkin tidak bisa mendeklarasikan relasi `One2many` ke `estate.booking` pada change ini agar Odoo tidak *error* (Model not found). Maka dari itu, deklarasi `booking_ids` sebaiknya ditunda hingga model `estate.booking` ada, atau diimplementasikan pada file yang sama jika modelnya diinisiasi sebagai *dummy* terlebih dulu. Sebagai kompromi, change ini akan fokus pada `booking_fee` dan penambahan status `reserved` terlebih dulu, atau mendeklarasikan *dummy class* `estate.booking`.
