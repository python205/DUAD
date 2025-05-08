

def sort_song_names(input_file, output_file):
    try:
        
        with open(input_file, 'r', encoding='utf-8') as file:
            songs = file.readlines()

        
        cleaned_songs = [song.strip() for song in songs]
        cleaned_songs.sort()

        
        with open(output_file, 'w', encoding='utf-8') as file:
            for song in cleaned_songs:
                file.write(song + '\n')

        print(f"Songs were sorted and saved to '{output_file}' successfully.")

    except FileNotFoundError:
        print(f"The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

#
sort_song_names("songs_input.txt", "songs_sorted.txt")

