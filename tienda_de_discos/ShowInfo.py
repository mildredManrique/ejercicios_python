class Album:
    def __init__(self, title, artist, genre, price):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.price = price
    
    def show_info(self):
        print(f"{self.title} by {self.artist} - Genre: {self.genre} - Price: ${self.price}")
    
album1 = Album("Lover", "Taylor Swift", "Pop", 18.99)
album1.show_info() 