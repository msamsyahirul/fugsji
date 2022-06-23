  class Hewan:
    def __init__(self,nama):
        self.nama = nama
    def gerak(self):
        print('gerak-gerak!!!')

class HewanDarat(Hewan):
    def __init__(self,nama,kaki=0):
        super().__init__(nama)   
        self.kaki = kaki         
        
    def gerak(self):            
        print(self.nama,'gerak di darat dengan kaki',self.kaki)

class HewanAir(Hewan):
    def __init__(self,nama,sirip='kecil'):
        super().__init__(nama)   
        self.sirip = sirip      
        
    def gerak(self):  
        print(self.nama,'gerak di air dengan sirip', self.sirip)

hewan = Hewan('pokoknya hewan')
kambing = HewanDarat('kambing',kaki=4)
hiu = HewanAir('hiu',sirip='lebar')

hewan.gerak()
kambing.gerak()
hiu.gerak()