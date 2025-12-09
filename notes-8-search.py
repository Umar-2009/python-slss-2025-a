# Into to Search
# Author: Umar Hassan
# 25 November

import csv

# Introduction to Search Algorithms
# Search for all songs by "Gunna"
# Display all YouTube and TikTok views
# Sort by either YouTube or TikTok views


def main():
    artist = "Gunna"  # artist to find
    track_col = 0
    artist_col = 2
    yt_views_col = 11
    tiktok_views_col = 15
    explicit_col = 8

    # open the file
    with open("data/spotify2024.csv") as f:
        # get rid of the header
        _ = f.readline()

        # create a csv reader
        r = csv.reader(f)

        gunna_songs = []
        clean_songs = []

        # read each line of data
        for info in r:
            if artist == info[artist_col]:
                gunna_songs.append(info)

                if info[explicit_col].lower() == "false":
                    clean_songs.append(info)

        # print how many songs are in the list
        print(f"Number of Gunna Songs: {len(gunna_songs)}")
        print(f"\nNon-Explicit {artist} Songs: {len(clean_songs)}\n")

        for song in clean_songs:
            print(f"Track: {song[track_col]}")
            print(f"YouTube Views: {song[yt_views_col]}")
            print(f"TikTok Views: {song[tiktok_views_col]}")
            print("-" * 40)


if __name__ == "__main__":
    main()
