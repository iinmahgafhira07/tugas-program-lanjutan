class pegawai:
  def __init__(self, nama, gaji=0):
    self.nama = nama
    self.gaji = gaji
  def tunjangan(self, persen):
     self.gaji = self.gaji + (self.gaji * persen)
  def kerja(self):
      print(self.nama, "pekerjaannya")
  def __repr__(self, nama):
       return "<pegawai:\n nama = %s, gaji = %s" %(self.nama, self.gaji)
class koki(pegawai):
  def __init__(self, nama):
    pegawai.__init__(self, nama, 100000)
  def kerja(self):
     print(self.nama, "membuat makanan")
class pelayan(pegawai):
  def __init__(self, nama):
      pegawai.__init__(self, nama, 50000)
  def kerja(self):
      print(self.nama, "melayani costumer")
class pizzarobot(koki):
  def __inti__(self, nama):
      koki.__init__(self, nama)
  def kerja(self):
       print(self.nama, "membuat pizza")
       
if __name__ == "__man__":
   agus = pizzarobot("agus")
   print(agus)
   agus.kerja()
   agus.tunjangan(0.20)
   print(agus)
   print
   
   for kelas in pegawai, koki, pelayan, pizzarobot:
     objek = kelas(kelas.__name__)
     objek.kerja()
     
