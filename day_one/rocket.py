import unittest

def sum_fuel_calcuations(modules_mass_file):
    return sum(calculate_total_fuel_requirements_of_modules(modules_mass_file))


def calculate_total_fuel_requirements_of_modules(modules_mass_file):
    for module in module_mass_file_lines(modules_mass_file):
        yield calculate_total_fuel_requirement_of_module(module)


def calculate_total_fuel_requirement_of_module(module_mass):
    module_fuel_cost = calculate_fuel_cost_for_mass(module_mass)
    return module_fuel_cost + calculate_additional_fuel_cost(module_fuel_cost)


def calculate_additional_fuel_cost(fuel_mass):
    if fuel_mass > 0:
        fuel_cost = calculate_fuel_cost_for_mass(fuel_mass)
        return fuel_cost + calculate_additional_fuel_cost(fuel_cost)
    return 0


def calculate_fuel_cost_for_mass(mass):
    fuel_cost_for_mass = (mass // 3) - 2
    return fuel_cost_for_mass if fuel_cost_for_mass > 0 else 0


def module_mass_file_lines(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield int(line)


class TestRocketModuleFuelCalculations(unittest.TestCase):

    def test_fuel_calculation_when_mass_requires_no_additional_fuel(self):
        self.assertEqual(calculate_total_fuel_requirement_of_module(14), 2)

    def test_fuel_calculation_when_mass_requires_additional_fuel(self):
        self.assertEqual(calculate_total_fuel_requirement_of_module(1969), 966)
        self.assertEqual(calculate_total_fuel_requirement_of_module(100756), 50346)

if __name__ == '__main__':
    unittest.main()