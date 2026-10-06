## Why
Untuk mendukung pengembangan sistem Odoo Estate Booking, diperlukan pembuatan kerangka awal (scaffolding) modul `estate_booking`. Modul ini menjadi fondasi awal sebelum penambahan model dan fungsionalitas lain dilakukan.
> **Reference:** [TSD](../../../docs/01-estate_booking/tsd.md) — Bagian 3.1
> **Reference:** [Roadmap](../../../docs/01-estate_booking/roadmap.md) — Fase 1

## What Changes
- Pembuatan direktori utama `estate_booking`.
- Inisialisasi file wajib Odoo: `__init__.py` dan `__manifest__.py`.
- Mendaftarkan dependensi wajib pada `__manifest__.py` yaitu: `estate`, `website`, `payment`, `account`.

## Capabilities
### New Capabilities
- `module-scaffolding`: Pembuatan struktur dasar modul dan pendaftaran dependensi inti Odoo.

### Modified Capabilities

## Impact
- **Files created:**
  - `__init__.py`
  - `__manifest__.py`
- **Files modified:**
  - Tidak ada
- **SSOT documents referenced:**
  - `docs/01-estate_booking/tsd.md`
  - `docs/01-estate_booking/roadmap.md`

**Estimated effort:** 1 hours.
