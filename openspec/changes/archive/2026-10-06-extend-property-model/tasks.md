## 1. Persiapan File Python
- [x] 1.1 Membuat folder `models` di dalam `addons/estate_booking/`.
- [x] 1.2 Membuat file `models/__init__.py` dan mendaftarkannya pada root `__init__.py`.
- [x] 1.3 Membuat file `models/estate_property.py` dan mendaftarkannya pada `models/__init__.py`.

## 2. Implementasi Inheritance
- [x] 2.1 Mendeklarasikan class yang melakukan inheritance terhadap `estate.property` menggunakan `_inherit` di `models/estate_property.py`.
- [x] 2.2 Menambahkan field `booking_fee` bertipe `fields.Float` pada class tersebut.
- [x] 2.3 Menambahkan opsi `('reserved', 'Dipesan')` pada field `status` dengan menggunakan atribut `selection_add` dan `ondelete={'reserved': 'set default'}`.
