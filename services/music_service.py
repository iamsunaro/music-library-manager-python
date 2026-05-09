from models.song import Song
from storage.storage import save_songs


# =========================
# Validation Functions
# =========================
def get_valid_number(prompt, error_message):
    try:
        number = int(input(prompt))

        if number <= 0:
            print("❌ Number must be greater than 0")
            return None

        return number

    except ValueError:
        print(error_message)
        return None


# =========================
# Display Functions
# =========================
def display_song(song):
    print("\n----- Song -----")
    print(f"Title: {song.title}")
    print(f"BPM: {song.bpm}")
    print(f"Key: {song.key}")
    print(f"Duration: {song.get_duration_formatted()}")
    print(f"Energy Level: {song.get_energy()}")
    print("---------------------")


# =========================
# Song Management Functions
# =========================
def create_song(song_title, bpm, key, duration):
    return Song(song_title, bpm, key, duration)


def add_song(songs, song):
    songs.append(song)
    save_songs(songs)


def view_songs(songs):
    if not songs:
        print("⚠️ Playlist is empty. Add some songs!")
    else:
        print(f"\n🎵 Total Songs: {len(songs)}")

        for song in songs:
            display_song(song)


def song_exists(songs, song_title):
    for song in songs:
        if song.is_title(song_title):
            return True

    return False


def search_song(songs):
    search_title = input("Enter song title to search: ").strip()
    found = False

    for song in songs:
        if song.matches_title(search_title):
            display_song(song)
            found = True

    if not found:
        print("❌ Song not found")


def delete_song(songs):
    title_to_delete = input("Enter song title to delete: ").strip()
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


def update_song_details(song):
    new_bpm = get_valid_number("New BPM: ", "❌ Invalid BPM")
    if new_bpm is None:
        return False

    new_key = input("New Key: ").strip()

    new_duration = get_valid_number("New Duration: ", "❌ Invalid duration")
    if new_duration is None:
        return False

    song.bpm = new_bpm
    song.key = new_key
    song.duration = new_duration

    return True


def edit_song(songs):
    title_to_edit = input("Enter song title to edit: ").strip()
    found = False

    for song in songs:
        if song.is_title(title_to_edit):
            print("Enter New Values:")

            updated = update_song_details(song)

            if not updated:
                return

            save_songs(songs)

            print("✅ Song updated successfully!")
            found = True
            break

    if not found:
        print("❌ Song not found")