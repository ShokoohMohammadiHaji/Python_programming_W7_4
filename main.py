
from typing import NamedTuple


class TIMESTAMP(NamedTuple):
    weekday: str
    hour: int
    consumption: float
    price: float


class DAY_USAGE(NamedTuple):
    weekday: str
    consumption: float
    cost: float


def readTimestamps(PfileName):
    timestamps: list[TIMESTAMP] = []

    print(f'Reading file "{PfileName}".')

    solidFile = open(PfileName, "r", encoding="utf-8")
    solidFile.readline()

    for line in solidFile:
        line = line.strip()

        if line == "":
            continue

        parts = line.split(";")

        timestamp = TIMESTAMP(
            parts[0],
            int(parts[1]),
            float(parts[2]),
            float(parts[3])
        )

        timestamps.append(timestamp)

    solidFile.close()

    return timestamps


def displayTimestamps(Ptimestamps, PweekDay):

    analysis_helper: list[DAY_USAGE] = []
    results: list[str] = []

    print("Analysing timestamps.")

    for day in PweekDay:

        totalconsumption = 0.0
        totalcost = 0.0

        for timestamp in Ptimestamps:

            if day == timestamp.weekday:
                totalconsumption += timestamp.consumption
                totalcost += timestamp.consumption * timestamp.price

        day_usage = DAY_USAGE(
            day,
            totalconsumption,
            totalcost
        )

        analysis_helper.append(day_usage)

    print("Displaying results.")
    print("### Electricity consumption summary ###")

    for item in analysis_helper:

        result = (
            f" - {item.weekday} usage "
            f"{item.consumption:.2f} kWh, "
            f"cost {item.cost:.2f} €"
        )

        results.append(result)

    for result in results:
        print(result)

    print("### Electricity consumption summary ###")

    return results


# Keep the original function names as well
def readFile(PfileName):
    return readTimestamps(PfileName)


def calculateTotal(Ptimestamps, PweekDay):
    return displayTimestamps(Ptimestamps, PweekDay)


def main():

    weekDay = (
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    )

    print("Program starting.")

    fileName = input("Insert filename: ")

    timestamps = readTimestamps(fileName)

    displayTimestamps(timestamps, weekDay)

    print("Program ending.")


if __name__ == "__main__":
    main()
