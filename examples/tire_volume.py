#Ehijie Omijie


#Additional features - Added a conditional statement to collect extra information from the user and store in the Volumes.txt file then also get
#give the user an option to purchase the tire(s)
import math
from datetime import datetime

# Get user input for tire properties
tire_width = float(input("Enter the width of the tire in mm (ex 205): "))
tire_aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
wheel_diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

# Using the formula, calculate for the numerator and finally -
# divide it by the denominator
numerator = math.pi * (tire_width**2) * tire_aspect_ratio * ((tire_width * tire_aspect_ratio) + (2540 * wheel_diameter))
denominator = 10000000000
tire_volume = numerator / denominator

# Print the tire volume with 2 decimal places
print(f"The approximate volume is {round(tire_volume, 2)} liters")

print("Thank you for using the tire volume calculator.")
