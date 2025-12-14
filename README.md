# praktikum-pbo-11


# Refactoring Struktur Kode Menggunakan Prinsip SOLID

## Studi Kasus
Refactoring Sistem Validasi Registrasi Mahasiswa

## Analisis Pelanggaran SOLID

### Single Responsibility Principle (SRP)
Class `ValidatorManager` memiliki lebih dari satu tanggung jawab, yaitu memvalidasi SKS dan prasyarat sekaligus. 
Hal ini menyebabkan class memiliki banyak alasan untuk berubah.

### Open/Closed Principle (OCP)
Penambahan jenis validasi baru mengharuskan perubahan pada method `validate()` menggunakan `if/else`, 
sehingga class tidak tertutup terhadap modifikasi.

### Dependency Inversion Principle (DIP)
Class utama bergantung langsung pada implementasi konkret, bukan pada abstraksi.

## Solusi Refactoring
- Membuat interface `Validator`
- Memisahkan setiap jenis validasi ke class masing-masing
- Menggunakan Dependency Injection pada `RegistrationValidator`

## Kesimpulan
Refactoring dengan prinsip SOLID menghasilkan kode yang lebih modular, fleksibel, dan mudah dikembangkan.
