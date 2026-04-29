from storage.storage import load_songs
from services.music_service import (
    add_song,
    view_songs,
    search_song,
    delete_song,
    edit_song
)


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
        add_song(songs)

    elif choice == "2":
        view_songs(songs)

    elif choice == "3":
        search_song(songs)

    elif choice == "4":
        delete_song(songs)

    elif choice == "5":
        edit_song(songs)

    elif choice == "6":
        print("👋 Exiting...")
        break

    else:
        print("❌ Invalid choice")