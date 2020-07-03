class pajak(object):
    "aplikasi pencatat pajak"
    def __init__(self, nama, NIP, Status, PenghasilanPerBulan, anak):
        self.nama = nama
        self.NIP = NIP
        self.Status = Status
        self.PenghasilanPerBulan = PenghasilanPerBulan
        self.anak = anak
    
    def PTKP(self):
        PenghasilanPerTahun = self.PenghasilanPerBulan * 12
        if self.Status == "1" and PenghasilanPerTahun > 54000000:
            return 54000000
        elif self.Status == "2" and PenghasilanPerTahun > 58500000 :
            return 58500000
        elif self.Status == "3":
            pajak_anak = self.anak * 4500000
            if PenghasilanPerTahun > (58500000 + pajak_anak):
                return (58500000 + pajak_anak)
            else:
                return 0
        else:
            return 0
    
    def PKP(self):
        PenghasilanPerTahun = self.PenghasilanPerBulan * 12
        if  self.PTKP() != 0:
            return (PenghasilanPerTahun - self.PTKP())
        else:
            return 0
    
    def PPh(self):
        pkp = self.PKP()
        if pkp < 50000000:
            return 5/100
        elif pkp > 50000000 and pkp < 250000000 :
            return 15/100
        elif pkp > 250000000 and pkp < 500000000 :
            return 25/100
        else:
            return 50/100
    
    def Hitung_Pajak(self):
        return int(self.PKP() * self.PPh())


