## Purpose
Menambahkan kemampuan bagi model properti yang sudah ada untuk menyimpan informasi nilai tanda jadi (booking fee), daftar reservasi terkait, dan memiliki status khusus saat dipesan oleh klien.

## ADDED Requirements

### Requirement: Atribut Pemesanan Properti
The system MUST menyimpan informasi nilai uang tanda jadi (booking fee) yang dibutuhkan untuk memesan sebuah properti, beserta referensi daftar reservasi yang terkait.
> **Reference:** [TSD](../../../../../docs/01-estate_booking/tsd.md) — Bagian 3.2

#### Scenario: Menentukan nilai pemesanan
- **WHEN** agen properti membuat atau memperbarui properti
- **THEN** sistem memungkinkan agen untuk menginput nilai uang (Monetary) ke dalam kolom `booking_fee`

### Requirement: Status Dipesan pada Properti
The system MUST mendukung perubahan status properti menjadi "dipesan" (reserved) ketika proses reservasi telah dikonfirmasi, untuk mencegah pemesanan ganda.
> **Reference:** [TSD](../../../../../docs/01-estate_booking/tsd.md) — Bagian 3.2

#### Scenario: Reservasi sukses
- **WHEN** sebuah dokumen reservasi terhadap properti berhasil dikonfirmasi
- **THEN** status properti berubah menjadi "dipesan" sehingga tidak dapat dipesan ulang oleh pengguna lain
