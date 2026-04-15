#kode perbaikan
pajak_PPN=0.11
diskon_maksimal=50000
batas_diskon=100000
def hitung_total_harga(harga_barang, jumlah_barang):
    """menghitung total harga barang beserta PPN"""
    subtotal = harga_barang * jumlah_barang
    total_pajak = subtotal * pajak_PPN
    return subtotal + total_pajak

def terapkan_diskon(total_harga):
    """memberikan diskon jika melebihi batas minimum pembelian"""
    if total_harga>batas_diskon:
        return total_harga - diskon_maksimal
    return total_harga

def cetak_struk(total_akhir,uang_bayar):
    """mencetak total tagihan dan uang kembalian"""
    kembalian = uang_bayar - total_akhir
    print(f"total bayar : Rp {total_akhir}")
    print(f"Kembalian : Rp {kembalian}")
    return kembalian
