import click

from solutions import day01, day02, day03

modules = [
    (day01.Day1PartA, ("day01/day_01_part01.txt", "day01/day_01_test.txt")),
    (day01.Day1PartB, ("day01/day_01_part01.txt",)),
    (day02.Day2PartA, ("day02/day_02.txt",)),
    (day02.Day2PartB, ("day02/day_02.txt",)),
    (day03.Day3PartA, ("day03/day_03.txt",)),
    (day03.Day3PartB, ("day03/day_03.txt",)),
]


@click.command()
@click.option(
    "--module", type=click.Choice([i[0].__name__ for i in modules]), required=True
)
def main(module):
    """
    Simple program that runs a module from the advent of code
    """
    item = [item for item in modules if item[0].__name__ == module]
    if not item:
        print(f"Module {module} not found")
        return False
    else:
        item = item[0]

    print(f"Running module '{item[0].__name__}'")

    class_to_run = item[0]
    class_instance = class_to_run()
    for filename in item[1]:
        res = class_instance(filename)
        print(f"Result for {filename} -> {res}")


if __name__ == "__main__":
    main()
