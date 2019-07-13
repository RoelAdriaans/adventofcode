from solutions import day01

import click

modules = {
    (day01.Day1PartA, "day01_a", ("../data/day01/day_01_part01.txt",)),
    (day01.Day1PartB, "day01_b", ("../data/day01/day_01_part01.txt",)),
}


@click.command()
@click.option("--module", type=click.Choice([i[1] for i in modules]))
def main(module):
    """
    Simple program that runs a module from the advent of code
    """
    item = [item for item in modules if item[1] == module]
    if not item:
        print(f"Module {module} not found")
        return False
    else:
        item = item[0]

    print(f"Processing '{item[1]}' with file '{item[2]}'")

    class_to_run = item[0]
    class_instance = class_to_run()
    res = class_instance(*item[2])

    print(f"Result: {res}")


if __name__ == "__main__":
    main()
