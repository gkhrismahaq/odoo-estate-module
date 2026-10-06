## Why
Modul manajemen properti saat ini (estate) belum mendukung alur reservasi. Untuk memfasilitasi integrasi portal dan pembayaran, kita perlu memodifikasi model `estate.property` agar dapat menampung nilai *booking fee*, relasi terhadap daftar reservasi, serta mendukung status baru "dipesan".
> **Reference:** [Roadmap](../../../docs/01-estate_booking/roadmap.md) — Fase 2.
> **Reference:** [TSD](../../../docs/01-estate_booking/tsd.md) — Bagian 3.2.

## What Changes
- Modifikasi model data `estate.property` melalui teknik *inheritance* in-place.
- Penambahan field `booking_fee` (Monetary) untuk mencatat nilai tanda jadi pemesanan.
- Penambahan field `booking_ids` (One2many) untuk melacak daftar reservasi yang terkait.
- Penambahan opsi `dipesan` pada field selection `status`.

## Capabilities
### New Capabilities
- `property-booking-models`: Modifikasi model `estate.property` untuk penambahan field terkait reservasi dan status `reserved`/dipesan.

### Modified Capabilities

## Impact
- **Files created:**
  - `models/estate_property.py`
  - `models/__init__.py` (jika belum ada)
- **Files modified:**
  - `__init__.py` (root)
  - `__manifest__.py`
- **SSOT documents referenced:**
  - `docs/01-estate_booking/tsd.md`
  - `docs/01-estate_booking/roadmap.md`

**Estimated effort:** 2 hours.
