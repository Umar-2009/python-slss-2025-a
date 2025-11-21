# E = mc^2


def main():
    # Speed of light in meters per second
    c = 3.0e8  # 3 × 10^8 m/s

    # Ask the user for mass in kilograms
    mass = float(input("Enter mass in kilograms: "))

    # Compute energy
    energy = mass * c**2

    # Display result
    print(f"The energy equivalent of {mass} kg is {energy:.3e} joules.")


if __name__ == "__main__":
    main()
