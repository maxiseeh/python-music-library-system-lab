class Song:
    # Class attributes - shared by all songs
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # Instance attributes - unique to each song
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Call methods to update class attributes
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()

    @classmethod
    def add_song_to_count(cls):
        # Add 1 to total song count
        cls.count += 1

    def add_to_genres(self):
        # Add genre if it's not already in the list
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)

    def add_to_artists(self):
        # Add artist if it's not already in the list
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)

    def add_to_genre_count(self):
        # Count how many songs per genre
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1

    def add_to_artist_count(self):
        # Count how many songs per artist
        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] += 1
        else:
            Song.artist_count[self.artist] = 1
