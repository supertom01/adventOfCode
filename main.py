import importlib
import pkgutil

from days.day import Day

if __name__ == '__main__':
    # Import all the days in the days package
    for (module_loader, name, ispkg) in pkgutil.iter_modules(["days"]):
        importlib.import_module('.' + name, "days")

    # Run all the run methods of the days
    for c in Day.__subclasses__():
        c().run()
