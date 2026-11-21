
from typing import NamedTuple


class TIMESTAMP(NamedTuple):
    weekday: str
    hour: str
    consumption: float
    price: float
    total: float


def readTimestamps(PfileName, Ptimestamps):

    print(f'Reading file "{PfileName}".')

    solidFile = open(PfileName, "r", encoding="utf-8")

    solidFile.readline()  # Skip header

    for line in solidFile:

        line = line.strip()

        if line == "":
            continue

        parts = line.split(";")

        weekday = parts[0]
        hour = parts[1]
        consumption = float(parts[2])
        price = float(parts[3])

        total = consumption * price

        timestamp = TIMESTAMP(
            weekday,
            hour,
            consumption,
            price,
            total
        )

        Ptimestamps.append(timestamp)

    solidFile.close()

    return Ptimestamps


def displayTimestamps(Ptimestamps):

    print("Electricity usage:")

    for timestamp in Ptimestamps:

        print(
            f" - {timestamp.weekday} {timestamp.hour}, "
            f"price {timestamp.price:.2f} €, "
            f"consumption {timestamp.consumption:.2f} kWh, "
            f"total {timestamp.total:.2f} €"
        )


def main():

    print("Program starting.")

    fileName = input("Insert filename: ")

    timestamps = []

    readTimestamps(fileName, timestamps)

    displayTimestamps(timestamps)

    print("Program ending.")


if __name__ == "__main__":
    main()
