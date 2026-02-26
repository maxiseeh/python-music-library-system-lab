# Music Library System Lab

## What This Project Does

This is a simple music library system that keeps track of songs. It counts how many songs we have, what genres and artists exist, and how many songs each artist and genre has.

## The Song Class

I built a `Song` class that:
- Stores song name, artist, and genre
- Counts total songs created
- Keeps a list of all unique artists
- Keeps a list of all unique genres  
- Counts how many songs per genre
- Counts how many songs per artist

## How It Works

When you create a new song, it automatically:
1. Saves the song's name, artist, and genre
2. Adds 1 to the total song count
3. Adds the genre to the list (if it's new)
4. Adds the artist to the list (if it's new)
5. Updates the genre count
6. Updates the artist count

## Example

```python
song1 = Song("99 Problems", "Jay Z", "Rap")
song2 = Song("Halo", "Beyonce", "Pop")

print(Song.count)  # Shows: 2
print(Song.genres)  # Shows: ['Rap', 'Pop']
print(Song.artists)  # Shows: ['Jay Z', 'Beyonce']
```

## Testing

All tests pass! ✅

Run tests with:
```bash
pipenv install
pipenv run pytest lib/testing/song_test.py -v
```

## Screenshot

![All Tests Passing](screenshot.png)

## What I Learned

- How to use class attributes to share data between all objects
- How to use class methods to work with class-level data
- How to make sure lists only have unique items (no duplicates)
- How to count things using dictionaries

## Files

- `lib/song.py` - Main Song class code
- `lib/testing/song_test.py` - Tests for the Song class
