import enum

from day_base import Day


class Pulse(enum.Enum):
    LOW = 0
    HIGH = 1
    NONE = 2


class Day20(Day):

    def __init__(self):
        super().__init__(2023, 20, 'Pulse Propagation', debug=False)
        
    def part_a(self):
        modules = dict()
        inputs = dict()

        # Parsing
        for line in self.input:
            tm, outputs = line.split(' -> ')
            outputs = outputs.split(', ')
            name = tm if tm == 'broadcaster' else tm[1:]
            if tm == 'broadcaster':
                modules[tm] = {
                    "outputs": outputs,
                    "type": 'broadcaster'
                }
            elif tm[0] == '%':
                modules[tm[1:]] = {
                    "on": False,
                    "input": [],
                    "outputs": outputs,
                    "pulse": Pulse.NONE,
                    "type": '%'
                }
            else:
                modules[tm[1:]] = {
                    "received_pulses": dict(),
                    "input": [],
                    "outputs": outputs,
                    "pulse": Pulse.NONE,
                    "type": '&'
                }

            for output in outputs:
                if output not in inputs.keys():
                    inputs[output] = []
                inputs[output].append(name)

        for module_name, input_list in inputs.items():
            if module_name in modules:
                modules[module_name]['input'] = input_list
                if modules[module_name]['type'] == '&':
                    for input in input_list:
                        modules[module_name]['received_pulses'][input] = Pulse.LOW

        # Algorithm!
        high_pulses = 0
        low_pulses = 0
        for i in range(100):
            low_pulses += 1
            active_modules = ['broadcaster']
            while len(active_modules) != 0:
                triggered_modules = []
                for active_module in active_modules:
                    output_modules = modules[active_module]['outputs']
                    output_pulses = dict()

                    # Determine the pulses that are send out
                    if modules[active_module]['type'] == 'broadcaster':
                        for output_module in output_modules:
                            output_pulses[output_module] = Pulse.LOW
                            low_pulses += 1
                    elif modules[active_module]['type'] == '%':
                        modules[active_module]['on'] = not modules[active_module]['on']
                        if modules[active_module]['on']:
                            for output_module in output_modules:
                                output_pulses[output_module] = Pulse.HIGH
                                high_pulses += 1
                        else:
                            for output_module in output_modules:
                                output_pulses[output_module] = Pulse.LOW
                                low_pulses += 1
                    elif modules[active_module]['type'] == '&':
                        if all(received_pulse == Pulse.HIGH for received_pulse in modules[active_module]['received_pulses'].values()):
                            for output_module in output_modules:
                                output_pulses[output_module] = Pulse.LOW
                                low_pulses += 1
                        else:
                            for output_module in output_modules:
                                output_pulses[output_module] = Pulse.HIGH
                                high_pulses += 1

                    # Figure out which modules are activated
                    for output_module in output_modules:
                        if output_module not in modules.keys():
                            continue
                        elif modules[output_module]['type'] == '%' and output_pulses[output_module] == Pulse.LOW:
                            triggered_modules.append(output_module)
                        elif modules[output_module]['type'] == '&':
                            triggered_modules.append(output_module)
                            modules[output_module]['received_pulses'][active_module] = output_pulses[output_module]

                active_modules = triggered_modules

        return low_pulses * high_pulses


if __name__ == '__main__':
    (Day20()).run()

