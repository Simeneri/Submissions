



import sys

def convert_units(inches, unit):
    if unit == "-mm":
        return round(inches * 25.4, 2)
    elif unit == "-cm":
        return round(inches * 2.54, 2)
    elif unit == "-m":
        return round(inches * 0.0254, 2)
    else:
        return "Invalid unit. Choose either '-mm', '-cm', or '-m'."

def test_convert_units():
    result = convert_units(1, "-mm")
    assert result == 25.4, f"Expected 25.4, but got {result}"

    result = convert_units(1, "-cm")
    assert result == 2.54, f"Expected 2.54, but got {result}"

    result = convert_units(1, "-m")
    assert result == 0.0254, f"Expected 0.0254, but got {result}"

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-t":
        test_convert_units()
    else:
        inches = float(input("Enter the value in inches: "))
        unit = input("Enter the unit to convert to (-mm, -cm, -m): ")
        result = convert_units(inches, unit)
        print(f"{inches} inches is equal to {result} {unit}.")

