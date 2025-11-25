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

    # open the file
    with open("data/spotify2024.csv") as f:
        # get rid of the header
        _ = f.readline()

        # create a csv reader
        r = csv.reader(f)

        gunna_songs = []

        # read each line of data
        for info in r:
            if artist == info[artist_col]:
                gunna_songs.append(info)

        # print how many songs are in the list
        print(f"Number of Gunna Songs: {len(gunna_songs)}")


if __name__ == "__main__":
    main()
