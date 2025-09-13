def create_sorted_song_list_file(path1, path2):
    song_list = []

    with open(path1) as file:
        for song in file.readlines():
            song_list.append(song)
    
    song_list.sort()

    with open(path2, "w") as file:
        for song in song_list:
            file.write(song)

    with open(path2) as file:
        print(file.read())

if __name__ == "__main__":
    create_sorted_song_list_file('top_10_songs_2000.txt', 'top_10_songs_2000_sorted.txt')