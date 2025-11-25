# Data Analysis
# Author: Umar Hassan


def main():
    filename = "nyc_central_park_weather_1869-2022.csv"

    count = 0
    rain_total = 0.0
    tmin_total = 0.0
    june_tmax_total = 0.0
    june_count = 0

    with open(filename) as f:
        header = f.readline().strip().split(",")

        date_i = header.index("DATE")
        prcp_i = header.index("PRCP")
        tmin_i = header.index("TMIN")
        tmax_i = header.index("TMAX")

        for line in f:
            parts = line.strip().split(",")

            # skip incomplete rows
            if len(parts) <= max(date_i, prcp_i, tmin_i, tmax_i):
                continue

            count += 1

            # rainfall
            prcp = parts[prcp_i]
            if prcp:
                rain_total += float(prcp)

            # minimum temp
            tmin = parts[tmin_i]
            if tmin:
                tmin_total += float(tmin)

            # extract month safely
            date = parts[date_i]
            try:
                month = date.split("-")[1]
            except:
                continue

            if month == "06":
                tmax = parts[tmax_i]
                if tmax:
                    june_tmax_total += float(tmax)
                    june_count += 1

    # compute averages
    avg_rain = rain_total / count
    avg_tmin_f = tmin_total / count
    avg_tmin_c = (avg_tmin_f - 32) * 5 / 9
    avg_june_tmax = june_tmax_total / june_count

    print("Total data points:", count)
    print("Average rainfall (in):", avg_rain)
    print("Average minimum temp (F):", avg_tmin_f)
    print("Average minimum temp (C):", avg_tmin_c)
    print("Average maximum temp in June (F):", avg_june_tmax)


if __name__ == "__main__":
    main()
