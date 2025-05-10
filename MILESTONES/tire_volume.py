#Ehijie Omijie


#Additional features - Added a conditional statement to collect extra information from the user and store in the Volumes.txt file then also get
#give the user an option to purchase the tire(s) and also collected names of customer for record purposes and easy accessibilty.

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

# Ask if the user wants to buy tires
buy_tires = input("Do you want to buy tires with these dimensions? (yes/no): ").lower()

# Check user's response
if buy_tires == "yes":
    # Prompt for the user's phone number
    phone_number = input("Please enter your phone number: ")

    # Get the current date and time
    current_date_and_time = datetime.now()

    # Open the file for appending text
    with open("volumes.txt", "a") as tire_file:
        # Write tire properties, volume, phone number, and date/time to the file
        tire_file.write(f"{current_date_and_time}: Tire Width: {tire_width} mm, Aspect Ratio: {tire_aspect_ratio}, "
                        f"Wheel Diameter: {wheel_diameter} inches, Volume: {tire_volume:.2f} liters, "
                        f"Phone Number: {phone_number}\n")
        print("Thank you! Your information has been recorded.")

else:
    print("Thank you for using the tire volume calculator.")

#printing the contents
with open("volumes.txt", "r") as file:
    file_contents = file.read()
print("Tire Properties")
print(file_contents)

user_name = input("Please enter your name: ")

