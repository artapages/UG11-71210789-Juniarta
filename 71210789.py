class RakBuku():
    def __init__(self):
        self.size = 5
        self.data = [None] * self.size

    def getHash(self, key):
        sum = 0
        for char in str(key):
            sum += ord(char)
        return sum % self.size
    
    def probing(self, key):
        for index in range(self.size):
            probeHash = self.linearProbing(key, index)
            if (self.data[probeHash] is None) or (self.data[probeHash] == 'Deleted'):
                return probeHash
        return None

    def linearProbing(self, key, index): 
        return (self.getHash(key)+index) % self.size
    
    def tambahBuku(self, jenisBuku, namaBuku):
        hash_key = self.getHash(jenisBuku)
        key_value = [jenisBuku, namaBuku]
        if self.data[hash_key] is None:
            self.data[hash_key] = list([key_value])
            return True
        else:
            hash_key = self.probing(jenisBuku)
            if hash_key is None:
                print('Rak Buku anda sudah penuh')
                return False
        self.data[hash_key] = list([key_value])
        return False
    
    def lihatBuku(self, jenisBuku):
        hash_key = self.getHash(jenisBuku)
        if (self.data[hash_key] is not None) and (self.data[hash_key]!='deleted'):
            for index in range(self.size):
                hash_key = self.linearProbing(jenisBuku, index)
                if self.data[hash_key][0][0] == jenisBuku:
                    return self.data[hash_key][0][1]
        print('Key', jenisBuku, 'tidak ditemukan')
        return None
    
    def ambilBuku(self, jenisBuku):
        hash_key = self.getHash(jenisBuku)
        if self.data[hash_key] is None:
            return False
        for index in range(self.size):
                hash_key = self.linearProbing(jenisBuku, index)
                if self.data[hash_key][0][0] == jenisBuku:
                    print('deleting',jenisBuku)
                    self.data[hash_key] = 'deleted'
                    return True
        print('Key', jenisBuku, 'tidak ditemukan')
        return False
    
    def printAll(self):
        print('=================== List Buku ===================')
        for item in self.data:
            if (item is not None) and (item != 'deleted'):
                print('Nama :',item[0][1],'<> Jenis :',item[0][0])
        print('=================================================')

if __name__ == "__main__":
    rak1 = RakBuku()

    rak1.tambahBuku("History", "Mein Kampf (B01)")
    rak1.tambahBuku("Fantasy", "The Witcher (B02)")
    rak1.tambahBuku("Mystery", "Exile (B03)")
    rak1.tambahBuku("Sci Fi", "The Martian (B04)")
    rak1.tambahBuku("History", "World War (B05)")
    rak1.tambahBuku("Romance", "Twilight (B06)")
    
    print(rak1.lihatBuku("History"))
    print(rak1.lihatBuku("Romance"))

    rak1.ambilBuku("Sci Fi")
    rak1.ambilBuku("Romance")

    rak1.printAll()