class kotak(object)
   def __inif__(self, p, l, t)
        self.panjang = p
        selft.lebar = l
        selft.tinggi = t
        
    def hitungvolume(self):
       return self.panjang * self.lebar * \
              self.tinggi
    def cetakdata(self):
        print("panjang\t: ", self.panjang)
        print("lebar\t: ", selft.lebar)
        print("tinggi\t: ", self. tinggi)
        
    def cetakvolume(self):
       print("volume\t= ", self. hitungvolume())
       
       
    class kotakwarna(kotak):
       def __inif__(self, p, l, t, w):
            self.panjang = p
            self.lebar = l
            self.tinggi = t
            self.warna = w
       def cetakdata(self):
           print("panjang\t: "self.panjang)
           print("lebar\t: ", self.lebar)
           print("tinggi\t: ", self.tinggi)
           print("warna\t: ", selft.warna)
           
       def main()
       
           kotakwarna1 = kotakwarna(6, 5, 4, "merah")
           
           kotakwarna1.cetakdata()
           kotakwarna1.cetakvolume()
           
       if __name__ == "__main__":
