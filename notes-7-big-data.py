def main():
    # Get the file
    path = "data/sfu_best_cmpt120.csv"
    file = open(path)

    # Read the header row
    header_row = file.readline()

    # Counters
    uncle_fatihs = 0
    club_ilia = 0
    pizza_hut = 0

    # Read the rest of the file
    for line in file:
        line = line.strip()  # remove newline
        print(line)

        # fav pizza is in column 5 (index 4)
        info = line.split(",")
        fav_pizza = info[4].strip().lower()  # normalize case/spacing
        name = info[1]

        if fav_pizza == "uncle fatihs":
            uncle_fatihs += 1
        elif fav_pizza == "club ilia":
            club_ilia += 1
        elif fav_pizza == "pizza hut":
            pizza_hut += 1
    file.close()

    # Print results
    print("\n--- Favorite Pizza Totals ---")
    print("Uncle Fatih's:", uncle_fatihs)
    print("Club Ilia:", club_ilia)
    print("Pizza Hut:", pizza_hut)


if __name__ == "__main__":
    main()
