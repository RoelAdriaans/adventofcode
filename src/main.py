import click

from solutions import day01, day02, day03, day04, day05, day06, day07, day08

modules = [
    (day01.Day1PartA, ("day01/day_01_part01.txt", "day01/day_01_test.txt")),
    (day01.Day1PartB, ("day01/day_01_part01.txt",)),
    (day02.Day2PartA, ("day02/day_02.txt",)),
    (day02.Day2PartB, ("day02/day_02.txt",)),
    (day03.Day3PartA, ("day03/day_03.txt",)),
    (day03.Day3PartB, ("day03/day_03.txt",)),
    (day04.Day4PartA, ("day04/day_04.txt",)),
    (day04.Day4PartB, ("day04/day_04.txt",)),
    (day05.Day5PartA, ("day05/day_05.txt",)),
    (day05.Day5PartB, ("day05/day_05.txt",)),
    (day06.Day06PartA, ("day_06/day06.txt",)),
    (day06.Day06PartB, ("day_06/day06.txt",)),
    (day07.Day07PartA, ("day_07/day07.txt",)),
    (day07.Day07PartB, ("day_07/day07.txt",)),
    (day08.Day08PartA, ("day_08/day08.txt", "day_08/day08_input_a.txt")),
    (day08.Day08PartB, ("day_08/day08.txt", "day_08/day08_input_a.txt")),
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

    for filename in item[1]:
        class_to_run = item[0]
        class_instance = class_to_run()
        res = class_instance(filename)
        print(f"Result for {filename} -> {res}")


if __name__ == "__main__":
    main()
