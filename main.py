import importlib
import pkgutil

from day_base import Day

YEAR = 2021

if __name__ == '__main__':
    # Import all the days in the days package
    for (module_loader, name, ispkg) in pkgutil.iter_modules([str(YEAR)]):
        importlib.import_module('.' + name, str(YEAR))

    # Run all the run methods of the days
    for c in Day.__subclasses__():
        c().run()
