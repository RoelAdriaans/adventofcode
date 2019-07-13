from solutions import day01

import click

modules = {
    (day01.Day1PartA, "day01_a", ("day01/day_01_part01.txt", "day01/day_01_test.txt")),
    (day01.Day1PartB, "day01_b", ("day01/day_01_part01.txt",)),
}


@click.command()
@click.option("--module", type=click.Choice([i[1] for i in modules]), required=True)
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

    print(f"Running module '{item[1]}'")

    class_to_run = item[0]
    class_instance = class_to_run()
    for filename in item[2]:
        res = class_instance(filename)
        print(f"Result for {filename} -> {res}")


if __name__ == "__main__":
    main()
