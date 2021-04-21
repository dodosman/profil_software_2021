import click

from calculations import CryptoHandler


@click.group(chain=True)
def main():
    pass


@main.command()
@click.option("--coin", help="enter a desired name of crypto currency", required=True)
@click.option("--date_start", help="enter start date", required=True)
@click.option("--date_end", help="enter end date", required=True)
def average_by_month(coin, date_start, date_end):
    ch = CryptoHandler()
    ch.average_by_month(coin, date_start, date_end)


@main.command()
@click.option("--coin", help="enter a desired name of crypto currency", required=True)
@click.option("--date_start", help="enter start date", required=True)
@click.option("--date_end", help="enter end date", required=True)
def high_cumulative_growth(coin, date_start, date_end):
    ch = CryptoHandler()
    ch.high_cumulative_growth(coin, date_start, date_end)


@main.command()
@click.option("--coin", help="enter a desired name of crypto currency", required=True)
@click.option("--date_start", help="enter start date", required=True)
@click.option("--date_end", help="enter end date", required=True)
@click.option(
    "--file_format",
    help="enter a format of saved file, could be csv or json",
    required=True,
)
@click.option("--filename", help="enter a name for a saved file")
def export(coin, date_start, date_end, file_format, filename):
    ch = CryptoHandler()
    ch.export(coin, date_start, date_end, file_format, filename)


if __name__ == "__main__":
    main()
