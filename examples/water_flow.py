#Ehijie Omijie

import math

def water_column_height(tower_height, tank_height):
    """Calculate and return the height of a column of water from a tower height and a tank wall height."""
    h = tower_height + (3 * tank_height) / 4
    return h

def pressure_gain_from_water_height(height):
    """Calculate and return the pressure caused by Earth's gravity pulling on the water stored in an elevated tank."""
    density_water = 998.2  # kg/m^3
    gravity = 9.80665  # m/s^2
    pressure = (density_water * gravity * height) / 1000
    return pressure

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """Calculate and return the water pressure lost because of the friction between the water and the walls of a pipe."""
    density_water = 998.2  # kg/m^3
    pressure_loss = (-friction_factor * pipe_length * density_water * fluid_velocity**2) / (2000 * pipe_diameter)
    return pressure_loss

# If you want to run this file directly for testing purposes, you can add a simple main function
if __name__ == "__main__":
    print(water_column_height(48.3, 12.8))  # Expected: 57.9
    print(pressure_gain_from_water_height(30.2))  # Expected: 295.628
    print(pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.75))  # Expected: -113.008
