from models.song import Song


def load_songs():
    songs = []

    try:
        with open("songs.txt", "r") as file:
            for line in file:
                title, bpm, key, duration = line.strip().split(",")
                song = Song(title, int(bpm), key, int(duration))
                songs.append(song)

    except FileNotFoundError:
        print("⚠️ No file found, starting fresh")

    return songs


def save_songs(songs):
    with open("songs.txt", "w") as file:
        for song in songs:
            file.write(f"{song.title},{song.bpm},{song.key},{song.duration}\n")