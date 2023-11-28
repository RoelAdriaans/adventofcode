import sys

MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

day_name = "{{ cookiecutter.day }}"
year_name = "{{ cookiecutter.year }}"

# Convert to int:
try:
    int_day_name = int(day_name)
except ValueError:
    print(f"ERROR: day_name: {day_name} is not a valid integer!")
    sys.exit(1)

try:
    int_year_name = int(year_name)
except ValueError:
    print(f"ERROR: day_name: {year_name} is not a valid integer!")
    sys.exit(1)

if not (1 <= int_day_name <= 25):
    print(f"ERROR: day_name: {day_name} is not a valid day, must be between 1 and 25")
    sys.exit(1)

if not (2015 <= int_year_name <= 2025):
    print(
        f"ERROR: day_name: {day_name} is not a valid day, must be between 2015 and 2025"
    )
    sys.exit(1)

# Check that we have a leading zero when needed:
prefix_day_name = f"{int_day_name:02d}"
if prefix_day_name != day_name:
    print(f"ERROR: day_name: {day_name} must have a leading zero")
    sys.exit(1)
