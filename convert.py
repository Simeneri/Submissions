
def convert_length(value, from_unit, to_unit):
    """Converts a length value from one unit to another"""
    conversion_factors = {
        "ft": 12,
        "in": 1,
        "mm": 1/25.4,
        "cm": 1/2.54,
        "m": 1/0.0254
    }
    return value * conversion_factors[from_unit] / conversion_factors[to_unit]

def convert_volume(value, from_unit, to_unit):
    """Converts a volume value from one unit to another"""
    conversion_factors = {
        "pt": 1,
        "qt": 2,
        "cup": 0.5,
        "ml": 0.00211338,
        "dl": 0.0211338,
        "l": 2.11338
    }
    return value * conversion_factors[from_unit] / conversion_factors[to_unit]

# Define a dictionary of valid units for length and volume
valid_units = {
    "length": ["ft", "in", "mm", "cm", "m"],
    "volume": ["pt", "qt", "cup", "ml", "dl", "l"]
}

# Prompt the user for input until they enter valid units
while True:
    from_type = input("Enter type of measurement to convert (length/volume): ")
    if from_type not in valid_units:
        print("Invalid type of measurement. Choose 'length' or 'volume'.")
        continue
    from_unit_options = ", ".join(valid_units[from_type])
    from_unit = input(f"Enter {from_type} units to convert from ({from_unit_options}): ")
    if from_unit not in valid_units[from_type]:
        print(f"Invalid {from_type} unit.")
        continue
    to_unit = input(f"Enter {from_type} units to convert to ({from_unit_options}): ")
    if to_unit not in valid_units[from_type]:
        print(f"Invalid {from_type} unit.")
        continue
    break

# Prompt the user for the value to convert
value = float(input(f"Enter {from_unit} value to convert: "))

# Convert the value
if from_type == "length":
    result = convert_length(value, from_unit, to_unit)
    print(f"{value} {from_unit} = {result} {to_unit}")
else:
    result = convert_volume(value, from_unit, to_unit)
    print(f"{value} {from_unit} = {result} {to_unit}")
