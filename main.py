from storage.storage import load_songs
from services.music_service import (
    add_song,
    view_songs,
    search_song,
    delete_song,
    edit_song,
    song_exists,
    create_song,
    get_valid_number
)

print("🎵 Welcome to Music Library Manager 🎵")

songs = load_songs()

while True:
    print("\n=== MUSIC LIBRARY ===")
    print("1. Add Song")
    print("2. View Songs")
    print("3. Search Song")
    print("4. Delete Song")
    print("5. Edit Song")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        song_title = input("Enter song title: ").strip()
        if not song_title:
            print("❌ Song title cannot be empty")
            continue
        if song_exists(songs, song_title):
            print("❌ Song already exists")
            continue


        bpm = get_valid_number("Enter BPM: ", "❌ Invalid BPM")
        if bpm is None:
            continue

        key = input("Enter key: ").strip()

        duration = get_valid_number("Enter duration: ", "❌ Invalid duration")
        if duration is None:
            continue

        song = create_song(song_title, bpm, key, duration)
        add_song(songs, song)

        print("✅ Song added!")

    elif choice == "2":
        view_songs(songs)

    elif choice == "3":
        search_song(songs)

    elif choice == "4":
        delete_song(songs)

    elif choice == "5":
        edit_song(songs)

    elif choice == "6":
        print("👋 Thanks for using Music Library Manager!")
        break

    else:
        print("❌ Invalid choice")