class Album:
    def __init__(self, title, artist, genre, price):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.price = price
    
 

album1 = Album("1989", "Taylor Swift", "Pop", 19.99)
print("Album: ", album1.title)
print("Artist: ", album1.artist)
print("Genre: ", album1.genre)
print("Price: ", album1.price)

print(album1.title, "-", album1.artist, "-", album1.genre, "- $", album1.price)