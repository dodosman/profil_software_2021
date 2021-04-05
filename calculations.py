import pandas as pd
from coinpaprika import client as Coinpaprika
import itertools, operator


class CryptoHandler:

  def __init__(self, coin_name):
    self.client = Coinpaprika.Client()
    self.coin_name = coin_name

  def _create_start_end_times(self, date_start, date_end):
    self.start_time = f"{date_start}T00:00:00Z"
    self.end_time = f"{date_end}T00:00:00Z"
    return self

  def name_of_CryptCurnecy(self, coin_name):

    self._curency_name = f"{coin_name}"
    return self

  def _convert_to_df(self, date_start, date_end):
    self._create_start_end_times(date_start, date_end)
    dict_raw = self.client.candles(self.coin_name, start=self.start_time, end=self.end_time)
    df_raw = pd.DataFrame(dict_raw)
    df = df_raw.filter(items=["time_close", "close"])
    return df

  def average_by_month(self, date_start, date_end):
    df = self._convert_to_df(date_start, date_end)
    df["month"] = pd.DatetimeIndex(df['time_close']).month
    self.df_gb = df.groupby("month")["close"].mean()
    print(round(self.df_gb, 2))

  def high_cumulative_growth(self, date_start, date_end):
    dict_raw = self.client.candles("self.coin_name", start=f"{date_start}T00:00:00Z", end=f"{date_end}T00:00:00Z")
    a = []
    dates = []
    for i in range(len(dict_raw)):
      a.append(dict_raw[i]["close"])
      dates.append(dict_raw[i]["time_close"][:10])

    b = list(range(len(a)))
    for i in range(len(a)):
      if a[i] > a[i - 1]:
        b[i] = True
      elif a[i] < a[i - 1]:
        b[i] = False
      else:
        b[i] = False

    r = max((list(y) for (x, y) in itertools.groupby((enumerate(b)), operator.itemgetter(1)) if x == True), key=len)
    min_index = r[0][0]
    max_index = r[-1][0]
    print("Longest consecutive period was from", dates[min_index], "to", dates[max_index], "with increase of:$",
          round(a[max_index] - a[min_index], 2))

  def _export_json(self, filename):
    self.df.to_json(f'{filename}.json', orient="records")

  def export(self, date_start, date_end, format, filename):
    df = self._convert_to_df(date_start, date_end)

  def export(self, date_start, date_end, format, filename):
    df = self._convert_to_df(date_start, date_end)

    if format == "csv":
      df.to_csv(f'{filename}.csv')
    elif format == "json":
      df.to_json(f'{filename}.json', orient="records")
    else:
      print("We don't support other types os saving files, please type format .json or .csv.")


if __name__ == '__main__':
  main()
