def validasi_obat(nama, harga, stok):
    """Cek input obat, error kalau salah."""
    if not nama.strip():
        raise ValueError("Nama wajib diisi")
    if harga < 0:
        raise ValueError("Harga tidak boleh negatif")
    if stok < 0:
        raise ValueError("Stok tidak boleh negatif")
    
