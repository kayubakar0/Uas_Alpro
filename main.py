from pajak import *

def main():
    jml_orang = int(input("masukkan jumlah orang yang bayar: "))
    orang = []
    urutan = 1
    for m in range(jml_orang):
        print("Warga ke - ", urutan)
        urutan += 1

        nama = input("Masukkan Nama = ")
        NIP = input("Masukkan NIP = ")
        Status = input("Masukkan Status (1.Bujangan, 2.menikah tanpa anak, 3.menikah punya anak) = ")
        Peghasilanperbulan = int(input("masukkan Penghasilan Per Bulan = "))
        if Status == "3":
            jumlah_anak = int(input("masukkan banyak anak : "))
        else :
            jumlah_anak =  0

        Detail_pajak = pajak(nama, NIP, Status, Peghasilanperbulan, jumlah_anak)
        #membuat Objek

        orang.append(Detail_pajak)
        print("")

    #READ
    urutan = 1
    for m in orang:
        print("""
        -----------------{}---------------------
        Nama             : {}
        NIP              : {}
        Pajak            : Rp {}
        -----------------------------------------
        """.format(urutan, m.nama, m.NIP, m.Hitung_Pajak()))
        urutan += 1
    
    #Delete
    pil = input("Apakah ingin menghapus data(y/n)? ")
    if(pil=='y' or pil=='Y'):
        pilU = int(input("nomor urut berapa? "))
        del orang[pilU-1]
    else:
        print("Data pajak tidak berubah")
    
    #READ
    for m in orang:
        print("""
        Nama             : {}
        NIP              : {}
        Pajak            : Rp {}
        """.format(m.nama, m.NIP, m.Hitung_Pajak()))

if __name__ == '__main__':
    main()

