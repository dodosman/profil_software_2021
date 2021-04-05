from calculations import CryptoHandler
import click

@click.group(chain = True)
def main():
    pass

@main.command()
@click.option('--date_start', help='enter a starting date to show the range of avg price')
@click.option('--date_end', help='enter an ending date to show the range of avg price')
def average_by_month(date_start, date_end): #EXPORT

  ch = CryptoHandler()
  ch.average_by_month(date_start, date_end)

  # if export:
  # 	ch.export()

@main.command()
@click.option('--date_start', help='enter a starting date to show the range of avg price')
@click.option('--date_end', help='enter an ending date to show the range of avg price')
def high_cumulative_growth(date_start, date_end):
  ch = CryptoHandler()
  ch.high_cumulative_growth(date_start, date_end)

@main.command()
@click.option('--date_start', help='enter a starting date to show the range of avg price')
@click.option('--date_end', help='enter an ending date to show the range of avg price')
@click.option('--format', help='enter a format of saved file, could be csv or json.')
@click.option('--filename', help='enter a name for a saved file.')
def export(date_start, date_end, format, filename):
  ch = CryptoHandler()
  ch.export(date_start, date_end, format, filename)


if __name__ == '__main__':
  main()


