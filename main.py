
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


def readFile(PfileName):
    timestamps: list[TIMESTAMP] = []

    print(f'Reading file "{PfileName}".')

    solidFile = open(PfileName, "r", encoding="utf-8")
    solidFile.readline()  # Skip header

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


def calculateTotal(Ptimestamps, PweekDay):

    analysis_helper: list[DAY_USAGE] = []
    results: list[str] = []

    print("Analysing timestamps.")

    for day in PweekDay:

        # Gatherers
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


def main():

    weekDay = (
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturnday",
        "Sunday"
    )

    print("Program starting.")

    fileName = input("Insert filename: ")

    timestamps = readFile(fileName)

    calculateTotal(timestamps, weekDay)

    print("Program ending.")


main()
