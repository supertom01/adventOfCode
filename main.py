import importlib
import pkgutil

from day_base import Day

YEAR = 2025

if __name__ == '__main__':
    # Import all the days in the days package
    for (module_loader, name, ispkg) in pkgutil.iter_modules([str(YEAR)]):
        importlib.import_module('.' + name, str(YEAR))

    # Run all the run methods of the days
    print("Initializing day classes and fetching input data from AoC site...")
    percentage = 0
    step_size = 100.0 / len(Day.__subclasses__())
    days = []
    for c in Day.__subclasses__():
        days.append(c())
        percentage += step_size
        print(f"\r{percentage:3.0f}% done", end="")
    print("\rFinished!\r\n")
    for day in sorted(days, key=lambda day: day.day_nr):
        try:
            day.run()
        except Exception as e:
            print(f"Warning exception occurred for {day.__class__.__name__}: {e}")
            print()
