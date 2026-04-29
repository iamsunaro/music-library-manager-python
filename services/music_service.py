from models.song import Song
from storage.storage import save_songs


def display_song(song):
    print("\n----- Song -----")
    print(f"Title: {song.title}")
    print(f"BPM: {song.bpm}")
    print(f"Key: {song.key}")
    print(f"Duration: {song.get_duration_formatted()}")
    print(f"Energy Level: {song.get_energy()}")
    print("---------------------")


def add_song(songs):
    title = input("Enter song title: ")

    try:
        bpm = int(input("Enter BPM: "))
    except ValueError:
        print("❌ Invalid BPM")
        return

    key = input("Enter key: ")

    try:
        duration = int(input("Enter duration: "))
    except ValueError:
        print("❌ Invalid duration")
        return

    song = Song(title, bpm, key, duration)
    songs.append(song)
    save_songs(songs)

    print("✅ Song added!")


def view_songs(songs):
    if not songs:
        print("⚠️ No songs in playlist!")
    else:
        for song in songs:
            display_song(song)


def search_song(songs):
    search_title = input("Enter song title to search: ")
    found = False

    for song in songs:
        if song.matches_title(search_title):
            display_song(song)
            found = True

    if not found:
        print("❌ Song not found")


def delete_song(songs):
    title_to_delete = input("Enter song title to delete: ")
    found = False

    for song in songs:
        if song.is_title(title_to_delete):
            songs.remove(song)
            save_songs(songs)
            print("🗑️ Song deleted successfully!")
            found = True
            break

    if not found:
        print("❌ Song not found")


def edit_song(songs):
    title_to_edit = input("Enter song title to edit: ")
    found = False

    for song in songs:
        if song.is_title(title_to_edit):
            print("Enter New Values:")

            song.bpm = int(input("New BPM: "))
            song.key = input("New Key: ")
            song.duration = int(input("New Duration: "))

            save_songs(songs)

            print("✅ Song updated successfully!")
            found = True
            break

    if not found:
        print("❌ Song not found")