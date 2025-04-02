class Album:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
    
    def suma_dos_numeros(self, a, b):
        return a + b

album1 = Album("1989", "Taylor Swift")
print("Album: ", album1.title)
print("Artist: ", album1.artist)

print("Resultado: ", album1.suma_dos_numeros(8, 9)) 