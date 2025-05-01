class Store:
    def __init__(self):
        self.albums = []
    
    def add_album(self, album):
        self.albums.append(album)

store = Store()
store.add_album(album=("Fearless", "Taylore Swift", "Country", 16.30))
print("Total albums in store:", len(store.albums))